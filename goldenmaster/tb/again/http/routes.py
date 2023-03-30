from fastapi import APIRouter



from tb.again import SameStruct1Interface
from tb.again import SameStruct2Interface
from tb.again import SameEnum1Interface
from tb.again import SameEnum2Interface

from . import shared

router = APIRouter()


same_struct_1_interface = SameStruct1Interface()
same_struct_2_interface = SameStruct2Interface()
same_enum_1_interface = SameEnum1Interface()
same_enum_2_interface = SameEnum2Interface()










