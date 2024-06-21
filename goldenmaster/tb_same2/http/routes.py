from fastapi import APIRouter
from . import shared

router = APIRouter()


same_struct1_interface = shared.SameStruct1InterfaceState()
same_struct2_interface = shared.SameStruct2InterfaceState()
same_enum1_interface = shared.SameEnum1InterfaceState()
same_enum2_interface = shared.SameEnum2InterfaceState()



@router.post(
    "/tb_same2/same_struct1_interface/func1", 
    response_model=shared.SameStruct1InterfaceFunc1Response
)
async def same_struct1_interface_func1(params: shared.SameStruct1InterfaceFunc1Request):
    result = same_struct1_interface.func1(params.param1)
    state = shared.SameStruct1InterfaceState(
        prop1 = same_struct1_interface.prop1,
    )
    response = shared.SameStruct1InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response



@router.post(
    "/tb_same2/same_struct2_interface/func1", 
    response_model=shared.SameStruct2InterfaceFunc1Response
)
async def same_struct2_interface_func1(params: shared.SameStruct2InterfaceFunc1Request):
    result = same_struct2_interface.func1(params.param1)
    state = shared.SameStruct2InterfaceState(
        prop1 = same_struct2_interface.prop1,
        prop2 = same_struct2_interface.prop2,
    )
    response = shared.SameStruct2InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_same2/same_struct2_interface/func2", 
    response_model=shared.SameStruct2InterfaceFunc2Response
)
async def same_struct2_interface_func2(params: shared.SameStruct2InterfaceFunc2Request):
    result = same_struct2_interface.func2(params.param1, params.param2)
    state = shared.SameStruct2InterfaceState(
        prop1 = same_struct2_interface.prop1,
        prop2 = same_struct2_interface.prop2,
    )
    response = shared.SameStruct2InterfaceFunc2Response(
        result=result,
        state=state
    )
    return response



@router.post(
    "/tb_same2/same_enum1_interface/func1", 
    response_model=shared.SameEnum1InterfaceFunc1Response
)
async def same_enum1_interface_func1(params: shared.SameEnum1InterfaceFunc1Request):
    result = same_enum1_interface.func1(params.param1)
    state = shared.SameEnum1InterfaceState(
        prop1 = same_enum1_interface.prop1,
    )
    response = shared.SameEnum1InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response



@router.post(
    "/tb_same2/same_enum2_interface/func1", 
    response_model=shared.SameEnum2InterfaceFunc1Response
)
async def same_enum2_interface_func1(params: shared.SameEnum2InterfaceFunc1Request):
    result = same_enum2_interface.func1(params.param1)
    state = shared.SameEnum2InterfaceState(
        prop1 = same_enum2_interface.prop1,
        prop2 = same_enum2_interface.prop2,
    )
    response = shared.SameEnum2InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_same2/same_enum2_interface/func2", 
    response_model=shared.SameEnum2InterfaceFunc2Response
)
async def same_enum2_interface_func2(params: shared.SameEnum2InterfaceFunc2Request):
    result = same_enum2_interface.func2(params.param1, params.param2)
    state = shared.SameEnum2InterfaceState(
        prop1 = same_enum2_interface.prop1,
        prop2 = same_enum2_interface.prop2,
    )
    response = shared.SameEnum2InterfaceFunc2Response(
        result=result,
        state=state
    )
    return response


