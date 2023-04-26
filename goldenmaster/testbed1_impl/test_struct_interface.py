
from testbed1_api import api
from testbed1_impl import StructInterface

class TestStructInterface:

    def test_func_bool(self):
        o = StructInterface()
        o.func_bool(param_bool={})

    def test_func_int(self):
        o = StructInterface()
        o.func_int(param_int={})

    def test_func_float(self):
        o = StructInterface()
        o.func_float(param_float={})

    def test_func_string(self):
        o = StructInterface()
        o.func_string(param_string={})

