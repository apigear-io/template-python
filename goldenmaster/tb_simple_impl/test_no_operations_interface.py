
from tb_simple_api import api
from tb_simple_impl import NoOperationsInterface

class TestNoOperationsInterface:

    def test_prop_bool(self):
        o = NoOperationsInterface()
        o.set_prop_bool(False)
        assert o.get_prop_bool() == False

    def test_prop_int(self):
        o = NoOperationsInterface()
        o.set_prop_int(0)
        assert o.get_prop_int() == 0
    pass

