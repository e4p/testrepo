import unittest
import evanptestmodule

class TestDatabase(unittest.TestCase):

    def test_run(self):
        evanptestmodule.run()

    def test_value(self):
        self.assertEqual(evanptestmodule.value(), 'the only value')
