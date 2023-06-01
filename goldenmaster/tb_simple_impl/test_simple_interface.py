
from tb_simple_api import api
from tb_simple_impl import SimpleInterface

class TestSimpleInterface:

    def test_prop_bool(self):
        o = SimpleInterface()
        o.set_prop_bool(False)
        assert o.get_prop_bool() == False

    def test_prop_int(self):
        o = SimpleInterface()
        o.set_prop_int(0)
        assert o.get_prop_int() == 0

    def test_prop_float(self):
        o = SimpleInterface()
        o.set_prop_float(0.0)
        assert o.get_prop_float() == 0.0

    def test_prop_string(self):
        o = SimpleInterface()
        o.set_prop_string("")
        assert o.get_prop_string() == ""

    def test_func_bool(self):
        o = SimpleInterface()
        o.func_bool(param_bool=False)

    def test_func_int(self):
        o = SimpleInterface()
        o.func_int(param_int=0)

    def test_func_float(self):
        o = SimpleInterface()
        o.func_float(param_float=0.0)

    def test_func_string(self):
        o = SimpleInterface()
        o.func_string(param_string="")

