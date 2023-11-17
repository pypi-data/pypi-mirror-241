"""
-------------------------------------------------
MHub - FileListImporter Module
This module imports files from a file table in
csv, tsv or json format, where each row represents
a file and each column represents a meta data key.
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg 
Email:  leonard.nuernberg@maastrichtuniversity.nl
Date:   02.04.2023
-------------------------------------------------
"""

from typing import List, Dict, Optional 
from typing_extensions import TypedDict, NotRequired
from mhubio.core import Config, Meta, Module, Instance, InstanceData, InstanceDataBundle, DataType, FileType
import os, csv, copy, uuid, re, shutil


class FileStructureImporter(Module):
    """
    File List Importer Module.
    Import data from a list of files and metadata.

    configuration:
        input_dir: str  (default: '')
            The input directory that is scanned for data.
        instance_dir: str (default: 'imported_instances')
            The directory where instances are stored.
    """
   
    def task(self) -> None:
        # scan input definitions
        input_dir = os.path.join(self.config.data.abspath, self.getConfiguration('input_dir', ''))
        instances_dir = os.path.join(self.config.data.abspath, self.getConfiguration('instance_dir', 'imported_instances'))

        