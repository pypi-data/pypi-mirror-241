"""
-------------------------------------------------
MHub - Fake model execution for pipeline testing
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

from typing import List
from mhubio.core import Module, Instance, InstanceData, IO

class DummyRunner(Module):

    @IO.Instance()
    @IO.Input('in_data', 'nifti:mod=ct', the="data to be processed")
    @IO.Output('out_data1', 'file1.nrrd', 'nrrd:mod=seg:roi=Heart', the="processed data")
    @IO.Output('out_data2', 'file2.nrrd', 'nrrd:mod=seg:roi=Ventricle_L,Ventricle_R', the="processed data")
    def task(self, instance: Instance, in_data: InstanceData, out_data1: InstanceData, out_data2: InstanceData) -> None:
        
        # print input data
        print('Dummy runer input data:', in_data.abspath)
        print('Creating dummy output files: ', out_data1.abspath, out_data2.abspath)

        # crate two dummy files
        with open(out_data1.abspath, 'w') as f:
            f.write('dummy1')

        with open(out_data2.abspath, 'w') as f:
            f.write('dummy2')