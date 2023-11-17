# type: ignore
"""
-------------------------------------------------
MHub - Data handler class for the mhubio framework
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg (27.02.2023)
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

from typing import List, Dict, Optional
from .DirectoryChain import DirectoryChainInterface
from .DataType import DataType
from .FileType import FileType
from .templates import CT, SEG
from enum import Enum
import uuid, os


class DGraph:
    base = '/app/data'
    steps: List['Step']
    nodes: List['Node']

    def filter(self, ref_type: DataType, confirmed_only: bool = True) -> List['Node']: 
        """
        Filter for instance data by a reference data type. Only instance data that match the file type and specified meta data of the reference type are returned. A datatype matches the reference type, if all metadata of the reference type is equal to the datatype. If a datatype contains additional meta data compared to the reference type (specialization) those additional keys are ignored. 
        """

        # collect only instance data passing all checks (ftype, meta)
        matching_nodes: List['Node'] = []

        # iterate all instance data of this instance
        for node in self.nodes:
            # check if data is confirmed
            if confirmed_only and not node.confirmed:
                continue

            # check file type, ignore other filetypes
            if ref_type.ftype is not FileType.NONE and not node.type.ftype == ref_type.ftype:
                continue

            # check if metadata is less general than ref_type's metadata
            if not node.type.meta <= ref_type.meta:
                continue
          
            # add instance data that passes all prior checks
            matching_nodes.append(node)

        # return matches
        return matching_nodes
    

class StepType(str, Enum):
    Import = 'import'
    Convert = 'convert'
    Organize = 'organize'
    Generate = 'generate'
    Process = 'process'

class Step:
    graph: DGraph
    descriptor: str
    type: StepType

    # TODO: support multiple filter datatypes (just go from single to list and set merge) 
    #       but simpler now to keep it single fro poc / initial experiments
    def __init__(self, graph: DGraph, descriptor: str, type: StepType, ins: DataType, outs: List['Node']) -> None:
        self.graph = graph
        self.descriptor = descriptor
        self.type = type

        # filter input nodes
        in_nodes = self.graph.filter(ins)

        # create output nodes
        


class Node:
    step: Step
    ins: List['Node']
    outs: List['Node']
    type: DataType
    path: str
    confirmed: bool

    def __init__(self, path: str, type: DataType, step: Step) -> None:
        self.path = path
        self.step = step
        self.type = type
        self.type = type

    def confirm(self) -> None:
        self.confirmed = True

#TODO: use DataType instead of FileType

if __name__ == "__main__":
    print("Test Graph STructure")

    graph = DGraph()

    # import nodes
    import_step = Step(graph, 'import', StepType.Import)
    n1 = Node('dicom', DataType(FileType.DICOM, CT), import_step)
    n2 = Node('nrrd', DataType(FileType.NRRD, SEG), import_step)

    # convert nodes to nifti
    convert_step = Step(graph, 'convert', StepType.Convert)
    n3 = Node('nifti', DataType(FileType.NIFTI, CT), convert_step)
    n3.ins = [n1]
    n1.outs += [n3]

    n4 = Node('nifti', DataType(FileType.NIFTI, SEG), convert_step)
    n4.ins = [n2]
    n2.outs += [n4]

    # rescale
    rescale_step = Step(graph, 'rescale', StepType.Process)
    n5 = Node('nifti', DataType(FileType.NIFTI, CT + {'scaled': 'xyz'}), rescale_step)
    n5.ins = [n3, n4]
    n3.outs += [n5]

    # run model (generates 2 roi)
    run_step = Step(graph, 'model', StepType.Generate)
    n6 = Node('nifti', DataType(FileType.NIFTI, SEG + {'roi': 'heart'}), run_step)
    n6.ins = [n4, n5]
    n4.outs += [n6]
    n5.outs += [n6]

    n7 = Node('nifti', DataType(FileType.NIFTI, SEG + {'roi': 'lung'}), run_step)
    n7.ins = [n4, n5]
    n4.outs += [n7]
    n5.outs += [n7]

    # convert again (or generate?)
    convert_step2 = Step(graph, 'dseg_convert', StepType.Convert)
    n8 = Node('dseg', DataType(FileType.DICOMSEG, SEG), convert_step2)
    n8.ins = [n1, n6, n7]
    n1.outs += [n8]
    n6.outs += [n8]
    n7.outs += [n8]



class DataHandler2(DirectoryChainInterface):
    # base:         str
    # _instances:   List[Instance]
    # _tmpdirs:     Dict[str, str]

    def __init__(self, base: str) -> None:
        self._instances: List[Instance] = []
        self._tmpdirs: Dict[str, List[str]] = {}

        super().__init__(path=base, base=None, parent=None)
        self.dc.makeEntrypoint()
        assert self.dc.isEntrypoint()

    @property
    def instances(self) -> List['Instance']:
       return self._instances

    @instances.setter
    def instances(self, instances: List['Instance']) -> None:
        for instance in instances:
            instance.handler = self
        self._instances = instances

    def addInstance(self, instance: 'Instance') -> None:
        assert instance not in self._instances, "Error: instance already added to data handler."
        instance.handler = self
        self._instances.append(instance)

    def getInstances(self, sorted: bool, type: 'DataType') -> List['Instance']:
        i_type = SortedInstance if sorted else UnsortedInstance
        return [i for i in self.instances if isinstance(i, i_type) and i.hasType(type)]

    def requestTempDir(self, label: Optional[str] = None) -> str:
        abs_base = "/app/tmp"
        dir_name = str(uuid.uuid4())
        path  = os.path.join(abs_base, dir_name)

        # remember temporary abspath by label
        if label is None:
            # TODO: what about a garbage-collection like system for tmp dirs, allowing auto-release by label name? Otherwise, we can always just erase the entire /tmp stack. Only when disc space is an issue + a lot of files are generated (and never released) this should be considered. 
            print("WARNING: No label set for temporary dir.")
        else:
            if label not in self._tmpdirs:
                self._tmpdirs[label] = []
            self._tmpdirs[label].append(path)

        # make path
        os.makedirs(path)

        # return
        return path

    def export_yml(self, path: str) -> None:
        instances = []
        for instance in self.instances:
            instance_dict = {
                'attr': instance.attr,
                'dc': {
                    'path': instance.dc.path,
                    'base': instance.dc.base
                },
                'data': []
            }
            for data in instance.data:
                data_dict = {
                    'path': data.dc.path,
                    'type': data.type.toString(),
                    'has_bundle': 'yes' if data.bundle else 'no',
                    'confirmed': data.confirmed
                }
                instance_dict['data'].append(data_dict)
            instances.append(instance_dict)

        #
        import yaml
        with open(path, 'w') as f:
            yaml.dump(instances, f)

    def import_yml(self, path: str) -> None:
        from mhubio.core import Instance, InstanceData, DataType
        
        # read yml
        import yaml
        with open(path, 'r') as f:
            instances = yaml.load(f, Loader=yaml.FullLoader)

        # clean instances
        self.instances = []

        # create instances
        for instance in instances:

            # create instance
            i = Instance(path=instance['dc']['path'])
            i.attr = instance['attr']
            self.addInstance(i)

            # add data
            for data in instance['data']:
                d = InstanceData(data['path'], DataType.fromString(data['type']))
                
                if data['confirmed']:
                    d.confirm()

                i.addData(d)

    def printInstancesOverview(self, level: str = "data+meta"):
        assert level in ["data", "meta", "data+meta"]
        for instance in self.instances:
            if level == "data":
                instance.printDataOverview(meta=False)
            elif level == "meta":
                instance.printDataMetaOverview()
            elif level == "data+meta":
                instance.printDataOverview(meta=True)


# avoiding circular imports
from .Instance import Instance, SortedInstance, UnsortedInstance