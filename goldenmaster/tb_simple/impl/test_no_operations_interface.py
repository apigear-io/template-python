
from tb_simple.api import api
from tb_simple.impl import NoOperationsInterface

class TestNoOperationsInterface:

    def test_prop_bool(self):
        o = NoOperationsInterface()
        self.called = False
        o.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_bool(False)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_bool() == False

    def test_prop_int(self):
        o = NoOperationsInterface()
        self.called = False
        o.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int(0)
        # should not be true since we are not changing the default value
        assert self.called == False
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
