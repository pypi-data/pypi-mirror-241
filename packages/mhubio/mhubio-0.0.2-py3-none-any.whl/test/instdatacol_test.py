import unittest

from mhubio.core import InstanceData, InstanceDataCollection, FileType, DataType, Meta, CT

class InstanceDataCollectionTest(unittest.TestCase):

    @classmethod
    def flatten(cls, c: InstanceDataCollection) -> str:
        return ''.join(sorted([d.dc.path for d in c.asList()]))

    def test_filter(self):

        # define some data
        d1 = InstanceData('a', DataType(FileType.DICOM, CT))
        d2 = InstanceData('b', DataType(FileType.DICOM, CT + {'flavour': 'sweet'}))
        d3 = InstanceData('c', DataType(FileType.NIFTI, CT))
        d4 = InstanceData('d', DataType(FileType.NIFTI, CT + {'flavour': 'sweet'}))
        d5 = InstanceData('e', DataType(FileType.NIFTI, Meta(mod='special')))
        d6 = InstanceData('f', DataType(FileType.NIFTI, Meta(mod='special', flavour='sweet')))
        d7 = InstanceData('g', DataType(FileType.NIFTI, Meta(mod='special', flavour='sour')))

        # instantiate collection
        c = InstanceDataCollection([d1, d2, d3, d4, d5, d6, d7])

        # filter by filetype, no meta
        s = c.filter(DataType(FileType.NIFTI))
        self.assertEquals(self.flatten(s), "cdefg")

        # filter by file type and meta
        s = c.filter(DataType(FileType.NIFTI, CT))
        self.assertEquals(self.flatten(s), "cd")

        # any filtetype (filter only by meta)
        s = c.filter(DataType(FileType.NONE, CT))
        self.assertEquals(self.flatten(s), "abcd")

        # filter by multiple meta fields
        s = c.filter(DataType(FileType.NONE, Meta(mod='special', flavour='sweet')))
        self.assertEquals(self.flatten(s), "f")

        # 
        s = c.filter([
            DataType(FileType.NONE, Meta(mod='special', flavour='sweet')),
            DataType(FileType.NONE, Meta(mod='special', flavour='sour'))
        ])
        self.assertEquals(self.flatten(s), "fg")

    def test_adding_data(self):
        
        # define some data
        d1 = InstanceData('a', DataType(FileType.DICOM, CT))
        d2 = InstanceData('b', DataType(FileType.DICOM, CT + {'flavour': 'sweet'}))
        d3 = InstanceData('c', DataType(FileType.NIFTI, CT))

        # instantiate collection
        c = InstanceDataCollection([d1, d2])

        # check data collection
        self.assertEquals(self.flatten(c), "ab")

        # add data
        c.add(d3)
        self.assertEquals(self.flatten(c), "abc")

        # add data again
        c.add(d3)
        c.add(d1)
        self.assertEquals(self.flatten(c), "abc")