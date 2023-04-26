
from tb_simple_api import api
from tb_simple_impl import SimpleArrayInterface

class TestSimpleArrayInterface:

    def test_func_bool(self):
        o = SimpleArrayInterface()
        o.func_bool(param_bool=[])

    def test_func_int(self):
        o = SimpleArrayInterface()
        o.func_int(param_int=[])

    def test_func_float(self):
        o = SimpleArrayInterface()
        o.func_float(param_float=[])

    def test_func_string(self):
        o = SimpleArrayInterface()
        o.func_string(param_string=[])

