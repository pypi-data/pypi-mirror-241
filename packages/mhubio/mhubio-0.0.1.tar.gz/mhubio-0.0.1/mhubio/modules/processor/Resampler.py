"""
-------------------------------------------------
MHub - DataResampler module to resample images
       with plastimatch
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

from typing import List, Dict, Any
from mhubio.core import Instance, DataType, InstanceDataCollection, InstanceData, FileType, Meta, IO
from mhubio.modules.processor.DataProcessor import DataProcessor

import os
import pyplastimatch as pypla

@IO.Config('sources', List[DataType], ['nifti:mod=seg:roi=*', 'nrrd:mod=seg:roi=*'], factory=IO.F.list(DataType.fromString), the='target segmentation files to convert to dicomseg')
@IO.Config('target', DataType, 'dicom:mod=ct', factory=DataType.fromString, the='target file to resample to')
class Resampler(DataProcessor):

    sources: List[DataType]
    target: DataType


    @IO.Instance()
    @IO.Inputs("in_segs", IO.C("source_segs"), the="input data to convert to dicomseg")
    @IO.Input("in_dicom", IO.C("target_dicom"), the="input dicom data to convert to dicomseg")
    @IO.Outputs('out_data', path=IO.C('converted_file_name'), dtype='dicomseg:mod=seg', data='in_dicom', bundle=IO.C('bundle_name'), auto_increment=True, the="converted data")
    def task(self, instance: Instance, in_segs: InstanceDataCollection, in_dicom: InstanceData, out_data: InstanceData) -> None:

        # input filter
        in_datas = instance.data.filter("NIFTI:part=ADC")

        # fixed filter
        fixed_data = instance.data.first("NIFTI:part=T2")

        # simple assertions 
        assert len(in_datas) > 0, "At least one input data is required"

        # simple case
        assert len(in_datas) == 1, "Only one input data is allowed"
        in_data = in_datas.asList()[0]

        # output data
        out_data = InstanceData('resampled.nii.gz', DataType(FileType.NIFTI, in_data.type.meta + {'resampled_to': 'T2'}), data=in_data)

        # log data
        log_data = InstanceData('_pypla.log', DataType(FileType.LOG, in_data.type.meta + {
            "log-origin": "plastimatch",
            "log-task": "resampling",
            "log-caller": "Resampler",
            "log-instance": str(instance)
        }), data=in_data, auto_increment=True)

        # process
        resample_args: Dict[str, Any] = {
            'input': in_data.abspath,
            'output': out_data.abspath,
            'fixed': fixed_data.abspath,
        }

        # TODO add log file
        pypla.resample(
            verbose=self.config.verbose,   
            path_to_log_file=log_data.abspath,
            **resample_args
        )

        # check if log was created to confirm log
        if os.path.isfile(log_data.abspath):
            log_data.confirm()

        # check if file was created
        if not os.path.isfile(out_data.abspath):
            print("RESAMPLE FAILED: {out_data.abspath} was not created")
            return 
        
        out_data.confirm()