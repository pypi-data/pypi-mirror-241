"""
-------------------------------------------------
MHub - Generate Dicom files from NRRD or NIFTI
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
Date:   17.04.2023
-------------------------------------------------
"""

from typing import Optional, List
from mhubio.core import Config, Module, Instance, InstanceData, DataType, FileType, Meta, CT, IO, InstanceDataCollection
import os, pydicom, SimpleITK as sitk, numpy as np, shutil


@IO.Config('targets', List[DataType], ['dicom:mod=ct', 'nrrd:mod=ct'], factory=IO.F.list(DataType.fromString), the='target data types to convert to nifti')
class DicomConverter(Module):
    """
    Convert NRRD or NIFTI to Dicom.
    """

    targets: List[DataType]

    def setTarget(self, target: DataType) -> None:
        self.targets.append(target)

    # FIXME: temporarily override the task method.
    def task(self):
        self.convert()

    def generate_dicom(self, input_file: str, output_directory: str):

        # Load NRRD or NIfTI data


        # Load NRRD or NIfTI data
        image = sitk.ReadImage(input_file)

        # print spacing, origin, direction and shape of the image
        print('Spacing:   ', image.GetSpacing())
        print('Origin:    ', image.GetOrigin())
        print('Direction: ', image.GetDirection())
        print('Shape:     ', image.GetSize())

        # Get the image array and metadata
        image_array = sitk.GetArrayFromImage(image)
        spacing = image.GetSpacing()
        origin = image.GetOrigin()
        direction = image.GetDirection()

        print("set slice thickness to:", spacing[2])

        # Set a small non-zero value for masked or zero values
        min_nonzero_value = 1e-6
        image_array[image_array <= 0] = min_nonzero_value

        # Create a directory to store the DICOM files
        output_directory = 'path/to/output/directory'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Loop through each slice of the 3D image and create a DICOM file for each slice
        for i in range(image_array.shape[0]):
            # Create a Pydicom Dataset
            ds = pydicom.Dataset()

            # 
            ds.SpecificCharacterSet = 'ISO_IR 100'
            ds.ImageType = ['ORIGINAL', 'PRIMARY', 'AXIAL']
            ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.2'             # CT Image Storage
            ds.SOPInstanceUID = pydicom.uid.generate_uid() # type: ignore
            ds.StudyDate = '20210417'
            ds.SeriesDate = '20210417'
            ds.StudyTime = '120000'
            ds.SeriesTime = '120000'
            ds.ContentTime = '120000'
            ds.AccessionNumber = ''
            ds.Modality = 'CT'
            ds.Manufacturer = 'MHub'
            ds.ReferringPhysicianName = ''
            ds.StudyDescription = 'No study description'
            ds.SeriesDescription = 'No series description'
            ds.ManufacturerModelName = 'MHub'
            ds.PatientName = 'Generated'
            ds.PatientID = '00000000'
            ds.PatientBirthDate = ''
            ds.PatientSex = ''
            ds.PatientAge = ''
            ds.PatientWeight = ''
            ds.SLiceThickness = 3 #spacing[2]
            ds.PatientPosition = 'HFS'
            ds.StudyInstanceUID = pydicom.uid.generate_uid() # type: ignore
            ds.SeriesInstanceUID = pydicom.uid.generate_uid() # type: ignore
            ds.StudyID = 'SLICER10001'
            ds.SeriesNumber = '1'
            ds.InstanceNumber = str(i + 1)
            ds.ImagePositionPatient = [-195, -171.7, -45.25]
            ds.ImageOrientationPatient = [1, 0, 0, 0, 1, 0]
            ds.FrameOfReferenceUID = '1.2.826.0.1.3680043.8.498.82029394104607732472778277387791844316'
            ds.PositionReferenceIndicator = ''
            ds.SamplesPerPixel = 1
            ds.PhotometricInterpretation = 'MONOCHROME2'
            ds.Rows = 512#image_array.shape[1]
            ds.Columns = 512#image_array.shape[2]
            ds.PixelSpacing = [0.3515625, 0.3515625]
            ds.BitsAllocated = 16
            ds.BitsStored = 16
            ds.HighBit = 15
            ds.PixelRepresentation = 1
            ds.WindowCenter = 40
            ds.WindowWidth = 350
            ds.RescaleIntercept = 0
            ds.RescaleSlope = 1
            ds.RescaleType = 'HU'
            ds.PixelData = image_array[i].tobytes()


            # Set DICOM metadata
            ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.2'  # CT Image Storage
            ds.SOPInstanceUID = pydicom.uid.generate_uid() # type: ignore
            ds.Modality = 'CT'
            ds.PatientName = 'Patient Name'
            ds.PatientID = 'Patient ID'
            ds.SeriesDescription = 'CT Series'
            ds.StudyDescription = 'CT Study'
            ds.SpacingBetweenSlices = spacing[2]
            ds.SliceThickness = spacing[2]
            ds.Rows = image_array.shape[1]
            ds.Columns = image_array.shape[2]
            ds.PixelSpacing = [spacing[1], spacing[0]]
            ds.ImageOrientationPatient = [direction[0], direction[1], direction[3], direction[4], direction[6], direction[7]]
            ds.ImagePositionPatient = [origin[0] + i * direction[0] * spacing[0], 
                                    origin[1] + i * direction[3] * spacing[1], 
                                    origin[2] + i * direction[6] * spacing[2]]
            ds.SliceLocation = origin[2] + i * spacing[2]
            ds.SamplesPerPixel = 1
            ds.PixelRepresentation = 0
            ds.BitsAllocated = 16
            ds.BitsStored = 12
            ds.HighBit = 11
            ds.PixelData = image_array[i].tobytes()

            # Set the transfer syntax to little-endian explicit VR
            ds.is_little_endian = True
            ds.is_implicit_VR = False

            # Save the DICOM file
            dicom_file_path = os.path.join(output_directory, f'slice{i + 1:03d}.dcm')
            pydicom.filewriter.write_file(dicom_file_path, ds) # type: ignore

            print(f'Saved DICOM file: {dicom_file_path}')

    @IO.Instance()
    @IO.Inputs('in_datas', IO.C('targets'), the="data to be converted")
    @IO.Outputs('out_datas', path='generated_dicom', dtype='dicom', data='in_datas', the="generated dicom data")
    def convert(self, instance: Instance, in_datas: InstanceDataCollection, out_datas: InstanceDataCollection) -> None:
        
        # some sanity checks
        assert isinstance(in_datas, InstanceDataCollection)
        assert isinstance(out_datas, InstanceDataCollection)
        assert len(in_datas) == len(out_datas)

        # conversion step
        for i, in_data in enumerate(in_datas):
            out_data = out_datas.get(i)

            # check if output data already exists
            #if os.path.isfile(out_data.abspath) and not self.overwrite_existing_file:
            #    print("CONVERT ERROR: File already exists: ", out_data.abspath)
            #    continue

            # generate dicom files
            self.generate_dicom(in_data.abspath, out_data.abspath)
        