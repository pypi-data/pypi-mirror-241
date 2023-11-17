from mhubio.core.Config import Config, DataType, FileType, CT, SEG
from mhubio.modules.importer.DataSorter import DataSorter
from modules.convert.NiftiConverter import NiftiConverter
from modules.convert.DsegConverter import DsegConverter
from mhubio.modules.runner.ModelRunner import TotalSegmentatorRunner
from mhubio.modules.organizer.DataOrganizer import DataOrganizer

# clean
import shutil
shutil.rmtree("/app/data/sorted", ignore_errors=True)
shutil.rmtree("/app/data/nifti", ignore_errors=True)
shutil.rmtree("/app/tmp", ignore_errors=True)
shutil.rmtree("/app/data/output_data", ignore_errors=True)

# config
config = Config('config.yml')
config.verbose = False  # TODO: define levels of verbosity and integrate consistently. 

# sort
DataSorter(config).execute()

# convert (ct:dicom -> ct:nifti)
NiftiConverter(config).execute()

# execute model (ct:nifti -> seg:nifti)
TotalSegmentatorRunner(config).execute()

# convert (seg:nifti -> seg:dicomseg)
DsegConverter(config).execute()

# organize data into output folder
organizer = DataOrganizer(config)
organizer.setTarget(DataType(FileType.NIFTI, CT), "/app/data/output_data/[i:SeriesID]/[path]")
organizer.setTarget(DataType(FileType.DICOMSEG, SEG), "/app/data/output_data/[i:SeriesID]/TotalSegmentator.seg.dcm")
organizer.execute()