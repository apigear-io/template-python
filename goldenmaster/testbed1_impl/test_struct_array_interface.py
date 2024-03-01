
from testbed1_api import api
from testbed1_impl import StructArrayInterface

class TestStructArrayInterface:

    def test_prop_bool(self):
        o = StructArrayInterface()
        o.set_prop_bool([])
        assert o.get_prop_bool() == []

    def test_prop_int(self):
        o = StructArrayInterface()
        o.set_prop_int([])
        assert o.get_prop_int() == []

    def test_prop_float(self):
        o = StructArrayInterface()
        o.set_prop_float([])
        assert o.get_prop_float() == []

    def test_prop_string(self):
        o = StructArrayInterface()
        o.set_prop_string([])
        assert o.get_prop_string() == []

    def test_func_bool(self):
        o = StructArrayInterface()
        o.func_bool(param_bool=[])

    def test_func_int(self):
        o = StructArrayInterface()
        o.func_int(param_int=[])

    def test_func_float(self):
        o = StructArrayInterface()
        o.func_float(param_float=[])

    def test_func_string(self):
        o = StructArrayInterface()
        o.func_string(param_string=[])

    def test_sig_bool(self):
        o = StructArrayInterface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool([])
        assert self.called == True

    def test_sig_int(self):
        o = StructArrayInterface()
        self.called = False
        o.on_sig_int += lambda *args: setattr(self, 'called', True)
        o._sig_int([])
        assert self.called == True

    def test_sig_float(self):
        o = StructArrayInterface()
        self.called = False
        o.on_sig_float += lambda *args: setattr(self, 'called', True)
        o._sig_float([])
        assert self.called == True

    def test_sig_string(self):
        o = StructArrayInterface()
        self.called = False
        o.on_sig_string += lambda *args: setattr(self, 'called', True)
        o._sig_string([])
        assert self.called == True
