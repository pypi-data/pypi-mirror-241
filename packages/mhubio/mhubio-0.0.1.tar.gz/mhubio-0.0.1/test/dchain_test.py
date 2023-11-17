from typing import Optional
import unittest, os
from mhubio.core import DirectoryChain, DirectoryChainInterface, DataHandler, Instance, InstanceData, DataType, FileType, CT

class DirectoryChainTest(unittest.TestCase):

    def test_simple_chaining(self):
        dc1 = DirectoryChain(path="a")
        dc2 = DirectoryChain(path="b", parent=dc1)
        dc3 = DirectoryChain(path="c", parent=dc2)
        self.assertEquals(dc3.abspath, "a/b/c")

    def test_siple_base(self):
        dc1 = DirectoryChain(path="b", base="a")
        self.assertEquals(dc1.abspath, "a/b")

    def test_chaining_with_base(self):
        dc1 = DirectoryChain(path="b", base="a")
        dc2 = DirectoryChain(path="c", parent=dc1)
        self.assertEquals(dc2.abspath, "a/b/c")

    def test_base_override(self):
        dc1 = DirectoryChain(path="b", base="a")
        dc2 = DirectoryChain(path="c", parent=dc1, base="d")
        self.assertEquals(dc2.abspath, "d/c")

        dc3 = DirectoryChain(path="e", parent=dc2)
        self.assertEquals(dc3.abspath, "d/c/e")

    def test_empty_path(self):
        # setting a path to an empty string, NOT NONE
        dc1 = DirectoryChain(path="")
        dc2 = DirectoryChain(path="", parent=dc1)
        dc3 = DirectoryChain(path="", parent=dc2)
        self.assertEquals(dc3.abspath, "")

    def test_empty_path2(self):
        dc1 = DirectoryChain(path="b", base="a")
        dc2 = DirectoryChain(path="", parent=dc1)
        dc3 = DirectoryChain(path="c", parent=dc2)
        self.assertEquals(dc3.abspath, "a/b/c")

    def test_empty_base(self):
        # setting a base to an empty string, NOT NONE
        dc1 = DirectoryChain(base="", path="a")
        self.assertEquals(dc1.abspath, "a")

    def test_empty_base2(self):
        # setting a base to an empty string, NOT NONE
        dc1 = DirectoryChain(path="b", base="a")
        dc2 = DirectoryChain(path="c", parent=dc1, base="")
        dc3 = DirectoryChain(path="d", parent=dc2)
        self.assertEquals(dc3.abspath, "c/d")

    def test_implemential_path_injection(self):
        class DirectoryChainImplementer(DirectoryChainInterface):
            def __init__(self, ref: str, base: Optional[str] = None):
                super().__init__(path=ref, base=base)
                self.ref = ref
            
        dci1 = DirectoryChainImplementer(ref="b", base="a")
        self.assertEquals(dci1.abspath, "a/b")

        dci2 = DirectoryChainImplementer(ref="c", base="d")
        dci2.dc.setParent(dci1.dc)
        self.assertEquals(dci2.abspath, "d/c")

        dci3 = DirectoryChainImplementer(ref="e")
        dci3.dc.setParent(dci2.dc)
        self.assertEquals(dci3.abspath, "d/c/e")

        dci2.dc.setBase(None)
        self.assertEquals(dci3.abspath, "a/b/c/e")

