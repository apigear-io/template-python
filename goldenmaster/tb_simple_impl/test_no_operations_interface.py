
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

    def test_sig_void(self):
        o = NoOperationsInterface()
        self.called = False
        o.on_sig_void += lambda *args: setattr(self, 'called', True)
        o._sig_void()
        assert self.called == True

    def test_sig_bool(self):
        o = NoOperationsInterface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool(False)
        assert self.called == True
