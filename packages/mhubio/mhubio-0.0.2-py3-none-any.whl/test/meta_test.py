import unittest

from mhubio.core import Meta


class MetaTest(unittest.TestCase):

    def test_operators(self):

        # assertions
        m1 = Meta(a="b")
        m2 = Meta() + {"a": "b"}
        m3 = Meta().ext({"a": "b"})
        m4 = Meta().ext([m1, m2])
        assert m1 == m2 and m2 == m3 and m3 == m4
        self.assertEquals(m1, m2)
        self.assertEquals(m1, m3)
        self.assertEquals(m1, m4)

        m1 += {"c": "d"}
        m5 = m1 + {"c": "d"}
        self.assertEquals(m1, m5)

        m6 = Meta()
        m6.mdict = {'a': 'b', 'c': 'd', 'e': 'f'}

        assert m6 <= m1
        assert not m1 <= m6
        assert m1 <= m6 - ['e', 'c']
        assert not m6 - ['e', 'c'] <= m1
        assert not m1 <= m6 - ['c']
        assert not m1 == m6
        assert m1 == m6 - ['e']
        assert m6['c'] == 'd'
        assert (m6 - ['e'])['a'] == 'b'
        assert 'a' in m1
        assert not 'e' in m1 

        # some examples
        m1 = Meta().ext({"a": "b", "c": "d"})

        print("m1                                       ", m1)
        print("m1 == m1                                 ", m1 == m1)
        print("m1 == m1 + {'e': 'f'}                    ", m1 == m1 + {'e': 'f'})
        print("m1 == {'a': 'b', 'c': 'd'}               ", m1 == {'a': 'b', 'c': 'd'})
        print("Meta() == {}                             ", Meta() == {})
        print("m1 <= m1                                 ", m1 <= m1)
        print("m1 <= m1 + {'e': 'f'}                    ", m1 <= m1 + {'e': 'f'})
        print("m1 - ['a']                               ", m1 - ['a'])
        print("m1 - ['a'] <= m1                         ", m1 - ['a'] <= m1)
        print("m1 <= m1 - ['a']                         ", m1 <= m1 - ['a'])

    def test_placeholders(self):
        m1 = Meta(**{'k1': 'foo', 'k2': 'hello'})
        m2 = Meta(**{'k1': 'foo', 'k2': 'world'})

        q1 = Meta(**{'k1': 'foo', 'k2': '*'})
        q2 = Meta(**{'k1': 'foo', 'k2': 'world'})

        self.assertFalse(m1 == q1)
        self.assertFalse(m2 == q1)
        self.assertTrue(m1 <= q1)
        self.assertTrue(m2 <= q1)
        self.assertFalse(m1 <= q2)
        self.assertTrue(m2 <= q2)