class InstanceImplementationTest(unittest.TestCase):

    def setUp(self):

        self.base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test2/data/"
        self.dataHandler = DataHandler(base=self.base_dir)

        # create instance
        self.instance_path = "instance1"
        self.instance = Instance(path=self.instance_path)
        
        # append instance to data handler (this sets the .handler property on the instance)
        # NOTE: self.dataHandler.instances.append(instance) would not work
        self.dataHandler.instances = [self.instance]

         # create instance data
        self.instance_data_path = "data1"
        self.instance_data = InstanceData(path=self.instance_data_path, type=DataType(FileType.NONE))
        
        # add data to instance (this sets the .instance property on the instance data to the instance)
        self.instance.addData(self.instance_data)


    def test_instance_data_handler_binding(self):
        self.assertEqual(self.instance.handler, self.dataHandler)

    def test_instance_data_instance_binding(self):
        self.assertEqual(self.instance_data.instance, self.instance)

    def test_data_handler(self):
        self.assertEquals(self.dataHandler.dc.base, "/")
        self.assertEquals(self.dataHandler.abspath, self.base_dir)
    
    def test_instance(self):
        self.assertEquals(self.instance.abspath, os.path.join(self.base_dir, self.instance_path))
        self.assertEquals(self.instance.dc.base, None)
        self.assertEquals(self.instance.dc.parent, self.dataHandler.dc)

    def test_instance_data(self):
        self.assertEquals(self.instance_data.abspath, os.path.join(self.base_dir, self.instance_path, self.instance_data_path))
        self.assertEquals(self.instance_data.dc.parent, self.instance.dc)

    def test_absolute_path_instance_data(self):

        # create instance data (my/data1)
        # CASE 1: set empty base, uses path (relative or absolute) as the entrypoint
        d1 = InstanceData(path="my/data1", type=DataType(FileType.NONE))
        d1.dc.setBase("")

        # CASE 3: set / as base, uses path (always absolute) as entrypoint
        d2 = InstanceData(path="my/data1", type=DataType(FileType.NONE))
        d2.dc.setBase("/")

        d3 = InstanceData(path="/my/data1", type=DataType(FileType.NONE))
        d3.dc.setBase("/")

        # CASE 4: set base, uses base as the entrypoint (/tmp/my/data1)
        d4 = InstanceData(path="my/data1", type=DataType(FileType.NONE))
        d4.dc.setBase("/tmp")

        # CASE 5: use syntactic sugar method for case 1 and 2
        d5 = InstanceData(path="my/data1", type=DataType(FileType.NONE))
        d5.dc.makeEntrypoint()

        # CASE 6: use absolute path (os.path.join will ignore base or parent)
        d6 = InstanceData(path="/my/data1", type=DataType(FileType.NONE))

        # validate path
        # as the  base is set on d1, d2, d3, d4, paths are the same before and after the data is added to the instance
        self.assertEquals(d1.abspath, "my/data1")
        self.assertEquals(d2.abspath, "/my/data1")
        self.assertEquals(d3.abspath, "/my/data1")
        self.assertEquals(d4.abspath, "/tmp/my/data1")
        self.assertEquals(d5.abspath, "/my/data1")
        self.assertEquals(d6.abspath, "/my/data1")

        # add datat to instance
        self.instance.addData(d1)
        self.instance.addData(d2)
        self.instance.addData(d3)
        self.instance.addData(d4)
        self.instance.addData(d6)

        # validate path
        self.assertEquals(d1.abspath, "my/data1")
        self.assertEquals(d2.abspath, "/my/data1")
        self.assertEquals(d3.abspath, "/my/data1")
        self.assertEquals(d4.abspath, "/tmp/my/data1")
        self.assertEquals(d5.abspath, "/my/data1")
        self.assertEquals(d6.abspath, "/my/data1")

        # d1-d5 have a base set, d6 has no base set
        for d in [d1, d2, d3, d4, d5]: self.assertNotEqual(d.dc.base, None)
        self.assertEquals(d6.dc.base, None)

        # all (d1-d6) are entrypoints
        for d in [d1, d2, d3, d4, d5, d6]:
            self.assertTrue(d.dc.isEntrypoint())


    def test_instance_data_bundle(self):

        # get a data bundle from instance
        data_bundle = self.instance.getDataBundle("my_model_data")
        
        # create some data
        d1 = InstanceData(path="my/dicom", type=DataType(FileType.DICOM))
        d2 = InstanceData(path="my/file.nrrd", type=DataType(FileType.NRRD))
        d3 = InstanceData(path="my/file.nii.gz", type=DataType(FileType.NIFTI))

        # validate path's before being added to the instance data bundle
        self.assertEquals(d1.abspath, "my/dicom")
        self.assertEquals(d2.abspath, "my/file.nrrd")
        self.assertEquals(d3.abspath, "my/file.nii.gz")

        # add data to data bundle
        data_bundle.addData(d1)
        data_bundle.addData(d2)
        data_bundle.addData(d3)

        # validate paths once added to the data bundle
        self.assertEquals(d1.abspath, os.path.join(self.base_dir, self.instance_path, "my_model_data", "my/dicom"))
        self.assertEquals(d2.abspath, os.path.join(self.base_dir, self.instance_path, "my_model_data", "my/file.nrrd"))
        self.assertEquals(d3.abspath, os.path.join(self.base_dir, self.instance_path, "my_model_data", "my/file.nii.gz"))

        # fetch data from instance and check paths
        d = self.instance.data.filter(DataType(FileType.NRRD)).first()
        self.assertEquals(d.abspath, os.path.join(self.base_dir, self.instance_path, "my_model_data", "my/file.nrrd"))

    def test_instance_data_data_bundle(self):

        # get a data bundle from instance
        data_bundle = self.instance.getDataBundle("my_model_data")
        
        # create some data
        d1 = InstanceData(path="my/dicom", type=DataType(FileType.DICOM))
        d2 = InstanceData(path="my/file.nrrd", type=DataType(FileType.NRRD))
        d3 = InstanceData(path="my/file.nii.gz", type=DataType(FileType.NIFTI))

        # add data to data bundle
        data_bundle.addData(d1)
        data_bundle.addData(d2)
        data_bundle.addData(d3)

        # fetch data from instance and check paths
        d = self.instance.data.filter(DataType(FileType.NRRD)).first()
        self.assertEquals(d.abspath, os.path.join(self.base_dir, self.instance_path, "my_model_data", "my/file.nrrd"))

        # create data bundle on fetched data
        data_bundle2 = d.getDataBundle("converted_data")

        # create conversion data
        d4 = InstanceData(path="converted.nii.gz", type=DataType(FileType.NIFTI)) 
        data_bundle2.addData(d4)

        # validate path
        self.assertEqual(d4.abspath, os.path.join(self.base_dir, self.instance_path, "my_model_data", "converted_data", "converted.nii.gz"))
    

    def tearDown(self):
        pass