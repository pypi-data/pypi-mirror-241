"""
-------------------------------------------------
MHub - MHA Conversion Module
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

from mhubio.core import Module, Instance, InstanceDataCollection, InstanceData, DataType, FileType, IO
import os, SimpleITK as sitk
from pathlib import Path

# conversion dependencies
from panimg.image_builders.dicom import image_builder_dicom # type: ignore
from panimg.image_builders.metaio_nrrd import image_builder_nrrd # type: ignore
from panimg.image_builders.metaio_nifti import image_builder_nifti # type: ignore

@IO.ConfigInput('in_datas', 'dicom|nrrd|nifti', the="target data that will be converted to mha")
@IO.Config('allow_multi_input', bool, False, the='allow multiple input files')
@IO.Config('bundle_name', str, 'mha', the="bundle name converted data will be added to")
@IO.Config('converted_file_name', str, '[filename].mha', the='name of the converted file')
@IO.Config('overwrite_existing_file', bool, False, the='overwrite existing file if it exists')
class MhaConverter(Module):
    """
    Conversion module that converts DICOM, NRRD and NIFTI data into MHA.
    """

    allow_multi_input: bool
    bundle_name: str                # TODO. make Optional[str] here and in decorator once supported
    converted_file_name: str
    overwrite_existing_file: bool

    @IO.Instance()
    @IO.Inputs('in_datas', the="data to be converted")
    @IO.Outputs('out_datas', path=IO.C('converted_file_name'), dtype='mha', data='in_datas', bundle=IO.C('bundle_name'), auto_increment=True, the="converted data")
    def task(self, instance: Instance, in_datas: InstanceDataCollection, out_datas: InstanceDataCollection, **kwargs) -> None:

        # some sanity checks
        assert isinstance(in_datas, InstanceDataCollection)
        assert isinstance(out_datas, InstanceDataCollection)
        assert len(in_datas) == len(out_datas)

        # filtered collection must not be empty
        if len(in_datas) == 0:
            print(f"CONVERT ERROR: no data found in instance {str(instance)}.")
            return None

        # check if multi file conversion is enables
        if not self.allow_multi_input and len(in_datas) > 1:
            print("WARNING: found more than one matching file but multi file conversion is disabled. Only the first file will be converted.")
            in_datas = InstanceDataCollection([in_datas.first()])

        # conversion step
        for i, in_data in enumerate(in_datas):
            out_data = out_datas.get(i)

            # check if output data already exists
            if os.path.isfile(out_data.abspath) and not self.overwrite_existing_file:
                print("CONVERT ERROR: File already exists: ", out_data.abspath)
                continue

            # check datatype 
            if in_data.type.ftype == FileType.DICOM:

                # extract dicom files
                # TODO: check if panimg can accept a dicom folder instad
                dcm_files_abspaths = [Path(os.path.join(in_data.abspath, f)) for f in os.listdir(in_data.abspath) if f.endswith(".dcm")]

                # for dicom data use a dicom image builder
                #  as we control the input (one dicom instance) we expect exactly one output. 
                #  We set None as default to avoid StopIteration exceptions in caseof an empty iterator.
                sitk_image = next(image_builder_dicom(files=dcm_files_abspaths), None)
                
            elif in_data.type.ftype == FileType.NRRD:

                # for nrrd files use the nrrd image builder
                sitk_image = next(image_builder_nrrd(files=[Path(in_data.abspath)]), None)

            elif in_data.type.ftype == FileType.NIFTI:

                # for nifti files use the tiff image builder
                sitk_image = next(image_builder_nifti(files=[Path(in_data.abspath)]), None)

            else:
                print("CONVERT ERROR: unsupported file type: ", in_data.type.ftype)
                continue

            # check that we got an image
            if sitk_image is None:
                print("CONVERT ERROR: image builder returned no images.")
                continue

            # write the file via SimpleITK
            sitk.WriteImage(sitk_image.image, out_data.abspath)