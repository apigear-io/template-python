
from tb_names.api import api
from tb_names.impl import NamEs

class TestNamEs:

    def test_switch(self):
        o = NamEs()
        self.called = False
        o.on_switch_changed += lambda *args: setattr(self, 'called', True)
        o.set_switch(False)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_switch() == False

    def test_some_property(self):
        o = NamEs()
        self.called = False
        o.on_some_property_changed += lambda *args: setattr(self, 'called', True)
        o.set_some_property(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_some_property() == 0

    def test_some_poperty2(self):
        o = NamEs()
        self.called = False
        o.on_some_poperty2_changed += lambda *args: setattr(self, 'called', True)
        o.set_some_poperty2(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_some_poperty2() == 0

    def test_some_function(self):
        o = NamEs()
        o.some_function(some_param=False)

    def test_some_function2(self):
        o = NamEs()
        o.some_function2(some_param=False)

    def test_some_signal(self):
        o = NamEs()
        self.called = False
        o.on_some_signal += lambda *args: setattr(self, 'called', True)
        o._some_signal(False)
        assert self.called == True

    def test_some_signal2(self):
        o = NamEs()
        self.called = False
        o.on_some_signal2 += lambda *args: setattr(self, 'called', True)
        o._some_signal2(False)
        assert self.called == True
