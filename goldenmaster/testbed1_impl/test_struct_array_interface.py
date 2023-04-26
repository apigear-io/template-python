
from testbed1_api import api
from testbed1_impl import StructArrayInterface

class TestStructArrayInterface:

    def test_func_bool(self):
        o = StructArrayInterface()
        o.func_bool(param_bool=[])

    def test_func_int(self):
        o = StructArrayInterface()
        o.func_int(param_int=[])

    def test_func_float(self):
        o = StructArrayInterface()
        o.func_float(param_float=[])

    def test_func_string(self):
        o = StructArrayInterface()
        o.func_string(param_string=[])

