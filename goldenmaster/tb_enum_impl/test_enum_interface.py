
from tb_enum_api import api
from tb_enum_impl import EnumInterface

class TestEnumInterface:

    def test_func0(self):
        o = EnumInterface()
        o.func0(param0=api.Enum0.VALUE0)

    def test_func1(self):
        o = EnumInterface()
        o.func1(param1=api.Enum1.VALUE1)

    def test_func2(self):
        o = EnumInterface()
        o.func2(param2=api.Enum2.VALUE2)

    def test_func3(self):
        o = EnumInterface()
        o.func3(param3=api.Enum3.VALUE3)

