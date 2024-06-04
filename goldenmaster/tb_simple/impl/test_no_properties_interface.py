
from tb_simple.api import api
from tb_simple.impl import NoPropertiesInterface

class TestNoPropertiesInterface:
    pass

    def test_func_void(self):
        o = NoPropertiesInterface()
        o.func_void()

    def test_func_bool(self):
        o = NoPropertiesInterface()
        o.func_bool(param_bool=False)

    def test_sig_void(self):
        o = NoPropertiesInterface()
        self.called = False
        o.on_sig_void += lambda *args: setattr(self, 'called', True)
        o._sig_void()
        assert self.called == True

    def test_sig_bool(self):
        o = NoPropertiesInterface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool(False)
        assert self.called == True
