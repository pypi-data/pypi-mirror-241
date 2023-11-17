import unittest, os, shutil

from mhubio.core import Config, DataType, FileType, CT, InstanceData, Instance, Meta, MHubMissingDataError
from mhubio.modules.convert.NiftiConverter import NiftiConverter, NiftiConverterEngine

BASE_DIR = '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure3'

# NOTE: Consider running this example on /structure2. 
#           BASE_DIR = '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure2'
#
#       First, we'd have to declare the instance path for patient 1 like so: 
#           patient1_dir = os.path.join(BASE_DIR, 'dcm', 'patient1')
#           patient1 = Instance(patient1_dir)
#           self.config.data.instances = [patient1]
#       And adding the dicom data like so:
#           patient1_dicom_data = InstanceData("", DataType(FileType.DICOM, CT), patient1)
#       Which results in the following absolute paths:
#           patient1.abspath    == '/home/leonard/Projects/mhub/organization/mhubio/test2/data/dcm2/patient1'
#           patient1_dicom_data == '/home/leonard/Projects/mhub/organization/mhubio/test2/data/dcm2/patient1/'
#       Where the latter has a trailing slash because data path was "" and on.path.join adds a trailing slash if the last item is empty string.
#   
#       DISCUSSION POINT 1: think about wheather ALL DIRECTORIES should always have a trailing slash to distinguish them from files. 
#       This also helps figuring the dicom / nifti (folder / file) issue.
#       This, however, needs to be properly implemented, documented and tested (should become a policy) but also needs to be implemented in a way, that for all DirectorChain items that
#       cannot be a file, a chekc is made and, if required, the trailing path added. 
#       Carefully weight the benefits (does it make code cleaner) or drawbacks (does it make code more complex or even break path comparisons 
#       if slashes are added more or less unexpectedly).
#       
#       Now, if we run the converter (which at this point has no additional path configuration exposed):
#           NiftiConverter(self.config).execute()
#       All files will be created in the patient1 instance path, which at the same time is the dicom director.
#
#       DISCUSSION POINT 2: At this point, it becomes apparent, that the output path is determined by the converter 
#       (always in the instance's data folder) but thereby is 'fixed' to the initial structure.
#       As we have a structure dicom/patientX, we cannot resolve this into nifti/patientX. 
#       We need to think about if this is a limitation or if we thereby (beneficially) enforce a certain structure.

class NiftiConversionUsingPlastimatchTest(unittest.TestCase):

    def setUp(self) -> None:
        # create nifti folder or clean existing one
        # NOTE: not relevant, as nifti files are placed under instance's abspath
        #       (which is the current COnverter behaviour that cannot (yet) be configurized)
        #self.data_converted_dir = os.path.join(BASE_DIR, 'nifti')
        #shutil.rmtree(self.data_converted_dir, ignore_errors=True)
        #os.mkdir(self.data_converted_dir)

        if os.path.isfile(os.path.join(BASE_DIR, 'patient1',  'nifti', 'dcm.pmconv.log')):
            os.remove(os.path.join(BASE_DIR, 'patient1', 'nifti', 'dcm.pmconv.log'))

        if os.path.isfile(os.path.join(BASE_DIR, 'patient1',  'nifti', 'dcm.nii.gz')):
            os.remove(os.path.join(BASE_DIR, 'patient1', 'nifti', 'dcm.nii.gz'))

        # config
        config_dict = {
            'general': {
                'data_base_dir': BASE_DIR
            }
        }

        # instantiate config
        self.config = Config(config=config_dict)
        self.config.verbose = True
        self.config.debug = True

        # create instance
        patient1_dir = os.path.join(BASE_DIR, 'patient1')
        patient1 = Instance(patient1_dir)
        self.config.data.instances = [patient1]

        # add data
        # NOTE: instance is passed as third argument which will automatically link data to that instance calling instance.addData() which in turn also sets teh data's instance (data.instance = instance) which then set's the instance as the parent in the directory chain
        InstanceData('dcm', DataType(FileType.DICOM, CT), patient1)

    def test_patient1_abspath(self):
        
        # NOTE: DataHandler.getInstance() should not have a 'sorted' boolean parameter but an optional instanceType instead. That instanceType must be a descendand of Instance (e.g. SortedInstance or UnsortedInstance). However, if no type is set, any Instance is valid to be returned. In addition, further query parameters (e.g. has specific file type etc) might be included in instance fetching? But likely to complex. As a (solid) workaround, just use data.instances directly instead of the getInstances() method.

        # fetch patient from config instances
        instances = self.config.data.instances
        print("----> num instances on patient 1", len(instances))
        self.assertTrue(len(instances) == 1)
        patient1 = instances[0]

        # check patient1 instance path
        # NOTE: no trailing slash
        self.assertEqual(patient1.abspath, '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure3/patient1')

        # check patient1 instance data path
        # NOTE: no trailing slash
        data = patient1.data.filter(DataType(FileType.DICOM, CT)).first()
        self.assertEqual(data.abspath, '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure3/patient1/dcm')

    def test_dicom_to_nifti_conversion(self):

        # expected log and nifti file paths
        expected_log_path = os.path.join(BASE_DIR, 'patient1',  'nifti', 'dcm.pmconv.log')
        expected_nifti_path = os.path.join(BASE_DIR, 'patient1', 'nifti', 'dcm.nii.gz')

        # these files shoul dnot exis (are cleaned in setUp so far, consider moving here!)
        self.assertFalse(os.path.isfile(expected_log_path))
        self.assertFalse(os.path.isfile(expected_nifti_path))

        # conversion module
        converter = NiftiConverter(self.config)
        
        # convert
        converter.execute()

        # get instance
        instances = self.config.data.instances
        self.assertTrue(len(instances) == 1)
        patient1 = instances[0]

        # fetch nifti data from instance      
        nifti_data = patient1.data.filter(DataType(FileType.NIFTI)).first()
        self.assertEqual(nifti_data.abspath, expected_nifti_path)

        # check log data
        log_data = patient1.data.filter(DataType(FileType.LOG, Meta(**{'log-task': 'conversion'}))).first()
        self.assertEqual(log_data.abspath, expected_log_path)

        # now we expect the files to be created
        self.assertTrue(os.path.isfile(expected_log_path))
        self.assertTrue(os.path.isfile(expected_nifti_path))

    def test_engine_override(self):
        # NOTE: in NiftiConversionUsingDcmqiTest we test, that the engine is correctly read from the config. Here we test the programmatic override.

        # create converter module
        converter = NiftiConverter(self.config)

        # check default engine
        self.assertEqual(converter.engine, NiftiConverterEngine.PLASTIMATCH)

        # override engine
        converter.engine = NiftiConverterEngine.DCM2NIIX

        # check engine
        self.assertEqual(converter.engine, NiftiConverterEngine.DCM2NIIX)

