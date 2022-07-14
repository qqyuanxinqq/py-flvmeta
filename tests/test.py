import unittest
import os.path

from pyflvmeta import flvmeta, flvmeta_dump,flvmeta_check, flvmeta_update

path = os.path.dirname(os.path.relpath(__file__))
video = os.path.join(path, "sample.flv")

def compare(a,b):
    assert a == b, "Actual: {a} \nversus\n Expected: {b}".format(a=a,b=b)

class TestFlvmeta(unittest.TestCase):
    def test_flvmeta_noopt(self):
        expected = (0,DUMPED)
        actually = flvmeta(video)
        compare(actually[0],expected[0])
        compare(actually[1][0:10],expected[1][0:10])

    def test_flvmeta_dump_noopt(self):
        expected = (0,DUMPED)
        actually = flvmeta_dump(video)
        compare(actually[0],expected[0])
        compare(actually[1][0:10],expected[1][0:10])
        
    def test_flvmeta_dump_json(self):
        expected = (0,DUMPED_JSON)
        actually = flvmeta_dump(video, "-j")
        compare(actually[0],expected[0])
        compare(actually[1][0:10],expected[1][0:10])

    def test_flvmeta_check_noopt(self):
        expected = (0,CHECKED)
        actually = flvmeta_check(video)
        compare(actually,expected)
    def test_flvmeta_update_noopt(self):
        expected = (0,'')
        actually = flvmeta_update(video)
        compare(actually,expected)

    def test_flvmeta_version(self):
        expected = (0,VERSION)
        actually = flvmeta("", "-V")
        compare(actually[0],expected[0])
        compare(actually[1][0:5],expected[1][0:5])

if __name__ == "__main__":
    unittest.main()

CHECKED = '0 error(s), 0 warning(s)\n'
DUMPED = '<?xml version="1.0"'
DUMPED_JSON = '{"hasMetadata"'
VERSION = "flvmeta"
