
from tb_enum_api import api
from tb_enum_impl import EnumInterface

class TestEnumInterface:

    def test_func0(self):
        o = EnumInterface()
        o.func0(api.Enum0.value0,)

    def test_func1(self):
        o = EnumInterface()
        o.func1(api.Enum1.value1,)

    def test_func2(self):
        o = EnumInterface()
        o.func2(api.Enum2.value2,)

    def test_func3(self):
        o = EnumInterface()
        o.func3(api.Enum3.value3,)

