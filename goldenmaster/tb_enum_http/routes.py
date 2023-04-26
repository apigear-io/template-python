from fastapi import APIRouter



from tb.enum import EnumInterface

from . import shared

router = APIRouter()


enum_interface = EnumInterface()



@router.post(
    "/enum_interface/func0", 
    response_model=shared.EnumInterfaceFunc0Response
)
async def enum_interface_func0(params: shared.EnumInterfaceFunc0Request):
    result = enum_interface.func0(params.param0)
    state = shared.EnumInterfaceState(
        prop0 = enum_interface.prop0,
        prop1 = enum_interface.prop1,
        prop2 = enum_interface.prop2,
        prop3 = enum_interface.prop3,
    )
    response = shared.EnumInterfaceFunc0Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/enum_interface/func1", 
    response_model=shared.EnumInterfaceFunc1Response
)
async def enum_interface_func1(params: shared.EnumInterfaceFunc1Request):
    result = enum_interface.func1(params.param1)
    state = shared.EnumInterfaceState(
        prop0 = enum_interface.prop0,
        prop1 = enum_interface.prop1,
        prop2 = enum_interface.prop2,
        prop3 = enum_interface.prop3,
    )
    response = shared.EnumInterfaceFunc1Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/enum_interface/func2", 
    response_model=shared.EnumInterfaceFunc2Response
)
async def enum_interface_func2(params: shared.EnumInterfaceFunc2Request):
    result = enum_interface.func2(params.param2)
    state = shared.EnumInterfaceState(
        prop0 = enum_interface.prop0,
        prop1 = enum_interface.prop1,
        prop2 = enum_interface.prop2,
        prop3 = enum_interface.prop3,
    )
    response = shared.EnumInterfaceFunc2Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/enum_interface/func3", 
    response_model=shared.EnumInterfaceFunc3Response
)
async def enum_interface_func3(params: shared.EnumInterfaceFunc3Request):
    result = enum_interface.func3(params.param3)
    state = shared.EnumInterfaceState(
        prop0 = enum_interface.prop0,
        prop1 = enum_interface.prop1,
        prop2 = enum_interface.prop2,
        prop3 = enum_interface.prop3,
    )
    response = shared.EnumInterfaceFunc3Response(
        result=result,
        state=state
    )
    return response


