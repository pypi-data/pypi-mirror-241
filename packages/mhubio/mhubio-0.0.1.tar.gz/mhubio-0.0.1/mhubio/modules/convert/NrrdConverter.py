"""
-------------------------------------------------
MHub - Dicom2Nrrd Conversion Module
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""


from typing import Optional, Dict, Any

from .DataConverter import DataConverter
from mhubio.core import Instance, InstanceData, DataType, FileType, IO, DataTypeQuery

import os
import pyplastimatch as pypla # type: ignore

# TODO: consider renaming less inzuitive 'target' to 'input'
# TODO: consider using default IO.Config decorators, e.g. IO.Config.InputSelector which are similar for all implementations
# TODO: allow for reg-ex based input matching for configs?
@IO.Config('targets', DataTypeQuery, 'nifti|dicom|mha:mod=ct', factory=DataTypeQuery, the='target data types to convert to nrrd')
class NrrdConverter(DataConverter):
    """
    Conversion module. 
    Convert instance data from dicom to nrrd.
    """
    
    targets: DataTypeQuery

    def convert(self, instance: Instance) -> Optional[InstanceData]:

        # filter data
        in_data = instance.data.filter(self.targets).first()

        # cretae a converted instance
        #assert instance.hasType(DataType(FileType.DICOM)), f"CONVERT ERROR: required datatype (dicom) not available in instance {str(instance)}."
        #dicom_data = instance.data.filter(DataType(FileType.DICOM)).first()
        assert in_data is not None, f"CONVERT ERROR: required datatype ({self.targets}) not available in instance {str(instance)}."

        # out data
        nrrd_data = InstanceData("image.nrrd", DataType(FileType.NRRD, in_data.type.meta), instance=instance, auto_increment=True)

        # paths
        out_log_file = os.path.join(instance.abspath, "_pypla.log")

        # sanity check
        #assert(os.path.isdir(inp_dicom_dir))

        # DICOM CT to NRRD conversion (if the file doesn't exist yet)
        if os.path.isfile(nrrd_data.abspath):
            print("CONVERT ERROR: File already exists: ", nrrd_data.abspath)
            return None
        else:
            convert_args_ct: Dict[str, Any] = {
                "input" : in_data.abspath,
                "output-img" : nrrd_data.abspath
            }

            # clean old log file if it exist
            if os.path.isfile(out_log_file): 
                os.remove(out_log_file)
            
            # run conversion using plastimatch
            pypla.convert(
                verbose=self.config.verbose,
                path_to_log_file=out_log_file,
                **convert_args_ct
            )

            return nrrd_data
    