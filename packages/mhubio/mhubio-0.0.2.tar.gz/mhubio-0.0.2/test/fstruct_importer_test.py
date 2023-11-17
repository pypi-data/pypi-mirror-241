import unittest, json, os, copy, shutil
from mhubio.core import Config, DataType, FileType, Meta
from mhubio.modules.importer.FileStructureImporter import FileStructureImporter, scan_directory, extend_meta_from_csv
from mhubio.modules.convert.NiftiConverter import NiftiConverter

class StructuralImporterTest(unittest.TestCase):

    def pretty_print_scan_results(self, scan_results) -> None:
        scan_results_dict = copy.deepcopy(scan_results)
        for i in range(len(scan_results_dict)):
            scan_results_dict[i]['meta'] = dict(scan_results_dict[i]['meta'])

        print(json.dumps(scan_results_dict, indent=4))

    def test_directory_scanner(self):

    
        # input / base directory

        # test/univimp
        # ├── data
        # │   ├── instance1
        # │   │   ├── img
        # │   │   │   └── img2.nrrd
        # │   │   └── seg
        # │   │       └── seg2.nii.gz
        # │   ├── instance2
        # │   │   ├── dicom
        # │   │   │   ├── 0001.dcm
        # │   │   │   └── 0002.dcm
        # │   │   ├── img
        # │   │   │   └── img.nrrd
        # │   │   └── seg
        # │   │       └── seg.nii.gz
        # │   └── mixed
        # │       ├── img3.nrrd
        # │       └── seg3.nii.gz
        # └── utils
        #     └── config.yml
        
        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data"
        self.assertTrue(os.path.exists(base_dir))

        # define structures
        structures = [
            "$sid/$mod/",
            "$sid/seg$mod/$file@nifti",
            "$sid/img$mod/$file@nrrd",
            "$sid/$mod",
            "$ref/",
            "$sid/dicom$mod@dicom",
        #    "mixed/$file@auto"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, [], verbose=False)

        # pretty print results
        self.pretty_print_scan_results(scan_results)

        # check results
        correct_import = [
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1/img/img2.nrrd",
                "meta": {
                    "sid": "instance1",
                    "ref": "instance1",
                    "mod": "img",
                    "file": "img2.nrrd"
                },
                "dtype": "nrrd"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1/seg/seg2.nii.gz",
                "meta": {
                    "sid": "instance1",
                    "ref": "instance1",
                    "mod": "seg",
                    "file": "seg2.nii.gz"
                },
                "dtype": "nifti"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/img/img.nrrd",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2",
                    "mod": "img",
                    "file": "img.nrrd"
                },
                "dtype": "nrrd"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/seg/seg.nii.gz",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2",
                    "mod": "seg",
                    "file": "seg.nii.gz"
                },
                "dtype": "nifti"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/dicom",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2",
                    "mod": "dicom"
                },
                "dtype": "dicom"
            }
        ]

        # remove random ids in scan_results
        for i in range(len(scan_results)):
            scan_results[i]['meta'] = {k: v for k, v in scan_results[i]['meta'].items() if k != 'id'}

        self.assertEquals(scan_results, correct_import)

    def test_import_after_dicomsort(self):
        
        # input / base directory
        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test2/data/structure1"
        self.assertTrue(os.path.exists(base_dir))

        # define structures
        structures = [
            "sorted/$sid@dicom/"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, [], verbose=False)

        # output results
        self.pretty_print_scan_results(scan_results)

        # get sid from folder name manually
        sid = os.listdir(os.path.join(base_dir, 'sorted'))[0]

        # validate results
        self.assertEqual(len(scan_results), 1)
        self.assertEqual(scan_results[0]["dtype"], "dicom")
        assert isinstance(scan_results[0]["meta"], dict)
        self.assertEqual(scan_results[0]["meta"]["sid"], sid)
        self.assertEqual(scan_results[0]["path"], os.path.join(base_dir, 'sorted', sid))

    def test_directory_scanner_with_excludes(self):
        
        # input / base directory
        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data"
        self.assertTrue(os.path.exists(base_dir))

        # define structures
        structures = [
            "$sid/$mod/",
            "$sid/seg$mod/$file@nifti",
            "$sid/img$mod/$file@nrrd",
            "$sid/$mod",
            "$ref/",
            "$sid/dicom@dicom",
        ]

        # exclude dicom folder
        excludes = [
            "$sid/dicom"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, excludes, verbose=True)

        # pretty print results
        self.pretty_print_scan_results(scan_results)

        # check results
        correct_import = [
            {       
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1/img/img2.nrrd",
                "meta": {
                    "ref": "instance1",
                    "sid": "instance1",
                    "mod": "img",
                    "file": "img2.nrrd"
                },
                "dtype": "nrrd"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1/seg/seg2.nii.gz",
                "meta": {
                    "ref": "instance1",
                    "sid": "instance1",
                    "mod": "seg",
                    "file": "seg2.nii.gz"
                },
                "dtype": "nifti"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/img/img.nrrd",
                "meta": {
                    "ref": "instance2",
                    "sid": "instance2",
                    "mod": "img",
                    "file": "img.nrrd"
                },
                "dtype": "nrrd"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/seg/seg.nii.gz",
                "meta": {
                    "ref": "instance2",
                    "sid": "instance2",
                    "mod": "seg",
                    "file": "seg.nii.gz"
                },
                "dtype": "nifti"
            }
        ]

        # remove random ids in scan_results
        for i in range(len(scan_results)):
            scan_results[i]['meta'] = {k: v for k, v in scan_results[i]['meta'].items() if k != 'id'}

        self.assertEquals(scan_results, correct_import)

    def test_directory_scanner_with_instances(self):

        # base directory
        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data"
        self.assertTrue(os.path.exists(base_dir))

        # define structures
        structures = [
            "$sid@instance/$mod/",
            "$sid/seg$mod/$file@nifti",
            "$sid/img$mod/$file@nrrd",
            "$sid/$mod",
            "$ref/",
            "$sid/dicom$mod@dicom",
        ]

        excludes = [
            "mixed",
            "imported_instances"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, excludes, verbose=False)

        # pretty print results
        self.pretty_print_scan_results(scan_results)

        # expexted scan results dict
        correct_import = [
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1",
                "meta": {
                    "sid": "instance1",
                    "ref": "instance1"
                },
                "dtype": "instance"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1/img/img2.nrrd",
                "meta": {
                    "sid": "instance1",
                    "ref": "instance1",
                    "mod": "img",
                    "file": "img2.nrrd"
                },
                "dtype": "nrrd"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance1/seg/seg2.nii.gz",
                "meta": {
                    "sid": "instance1",
                    "ref": "instance1",
                    "mod": "seg",
                    "file": "seg2.nii.gz"
                },
                "dtype": "nifti"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2"
                },
                "dtype": "instance"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/img/img.nrrd",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2",
                    "mod": "img",
                    "file": "img.nrrd"
                },
                "dtype": "nrrd"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/seg/seg.nii.gz",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2",
                    "mod": "seg",
                    "file": "seg.nii.gz"
                },
                "dtype": "nifti"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/instance2/dicom",
                "meta": {
                    "sid": "instance2",
                    "ref": "instance2",
                    "mod": "dicom"
                },
                "dtype": "dicom"
            }
        ]

        # remove random ids in scan_results
        for i in range(len(scan_results)):
            scan_results[i]['meta'] = {k: v for k, v in scan_results[i]['meta'].items() if k not in ['id', '_instance']}

        # validate results
        self.assertEquals(scan_results, correct_import)

    def test_meta_extension_from_csv(self):

        # input / base directory
        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data"
        csv_file = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/utils/meta.csv"
        csv_file2 = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/utils/mod_meta.csv"
        self.assertTrue(os.path.isdir(base_dir))
        self.assertTrue(os.path.isfile(csv_file))
        self.assertTrue(os.path.isfile(csv_file2))

        # define structures
        structures = [
            "$sid@instance/$mod/",
            "$sid/seg/$file@nifti",
            "$sid/img/$file@nrrd"
        ]

        excludes = [
            "mixed",
            "imported_instances"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, excludes, verbose=True)

        # extend meta
        extend_meta_from_csv(scan_results=scan_results, csv_path=csv_file, id="sid")
        self.pretty_print_scan_results(scan_results)

        # extend on mod=img only
        extend_meta_from_csv(scan_results=scan_results, csv_path=csv_file2, id="mod")
        self.pretty_print_scan_results(scan_results)

        # lookup for added meta data 
        instance1_meta = {
            "patient": "patient1"   
        }

        instance2_meta = {
            "patient": "patient2",
            "link": " test"     
        }

        # check that meta was extended corectly in all scan results
        for sr in scan_results:
            sr_meta = sr["meta"]
            assert isinstance(sr_meta, dict)

            sr_meta_sid = sr_meta["sid"]

            if sr_meta_sid == "instance1":
                self.assertDictContainsSubset(instance1_meta, sr_meta)
            elif sr_meta_sid == "instance2":
                self.assertDictContainsSubset(instance2_meta, sr_meta)

    def test_import(self):

        # config file
        config_file = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/utils/config.yml"

        # instantiate config
        config = Config(config_file)
        config.debug = True

        # instantiate importer
        importer = FileStructureImporter(config)

        # clean input dir (if it exists)
        importer_instance_dir = importer.instance_dir #importer.getConfiguration('instances_dir', '')
        assert importer_instance_dir == "imported_instances"
        if len(importer_instance_dir) and os.path.isdir(os.path.join(config.data.abspath, importer_instance_dir)):
            shutil.rmtree(os.path.join(config.data.abspath, importer_instance_dir))

        # run import
        importer.execute()

        # check if import was successful (2 instances should be imported)
        instances = config.data.instances
        self.assertTrue(len(instances) == 2)

        # check if instance 1 was imported correctly (fetch data by auto generated meta)
        instance1 = [i for i in instances if i.attr['sid'] == "instance1"][0]
        data = instance1.data.filter(DataType(FileType.NRRD, Meta(mod="img"))).first()
        self.assertTrue(data is not None)

        data = instance1.data.filter(DataType(FileType.NIFTI, Meta(mod="seg"))).first()
        self.assertTrue(data is not None)

        # check if instance 2 was imported correctly (fetch data by auto generated meta)
        instance2 = [i for i in instances if i.attr['sid'] == "instance2"][0]
        data = instance2.data.filter(DataType(FileType.NRRD, Meta(mod="img"))).first()
        self.assertTrue(data is not None)

        data = instance2.data.filter(DataType(FileType.NIFTI, Meta(mod="seg"))).first()
        self.assertTrue(data is not None)

        data = instance2.data.filter(DataType(FileType.DICOM)).first()
        self.assertTrue(data is not None)

    def test_auto__WorkInProgress(self):
        # TODO: get dtype from file dite if auto is provided and update test accordingly

        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data"
        self.assertTrue(os.path.exists(base_dir))

        # define structures
        structures = [
            "mixed/$file@auto",
        ]

        # excludes
        excludes = [
            "instance1",
            "instance2",
            "mixed/regex_folder_id156723_modImage",
            "mixed/regex_folder_id156723_modUtils",
            "imported_instances"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, excludes, verbose=False)

        # pretty print results
        self.pretty_print_scan_results(scan_results)

        # expected results
        correct_import = [
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/mixed/img3.nrrd",
                "meta": {
                    "file": "img3.nrrd"
                },
                "dtype": "auto"
            },
            {
                "path": "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data/mixed/seg3.nii.gz",
                "meta": {
                    "file": "seg3.nii.gz"
                },
                "dtype": "auto"
            }
        ]

        # remove random ids in scan_results
        for i in range(len(scan_results)):
            scan_results[i]['meta'] = {k: v for k, v in scan_results[i]['meta'].items() if k != 'id'}

        # validate results
        self.assertEquals(scan_results, correct_import)

    def test_regex(self): 

        base_dir = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/data"
        self.assertTrue(os.path.exists(base_dir))

        # define structures
        structures = [
            r"mixed/re:(\w{3})(\d+).[\w\.]+::$mod::$nr@instance::@nrrd",
            r"mixed/re:\w+\.([\w\.]+)::$ext",
            r"mixed/re:regex_folder_id(\d+)_mod(\w+)::$id@instance::$mod/image.png@png"
        ]

        # excludes
        excludes = [
            "instance1",
            "instance2"
        ]

        # run scanner
        scan_results = scan_directory(base_dir, structures, excludes, verbose=True)

        # pretty print results
        self.pretty_print_scan_results(scan_results)

    def test_regex_import(self):
        # config file
        config_file = "/home/leonard/Projects/mhub/organization/mhubio/test/univimp/utils/config.yml"

        # instantiate config
        config = Config(config_file, config={
            'modules': {
                'FileStructureImporter': {
                    'input_dir': '',
                    'import_id': 'nr',
                    'structures': [
                        r"mixed/re:(\w{3})(\d+).[\w\.]+::img$mod::$nr@instance::@nrrd",
                        r"mixed/re:(\w{3})(\d+).[\w\.]+::seg$mod::$nr::@nifti",
                        r"mixed/re:\w+\.([\w\.]+)::$ext",
                        r"mixed/re:regex_folder_id(\d+)_mod(\w+)::$nr@instance::Image$type/image.png@txt"
                    ],
                    "excludes": [
                        "instance1",
                        "instance2"
                    ]
                },
                'NiftiConverter': {
                    'in_datas': 'nrrd:mod=img'
                }
            }
        })

        config.debug = True

        # instantiate importer
        importer = FileStructureImporter(config)

        # run import
        importer.execute()

        # convert
        # NOTE: conversion fails because image is empty file, buty log get's created at the created instance folder!
        converter = NiftiConverter(config)
        converter.execute()

if __name__ == '__main__':
    test = StructuralImporterTest()
    #test.test_regex()
    test.test_regex_import()