from fastapi import APIRouter



from testbed1 import StructInterface
from testbed1 import StructArrayInterface

from . import shared

router = APIRouter()


struct_interface = StructInterface()
struct_array_interface = StructArrayInterface()



@router.post(
    "/struct_interface/funcBool", 
    response_model=shared.StructInterfaceFuncBoolResponse
)
async def struct_interface_funcBool(params: shared.StructInterfaceFuncBoolRequest):
    result = struct_interface.funcBool(params.paramBool)
    state = shared.StructInterfaceState(
        propBool = struct_interface.propBool,
        propInt = struct_interface.propInt,
        propFloat = struct_interface.propFloat,
        propString = struct_interface.propString,
    )
    response = shared.StructInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/struct_interface/funcInt", 
    response_model=shared.StructInterfaceFuncIntResponse
)
async def struct_interface_funcInt(params: shared.StructInterfaceFuncIntRequest):
    result = struct_interface.funcInt(params.paramInt)
    state = shared.StructInterfaceState(
        propBool = struct_interface.propBool,
        propInt = struct_interface.propInt,
        propFloat = struct_interface.propFloat,
        propString = struct_interface.propString,
    )
    response = shared.StructInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/struct_interface/funcFloat", 
    response_model=shared.StructInterfaceFuncFloatResponse
)
async def struct_interface_funcFloat(params: shared.StructInterfaceFuncFloatRequest):
    result = struct_interface.funcFloat(params.paramFloat)
    state = shared.StructInterfaceState(
        propBool = struct_interface.propBool,
        propInt = struct_interface.propInt,
        propFloat = struct_interface.propFloat,
        propString = struct_interface.propString,
    )
    response = shared.StructInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/struct_interface/funcString", 
    response_model=shared.StructInterfaceFuncStringResponse
)
async def struct_interface_funcString(params: shared.StructInterfaceFuncStringRequest):
    result = struct_interface.funcString(params.paramString)
    state = shared.StructInterfaceState(
        propBool = struct_interface.propBool,
        propInt = struct_interface.propInt,
        propFloat = struct_interface.propFloat,
        propString = struct_interface.propString,
    )
    response = shared.StructInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/struct_array_interface/funcBool", 
    response_model=shared.StructArrayInterfaceFuncBoolResponse
)
async def struct_array_interface_funcBool(params: shared.StructArrayInterfaceFuncBoolRequest):
    result = struct_array_interface.funcBool(params.paramBool)
    state = shared.StructArrayInterfaceState(
        propBool = struct_array_interface.propBool,
        propInt = struct_array_interface.propInt,
        propFloat = struct_array_interface.propFloat,
        propString = struct_array_interface.propString,
    )
    response = shared.StructArrayInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/struct_array_interface/funcInt", 
    response_model=shared.StructArrayInterfaceFuncIntResponse
)
async def struct_array_interface_funcInt(params: shared.StructArrayInterfaceFuncIntRequest):
    result = struct_array_interface.funcInt(params.paramInt)
    state = shared.StructArrayInterfaceState(
        propBool = struct_array_interface.propBool,
        propInt = struct_array_interface.propInt,
        propFloat = struct_array_interface.propFloat,
        propString = struct_array_interface.propString,
    )
    response = shared.StructArrayInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/struct_array_interface/funcFloat", 
    response_model=shared.StructArrayInterfaceFuncFloatResponse
)
async def struct_array_interface_funcFloat(params: shared.StructArrayInterfaceFuncFloatRequest):
    result = struct_array_interface.funcFloat(params.paramFloat)
    state = shared.StructArrayInterfaceState(
        propBool = struct_array_interface.propBool,
        propInt = struct_array_interface.propInt,
        propFloat = struct_array_interface.propFloat,
        propString = struct_array_interface.propString,
    )
    response = shared.StructArrayInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/struct_array_interface/funcString", 
    response_model=shared.StructArrayInterfaceFuncStringResponse
)
async def struct_array_interface_funcString(params: shared.StructArrayInterfaceFuncStringRequest):
    result = struct_array_interface.funcString(params.paramString)
    state = shared.StructArrayInterfaceState(
        propBool = struct_array_interface.propBool,
        propInt = struct_array_interface.propInt,
        propFloat = struct_array_interface.propFloat,
        propString = struct_array_interface.propString,
    )
    response = shared.StructArrayInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response