class NiftiConversionUsingDcmqiTest(unittest.TestCase):

    def setUp(self) -> None:
        # create nifti folder or clean existing one
        # NOTE: not relevant, as nifti files are placed under instance's abspath
        #       (which is the current COnverter behaviour that cannot (yet) be configurized)
        #self.data_converted_dir = os.path.join(BASE_DIR, 'nifti')
        #shutil.rmtree(self.data_converted_dir, ignore_errors=True)
        #os.mkdir(self.data_converted_dir)

        if os.path.isfile(os.path.join(BASE_DIR, 'patient1',  'nifti', 'dcm.pmconv.log')):
            os.remove(os.path.join(BASE_DIR, 'patient1',  'nifti', 'dcm.pmconv.log'))

        if os.path.isfile(os.path.join(BASE_DIR, 'patient1', 'nifti', 'dcm.nii.gz')):
            os.remove(os.path.join(BASE_DIR, 'patient1', 'nifti', 'dcm.nii.gz'))


        # config
        config_dict = {
            'general': {
                'data_base_dir': BASE_DIR
            },
            'modules': {
                'NiftiConverter': {
                    'engine': 'dcm2niix'
                },
            }
        }

        # instantiate config
        self.config = Config(config=config_dict)
        self.config.verbose = True
        self.config.debug = True

        # create instance
        patient1_dir = os.path.join(BASE_DIR, 'patient1')
        patient1 = Instance(patient1_dir)
        self.config.data.instances = [patient1]

        # add data
        patient1_dicom_data = InstanceData('dcm', DataType(FileType.DICOM, CT), patient1)

    def test_patient1_abspath(self):
        
        # NOTE: DataHandler.getInstance() should not have a 'sorted' boolean parameter but an optional instanceType instead. That instanceType must be a descendand of Instance (e.g. SortedInstance or UnsortedInstance). However, if no type is set, any Instance is valid to be returned. In addition, further query parameters (e.g. has specific file type etc) might be included in instance fetching? But likely to complex. As a (solid) workaround, just use data.instances directly instead of the getInstances() method.

        # fetch patient from config instances
        instances = self.config.data.instances
        self.assertTrue(len(instances) == 1)
        patient1 = instances[0]

        # check patient1 instance path
        # NOTE: no trailing slash
        self.assertEqual(patient1.abspath, '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure3/patient1')

        # check patient1 instance data path
        # NOTE: no trailing slash
        data = patient1.data.filter(DataType(FileType.DICOM, CT)).first()
        self.assertEqual(data.abspath, '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure3/patient1/dcm')

    def test_dicom_to_nifti_conversion(self):

        # expected log and nifti file paths
        unexpected_log_path = os.path.join(BASE_DIR, 'patient1', '_pypla.log')
        expected_nifti_path = os.path.join(BASE_DIR, 'patient1', 'nifti', 'dcm.nii.gz')

        # these files shoul dnot exis (are cleaned in setUp so far, consider moving here!)
        self.assertFalse(os.path.isfile(unexpected_log_path))
        self.assertFalse(os.path.isfile(expected_nifti_path))

        # conversion module
        converter = NiftiConverter(self.config)
        
        # check engine is set to dcm2nii
        print("modes: ", NiftiConverterEngine.__members__)
        self.assertEqual(converter.engine, NiftiConverterEngine.DCM2NIIX)

        # convert
        converter.execute()

        # get instance
        instances = self.config.data.instances
        self.assertTrue(len(instances) == 1)
        patient1 = instances[0]

        # fetch nifti data from instance      
        nifti_data = patient1.data.filter(DataType(FileType.NIFTI)).first()
        self.assertEqual(nifti_data.abspath, expected_nifti_path)

        # no log data (fetching them will raise an IndexError exception)
        # TODO: raise a proper error in the future instead of only printing a warning in Instance.getData() method if no matches found.
        fetch = patient1.data.filter(DataType(FileType.LOG, Meta(origin='plastimatch')))
        self.assertRaises(MHubMissingDataError, fetch.first)

        # now we expect the files to be created
        self.assertFalse(os.path.isfile(unexpected_log_path))
        self.assertTrue(os.path.isfile(expected_nifti_path))

