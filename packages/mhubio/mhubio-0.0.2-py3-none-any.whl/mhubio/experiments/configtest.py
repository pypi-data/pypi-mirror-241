# TODO: remove sys hacks once in final (package-like) structure
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))) 

# imports
from mhubio.core.Config import Config
from mhubio.modules.runner.ModelRunner import TotalSegmentatorRunner

config = Config('../config.yml')

print(config[TotalSegmentatorRunner])

print("----")
from mhubio.core.Config import Instance, InstanceData, DataType, FileType, CT
from mhubio.modules.organizer.DataOrganizer import DataOrganizer

inst1 = Instance("/test/instance1")
inst1.attr["sid"] = "1.232424.121326465"
config.data.instances = [inst1]
assert inst1.handler == config.data, "instance handler was not set automatically."

d0 = InstanceData("file1.nii", DataType(FileType.NIFTI, CT))
d1 = InstanceData("file1.nii", DataType(FileType.NRRD, CT))
d2 = InstanceData("file2.nrrd", DataType(FileType.NRRD, CT + {"model": "TotalSegmentator"}))
inst1.addData(d0)
inst1.addData(d1)
inst1.addData(d2)
assert d1.instance == inst1, "data instance was not set automatically"

print("d2, resolved: ", DataOrganizer(config).resolveTarget("/test/org/[i:id]/[i:sid]-[d:mod]-[d:model].ext", d2))

org = DataOrganizer(config)
org.dry = True
org.setTarget(DataType(FileType.NRRD), "/test/org/[i:id]-[d:mod]/[d:model]/[random]/[path]")
# -> dry copy /test/instance1/file2.nrrd to /test/org/76e56283-ca2d-4fe2-92d8-59aa649cd8e5-ct/TotalSegmentator/776a0b5d-eac6-4bff-9ad4-3355a77c68ed/file2.nrrd

org.execute()
