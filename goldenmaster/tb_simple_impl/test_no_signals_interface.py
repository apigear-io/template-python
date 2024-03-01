
from tb_simple_api import api
from tb_simple_impl import NoSignalsInterface

class TestNoSignalsInterface:

    def test_prop_bool(self):
        o = NoSignalsInterface()
        o.set_prop_bool(False)
        assert o.get_prop_bool() == False

    def test_prop_int(self):
        o = NoSignalsInterface()
        o.set_prop_int(0)
        assert o.get_prop_int() == 0

    def test_func_void(self):
        o = NoSignalsInterface()
        o.func_void()

    def test_func_bool(self):
        o = NoSignalsInterface()
        o.func_bool(param_bool=False)
    pass
