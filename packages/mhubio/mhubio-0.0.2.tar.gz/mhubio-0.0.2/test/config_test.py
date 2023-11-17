import unittest
import os, yaml, uuid
from mhubio.core import Config, Instance, InstanceData, DataType, FileType
from mhubio.core.Config import config_argument_parser
from mhubio.modules.importer.NrrdImporter import NrrdImporter

class ConfigurationTest(unittest.TestCase):

    def test_default_configuration(self):
        
        default_config = {
            'general': {
                'data_base_dir': '/app/data'
            },
            'modules': {}
        }
        
        # instantiate config
        config = Config()

        # assertion
        self.assertDictEqual(default_config, config._config)

    def test_file_configuration(self):
        
        # path to the configuration file used for testing
        config_file = '/home/leonard/Projects/mhub/organization/mhubio/test/config.yml'
        self.assertTrue(os.path.isfile(config_file))

        # instantiate config
        config = Config(config_file)

        # load config yaml manually
        with open(config_file, 'r') as f:
            file_config_dict = yaml.safe_load(f)

        # assertion
        self.assertDictEqual(file_config_dict, config._config)

    def test_explicit_configuration(self):
        
        # define some explicit configuration dict
        explicit_configuration = {
            'general': {
                'data_base_dir': '/some/data/folder',
                '_test_random': str(uuid.uuid4())
            },
            'modules': {}
        }

        # instantiate config with explicit config dict
        config = Config(config=explicit_configuration)

        # assertion
        self.assertDictEqual(explicit_configuration, config._config)

    def test_file_and_explicit_configuration(self):
        
        # path to the configuration file used for testing
        config_file = '/home/leonard/Projects/mhub/organization/mhubio/test/config.yml'
        self.assertTrue(os.path.isfile(config_file))

        # define explicit configuration to parially override and extend the file-loaded config
        explicit_configuration = {
            'general': {
                'data_base_dir': str(uuid.uuid4()),
                '_test_random': str(uuid.uuid4())
            },
            'modules': {
                '_test_random': str(uuid.uuid4())
            }
        }

        # instantiate config
        config = Config(config_file, explicit_configuration)

        # load config yaml manually
        with open(config_file, 'r') as f:
            file_config_dict = yaml.safe_load(f)

        # assertion
        self.assertEqual(explicit_configuration['general']['_test_random'], config._config['general']['_test_random'])
        self.assertEqual(explicit_configuration['modules']['_test_random'], config._config['modules']['_test_random'])

        self.assertEqual(explicit_configuration['general']['data_base_dir'], config._config['general']['data_base_dir'])

        t = file_config_dict
        t['general']['data_base_dir'] = explicit_configuration['general']['data_base_dir']  # set expected override
        t['general']['_test_random'] = explicit_configuration['general']['_test_random']    # set expected override
        t['general']['_test_random'] = explicit_configuration['general']['_test_random']    # set expected override
        t['modules']['_test_random'] = explicit_configuration['modules']['_test_random']    # set expected override
        self.assertDictEqual(t, config._config)

    def test_file_and_arg_configuration(self):
           
        # path to the configuration file used for testing
        config_file = '/home/leonard/Projects/mhub/organization/mhubio/test/config.yml'
        self.assertTrue(os.path.isfile(config_file))

        # argument to set threshold value to 400 insead of the defined 300
        args = ['--config:modules#ThresholdingRunner#TH=400']

        # instantiate config
        config = Config(config_file, args=args)

        # test
        self.assertEqual(config._config['modules']['ThresholdingRunner']['TH'], 400)

    def test_argument_parser(self):
        
        args = ['--config:modules#ThresholdingRunner#TH=400']
        parsed = config_argument_parser(args, allow_json_type_parsing=True)
        self.assertDictEqual(parsed, {'modules': {'ThresholdingRunner': {'TH': 400}}})

    def test_arg_type_conversion(self):

        # define arguments with different type values
        args = [
            '--config:some#key#path#str=str',               # string
            '--config:some#key#path#int=100',               # int
            '--config:some#key#path#float=1.0',             # float    
            '--config:some#key#path#bool=True',             # bool
            '--config:some#key#path#none=None',             # None
            '--config:some#key#path#list=[1,2,3]',          # list 
            '--config:some#key#path#dict={"a": 1, "b": 2}'  # dict
        ]

        # instantiate config
        config = Config(args=args)

        # validate types
        self.assertEqual(type(config._config['some']['key']['path']['str']), str)
        self.assertEqual(type(config._config['some']['key']['path']['int']), int)
        self.assertEqual(type(config._config['some']['key']['path']['float']), float)
        self.assertEqual(type(config._config['some']['key']['path']['bool']), bool)
        self.assertEqual(config._config['some']['key']['path']['none'], None)
        self.assertEqual(type(config._config['some']['key']['path']['list']), list)
        self.assertEqual(type(config._config['some']['key']['path']['dict']), dict)


class PathConcatenationTest(unittest.TestCase):
    
    def setUp(self) -> None:
        
        # define explicit configuration
        explicit_configuration = {
            'general': {
                'data_base_dir': '/tmp/mhubio/test/base'
            }
        }

        # create shared config
        self.config = Config(config=explicit_configuration)

    def test_base_path(self) -> None:
        config = self.config

        # check the base path on the data handler
        self.assertEqual(config.data.dc.abspath, '/tmp/mhubio/test/base')

    def test_instance_path(self) -> None:
        config = self.config

        # create instance
        instance = Instance(path = "instance/path")

        # set instance
        config.data.instances = [instance]

        #
        self.assertEqual(instance.handler, config.data)
        self.assertEqual(instance.abspath, '/tmp/mhubio/test/base/instance/path')

    def test_instance_data_path(self) -> None:
        config = self.config

        # create instance
        instance = Instance(path = "instance/path")

        # set instance
        config.data.instances = [instance]

        # instance data
        data = InstanceData('some_file.ext', DataType(FileType.NONE))
        instance.addData(data)

        #
        self.assertEqual(instance.handler, config.data)
        self.assertEqual(data.instance, instance)
        self.assertEqual(instance.abspath, '/tmp/mhubio/test/base/instance/path')
        self.assertEqual(data.dc.base, None)
        self.assertEqual(data.abspath, '/tmp/mhubio/test/base/instance/path/some_file.ext')

    def test_instance_data_base(self) -> None:
        config = self.config

        # create instance
        instance = Instance(path = "instance/path")

        # set instance
        config.data.instances = [instance]

        # instance data
        data = InstanceData('some_file.ext', DataType(FileType.NONE))
        data.dc.setBase('/tmp/mhubio/test/extbase')
        instance.addData(data)

        #
        self.assertEqual(instance.handler, config.data)
        self.assertEqual(data.instance, instance)
        self.assertEqual(instance.abspath, '/tmp/mhubio/test/base/instance/path')
        self.assertEqual(data.dc.base, '/tmp/mhubio/test/extbase')
        self.assertEqual(data.abspath, '/tmp/mhubio/test/extbase/some_file.ext')


class ModuleConfigTest(unittest.TestCase):

    def setUp(self) -> None:
        
        # create shared config
        config_file = '/home/leonard/Projects/mhub/organization/mhubio/test/config.yml'
        self.config = Config(config_file)

    def test_import_module_config(self):
        importer = NrrdImporter(self.config)

        self.assertEqual(importer.c['input_dir'] , 'input_data')
        


if __name__ == '__main__':
    unittest.main()
