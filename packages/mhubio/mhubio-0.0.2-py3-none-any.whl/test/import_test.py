import unittest, os, shutil

from mhubio.core import Config, DataType, FileType, CT
from mhubio.modules.importer.UnsortedDicomImporter import UnsortedInstanceImporter
from mhubio.modules.importer.DataSorter import DataSorter

BASE_DIR_STRUCTURE1 = '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure1'
BASE_DIR_STRUCTURE2 = '/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure2'

class DataSorterTest(unittest.TestCase):

    def setUp(self):

        # clean up 
        shutil.rmtree(os.path.join(BASE_DIR_STRUCTURE1, 'sorted'), ignore_errors=True)
        shutil.rmtree(os.path.join(BASE_DIR_STRUCTURE2, 'sorted'), ignore_errors=True)

        # config
        self.config_dict = {
            'general': {
                'data_base_dir': BASE_DIR_STRUCTURE1
            },
            'modules': {
                'UnsortedInstanceImporter': {
                    'input_dir': 'dcm'
                },
                'DataSorter': {
                    #'base_dir': '/home/leonard/Projects/mhub/organization/mhubio/test2/data/sorted',
                    'structure': '%SeriesInstanceUID/dicom/%SOPInstanceUID.dcm'
                }
            }
        }

    def test_data_sorter_import_with_absolute_base_dir(self):

        # modify config, set absolute base dir
        config_dict = self.config_dict
        config_dict['modules']['DataSorter']['base_dir'] = os.path.join(BASE_DIR_STRUCTURE1, 'sorted')

        # config
        config = Config(config=config_dict)
        config.verbose = True
        config.debug = True

        # import
        importer = UnsortedInstanceImporter(config)
        importer.execute()

        # sort
        sorter = DataSorter(config)
        sorter.execute()

        # instances
        instances = config.data.getInstances(sorted=True, type=DataType(FileType.DICOM, CT))

        # check
        self.assertEqual(len(instances), 1)
        instance = instances[0]

        # get data
        data = instance.data.filter(DataType(FileType.DICOM, CT)).first()

        # get sids from sorter
        sids = sorter.getSeriesIDs()
        sid = sids[0]

        # assert data path
        self.assertEqual(config_dict['modules']['DataSorter']['base_dir'], os.path.join(BASE_DIR_STRUCTURE1, 'sorted'))
        self.assertEqual(data.abspath, os.path.join(BASE_DIR_STRUCTURE1, 'sorted', sid, 'dicom'))

    def test_data_sorter_import_with_relative_base_dir(self):

        # modify config, set absolute base dir
        config_dict = self.config_dict
        config_dict['modules']['DataSorter']['base_dir'] = 'sorted'

        # config
        config = Config(config=config_dict)
        config.verbose = True
        config.debug = True

        # import
        importer = UnsortedInstanceImporter(config)
        importer.execute()

        # sort
        sorter = DataSorter(config)
        sorter.execute()

        # instances
        instances = config.data.getInstances(sorted=True, type=DataType(FileType.DICOM, CT))

        # check
        self.assertEqual(len(instances), 1)
        instance = instances[0]

        # get data
        data = instance.data.filter(DataType(FileType.DICOM, CT)).first()

        # get sids from sorter
        sids = sorter.getSeriesIDs()
        sid = sids[0]

        # assert data path
        self.assertEqual(config_dict['modules']['DataSorter']['base_dir'], 'sorted')
        self.assertEqual(data.abspath, os.path.join(BASE_DIR_STRUCTURE1, 'sorted', sid, 'dicom'))

    def test_data_dry_import_files(self):

        # modify config, set absolute base dir
        config_dict = self.config_dict
        config_dict['modules']['DataSorter']['base_dir'] = 'sorted'
        config_dict['modules']['DataSorter']['bypass'] = True

        # config
        config = Config(config=config_dict)
        config.verbose = True
        config.debug = True

        # import
        importer = UnsortedInstanceImporter(config)
        importer.execute()

        # sort
        sorter = DataSorter(config)
        sorter.execute()

        # instances
        instances = config.data.getInstances(sorted=True, type=DataType(FileType.DICOM, CT))

        # check
        self.assertEqual(len(instances), 1)
        instance = instances[0]

        # get data
        data = instance.data.filter(DataType(FileType.DICOM, CT)).first()

        # assert data path
        self.assertEqual(config_dict['modules']['DataSorter']['base_dir'], 'sorted')
        self.assertEqual(data.abspath, os.path.join(BASE_DIR_STRUCTURE1, 'sorted', 'dicom'))
      
    def test_data_dry_import_folders(self):

        # modify config, set absolute base dir
        config_dict = self.config_dict
        config_dict['general']['data_base_dir'] = BASE_DIR_STRUCTURE2
        config_dict['modules']['DataSorter']['base_dir'] = 'sorted'
        config_dict['modules']['DataSorter']['bypass'] = True

        # config
        config = Config(config=config_dict)
        config.verbose = True
        config.debug = True

        # import
        importer = UnsortedInstanceImporter(config)
        importer.execute()

        # sort
        sorter = DataSorter(config)
        sorter.execute()

        # instances
        instances = config.data.getInstances(sorted=True, type=DataType(FileType.DICOM, CT))

        # check
        self.assertEqual(len(instances), 2)
       
        for instance in instances:

            # get data
            data = instance.data.filter(DataType(FileType.DICOM, CT)).first()

            # assert data path
            self.assertEqual(data.abspath, os.path.join(BASE_DIR_STRUCTURE2, 'sorted', data.instance.attr["ref"], 'dicom'))
