"""
-------------------------------------------------
MHub - Data Sorter Module
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

import os
import subprocess
import shutil

from mhubio.core import Config, Module, UnsortedInstance, SortedInstance, InstanceData, DataType, FileType, CT, DirectoryChain
from mhubio.modules.importer.DataImporter import DataImporter

class DataSorter(Module):
    """
    Sort Module (without imports).
    Operates only on the input direcory. 
    Agnostic to instances.
    Organize patient data in a unique folder structure.
    For now, the static schema is: %SeriesInstanceUID/dicom/%SOPInstanceUID.dcm
    """

    def __init__(self, config: Config):
        super().__init__(config)

        # get directory chain based on the data handler and the configured base dir
        # NOTE: setting `input_dir` or òutput_dir` to an absolute path (starting with /) will override the data handler prefix path and make it an entrypoint instead. 
        self.in_dc = DirectoryChain(path=self.c['input_dir'], parent=self.config.data.dc)
        self.out_dc = DirectoryChain(path=self.c['output_dir'], parent=self.config.data.dc)
        
        # bypass mode
        self.bypass: bool = bool(self.c['bypass']) if 'bypass' in self.c else False

    # override instance generator 
    def _generateInstance(self, path: str) -> SortedInstance:
        return SortedInstance(path)

    def sort(self) -> None:       
        
        # print schema
        schema = os.path.join(self.out_dc.abspath, self.c['structure'])
        self.v("sorting schema:",  schema)

        # create output folder if required
        if not os.path.isdir(self.out_dc.abspath):
            os.makedirs(self.out_dc.abspath)

        # compose command
        bash_command = [
            "dicomsort", 
            "-k", "-u",
            self.in_dc.abspath, 
            schema
        ]

        # print command in debug mode
        if self.config.debug:
            print(">> run: ", " ".join(bash_command))

        # run command
        _ = subprocess.run(bash_command, check=True, text=True)

    def getSeriesIDs(self):
        return os.listdir(self.out_dc.abspath)

    def task(self) -> None:

        if not self.bypass:
            self.sort()
        else:
            self.v("Sorting is bypassed.")