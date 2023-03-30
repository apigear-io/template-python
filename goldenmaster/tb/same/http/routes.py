from fastapi import APIRouter



from tb.same import SameStruct1Interface
from tb.same import SameStruct2Interface
from tb.same import SameEnum1Interface
from tb.same import SameEnum2Interface

from . import shared

router = APIRouter()


same_struct_1_interface = SameStruct1Interface()
same_struct_2_interface = SameStruct2Interface()
same_enum_1_interface = SameEnum1Interface()
same_enum_2_interface = SameEnum2Interface()










