
from tb_simple.api import api
from tb_simple.impl import VoidInterface

class TestVoidInterface:
    pass

    def test_func_void(self):
        o = VoidInterface()
        o.func_void()

    def test_sig_void(self):
        o = VoidInterface()
        self.called = False
        o.on_sig_void += lambda *args: setattr(self, 'called', True)
        o._sig_void()
        assert self.called == True
