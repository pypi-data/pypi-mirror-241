from typing import Optional, List
import unittest, os

from mhubio.core import Meta, DataType, DataTypeQuery
from mhubio.core.RunnerOutput import ValueOutput, ClassOutput, OutputClass


class DataTypeQueryTest(unittest.TestCase):

    def test_tokenization(self):
        
        query = 'nrrd:mod=ct AND (dicom:mod=ct OR dicom:mod=mr)'
        tokens: List[str] = DataTypeQuery.tokenize(query)
        self.assertEqual(tokens[0], 'nrrd:mod=ct')
        self.assertEqual(tokens[1], 'AND')
        self.assertEqual(tokens[2], '(dicom:mod=ct OR dicom:mod=mr)')

        query = 'nrrd:mod=ct AND (dicom:mod=ct OR dicom:mod=mr) OR dicom:mod=mr'
        tokens: List[str] = DataTypeQuery.tokenize(query)
        self.assertEqual(tokens[0], 'nrrd:mod=ct')
        self.assertEqual(tokens[1], 'AND')
        self.assertEqual(tokens[2], '(dicom:mod=ct OR dicom:mod=mr)')
        self.assertEqual(tokens[3], 'OR')
        self.assertEqual(tokens[4], 'dicom:mod=mr')

        query = '(nrrd:mod=ct) AND ((dicom:mod=ct OR dicom:mod=mr) AND (dicom:mod=mr)) OR (dicom:mod=mr AND (nrrd:mod=ct))'
        tokens: List[str] = DataTypeQuery.tokenize(query)
        self.assertEqual(tokens[0], '(nrrd:mod=ct)')
        self.assertEqual(tokens[1], 'AND')
        self.assertEqual(tokens[2], '((dicom:mod=ct OR dicom:mod=mr) AND (dicom:mod=mr))')
        self.assertEqual(tokens[3], 'OR')
        self.assertEqual(tokens[4], '(dicom:mod=mr AND (nrrd:mod=ct))')

        query = 'nrrd:mod=ct AND (dicom:mod~=re(ge)x OR dicom:mod=mr)'
        tokens: List[str] = DataTypeQuery.tokenize(query)
        self.assertEqual(tokens[0], 'nrrd:mod=ct')
        self.assertEqual(tokens[1], 'AND')
        self.assertEqual(tokens[2], '(dicom:mod~=re(ge)x OR dicom:mod=mr)')

    def test_query_resolving(self):

        # dummy datatype. TODO: can we get rid of this?
        d = DataType.fromString('none')

        #
        self.assertTrue(DataTypeQuery.parse('TRUE AND (FALSE OR TRUE)', d))
        self.assertTrue(DataTypeQuery.parse('FALSE OR (TRUE OR TRUE)', d))
        self.assertTrue(DataTypeQuery.parse('TRUE AND TRUE AND TRUE', d))
        self.assertTrue(DataTypeQuery.parse('FALSE OR TRUE OR FALSE', d))

        self.assertFalse(DataTypeQuery.parse('FALSE AND (FALSE OR TRUE)', d))
        self.assertFalse(DataTypeQuery.parse('FALSE OR (FALSE OR FALSE)', d))
        self.assertFalse(DataTypeQuery.parse('TRUE AND FALSE AND TRUE', d))
        self.assertFalse(DataTypeQuery.parse('FALSE OR FALSE OR FALSE', d))

        self.assertTrue(DataTypeQuery.parse('TRUE AND (FALSE OR TRUE) OR TRUE', d))
        self.assertFalse(DataTypeQuery.parse('NOT (TRUE AND (FALSE OR TRUE) OR TRUE)', d))
        self.assertTrue(DataTypeQuery.parse('NOT FALSE AND (FALSE OR (NOT FALSE))', d))

        self.assertFalse(DataTypeQuery.parse('NOT (TRUE OR FALSE)', d))
        self.assertFalse(DataTypeQuery.parse('NOT TRUE AND NOT FALSE', d))
        #self.assertFalse(DataTypeQuery.parse('NOT(TRUE) AND NOT(FALSE)', d))

    def test_simple_parsing_and_query(self):
        query = 'dicom:roi=HEART AND (dicom:mod=ct OR dicom:mod=mr)'

        dtq: DataTypeQuery = DataTypeQuery(query)
        self.assertTrue(dtq.parse(query, DataType.fromString('dicom:mod=ct:roi=HEART')))
        self.assertTrue(dtq.parse(query, DataType.fromString('dicom:mod=mr:roi=HEART')))
        self.assertFalse(dtq.parse(query, DataType.fromString('dicom:mod=seg:roi=HEART')))
        self.assertFalse(dtq.parse(query, DataType.fromString('dicom:mod=mr:roi=LIVER')))
        self.assertFalse(dtq.parse(query, DataType.fromString('dicom:mod=mr')))

    def test_complex_datatype_parsing(self):

        query = 'dicom|nrrd'
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('dicom:mod=ct:roi=HEART')))
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('nrrd:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('nifti:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('none:mod=ct:roi=HEART')))
        
        query = 'dicom|nrrd:mod=ct'
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('dicom:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('dicom:mod=seg:roi=HEART')))
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('nrrd:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('nrrd:mod=seg:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('nifti:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('nifti:mod=seg:roi=HEART')))

        query = 'dicom|nrrd:mod=ct OR nifti:mod=seg'
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('dicom:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('dicom:mod=seg:roi=HEART')))
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('nrrd:mod=ct:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('nrrd:mod=seg:roi=HEART')))
        self.assertFalse(DataTypeQuery.parse(query, DataType.fromString('nifti:mod=ct:roi=HEART')))
        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('nifti:mod=seg:roi=HEART')))


    def test_meta_resolving_EQUAL(self):

        # string comparison
        self.assertTrue( DataTypeQuery.evaluateMeta('mod=ct', Meta(mod='ct')))

        # number comparison
        self.assertTrue( DataTypeQuery.evaluateMeta('v=5',   Meta(v='5')))
        self.assertTrue( DataTypeQuery.evaluateMeta('v=1.2', Meta(v='1.2')))
        self.assertFalse(DataTypeQuery.evaluateMeta('v=13',  Meta(v='8')))
        self.assertFalse(DataTypeQuery.evaluateMeta('v=0',   Meta(v='')))

        # list comparison
        self.assertTrue( DataTypeQuery.evaluateMeta('roi=a,b,c', Meta(roi='a,b,c')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi=a,b,c', Meta(roi='a,c,b')))

        # placeholder *
        self.assertTrue(DataTypeQuery.evaluateMeta('roi=*', Meta(roi='')))
        self.assertTrue(DataTypeQuery.evaluateMeta('roi=*', Meta(roi='HEART')))
        self.assertTrue(DataTypeQuery.evaluateMeta('roi=*', Meta(roi='HEART,LIVER')))

        # options A|B
        self.assertTrue( DataTypeQuery.evaluateMeta('roi=a|b|c', Meta(roi='a')))
        self.assertTrue( DataTypeQuery.evaluateMeta('roi=a|b|c', Meta(roi='b')))
        self.assertTrue( DataTypeQuery.evaluateMeta('roi=a|b|c', Meta(roi='c')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi=a|b|c', Meta(roi='a|b|c')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi=a|b|c', Meta(roi='d')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi=a|b|c', Meta(roi='')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi=a|b|c', Meta()))

    def test_meta_resolving_REGEX(self):
        self.assertTrue( DataTypeQuery.evaluateMeta('mod~=c.+', Meta(mod='ct')))
        self.assertTrue( DataTypeQuery.evaluateMeta('mod~=c.+', Meta(mod='ctc')))
        self.assertFalse(DataTypeQuery.evaluateMeta('mod~=c.+', Meta(mod='at')))
        self.assertFalse(DataTypeQuery.evaluateMeta('mod~=c.+', Meta(mod='c')))

    def test_meta_resolving_CONTAINS_ANY(self):
        self.assertTrue( DataTypeQuery.evaluateMeta('roi<=a,b,c', Meta(roi='a,b')))
        self.assertTrue( DataTypeQuery.evaluateMeta('roi<=a,b,c', Meta(roi='a,c,b')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi<=a,b,c', Meta(roi='')))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi<=a,b,c', Meta()))
        self.assertFalse(DataTypeQuery.evaluateMeta('roi<=a,b,c', Meta(roi='a,x')))

    def test_complex_meta_parsing(self):
        pass

    def test_complex_parsing(self):
        pass

    def test_complex_parsing_and_query(self):
        
        query = 'dicom|nrrd:mod=ct|mr:roi<=HEART,LIVER,LUNG OR dicom:mod=seg:roi=*'

        self.assertTrue(DataTypeQuery.parse(query, DataType.fromString('dicom:mod=ct:roi=HEART')))


class ValueOutputQueryTest(unittest.TestCase):

    # test setup
    def setUp(self):
        
        # create some outout data instances
        data1 = ValueOutput()
        data1.name = 'data1'
        data1.label = 'label1'
        data1.description = 'description1'
        data1.dtype = int
        data1.value = 10
        data1.meta = Meta(a="b", c="d")

        data2 = ValueOutput()
        data2.name = 'data2'
        data2.label = 'label2'
        data2.description = 'description2'
        data2.dtype = str
        data2.value = "hello"
        data2.meta = Meta(a="b", c="d")

        data3 = ValueOutput()
        data3.name = 'data3'
        data3.label = 'label3'
        data3.description = 'description3'
        data3.dtype = str
        data3.value = "world"
        data3.meta = Meta(a="b", c="d")

        # data4 = ClassOutput()
        # data4.name = 'data4'
        # data4.label = 'label4'
        # data4.description = 'description4'
        # data4.classes.append(OutputClass(0, "class0", "desc class 0"))
        # data4.classes.append(OutputClass(1, "class1", "desc class 1"))


        self.output_data_list = [data1, data2, data3]

    def test_query(self):
        
        query = 'data1|data3:a=b:.value>5'

        self.assertTrue(DataTypeQuery.parse(query, self.output_data_list[0]))
