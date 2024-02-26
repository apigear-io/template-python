
from tb_simple_api import api
from tb_simple_impl import NoPropertiesInterface

class TestNoPropertiesInterface:
    pass

    def test_func_void(self):
        o = NoPropertiesInterface()
        o.func_void()

    def test_func_bool(self):
        o = NoPropertiesInterface()
        o.func_bool(param_bool=False)

