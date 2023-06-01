
from testbed1_api import api
from testbed1_impl import StructInterface

class TestStructInterface:

    def test_prop_bool(self):
        o = StructInterface()
        o.set_prop_bool({})
        assert o.get_prop_bool() == {}

    def test_prop_int(self):
        o = StructInterface()
        o.set_prop_int({})
        assert o.get_prop_int() == {}

    def test_prop_float(self):
        o = StructInterface()
        o.set_prop_float({})
        assert o.get_prop_float() == {}

    def test_prop_string(self):
        o = StructInterface()
        o.set_prop_string({})
        assert o.get_prop_string() == {}

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

