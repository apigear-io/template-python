from fastapi import APIRouter



from tb.simple import SimpleInterface
from tb.simple import SimpleArrayInterface

from . import shared

router = APIRouter()


simple_interface = SimpleInterface()
simple_array_interface = SimpleArrayInterface()



@router.post(
    "/simple_interface/funcBool", 
    response_model=shared.SimpleInterfaceFuncBoolResponse
)
async def simple_interface_funcBool(params: shared.SimpleInterfaceFuncBoolRequest):
    result = simple_interface.funcBool(params.paramBool)
    state = shared.SimpleInterfaceState(
        propBool = simple_interface.propBool,
        propInt = simple_interface.propInt,
        propFloat = simple_interface.propFloat,
        propString = simple_interface.propString,
    )
    response = shared.SimpleInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/simple_interface/funcInt", 
    response_model=shared.SimpleInterfaceFuncIntResponse
)
async def simple_interface_funcInt(params: shared.SimpleInterfaceFuncIntRequest):
    result = simple_interface.funcInt(params.paramInt)
    state = shared.SimpleInterfaceState(
        propBool = simple_interface.propBool,
        propInt = simple_interface.propInt,
        propFloat = simple_interface.propFloat,
        propString = simple_interface.propString,
    )
    response = shared.SimpleInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/simple_interface/funcFloat", 
    response_model=shared.SimpleInterfaceFuncFloatResponse
)
async def simple_interface_funcFloat(params: shared.SimpleInterfaceFuncFloatRequest):
    result = simple_interface.funcFloat(params.paramFloat)
    state = shared.SimpleInterfaceState(
        propBool = simple_interface.propBool,
        propInt = simple_interface.propInt,
        propFloat = simple_interface.propFloat,
        propString = simple_interface.propString,
    )
    response = shared.SimpleInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/simple_interface/funcString", 
    response_model=shared.SimpleInterfaceFuncStringResponse
)
async def simple_interface_funcString(params: shared.SimpleInterfaceFuncStringRequest):
    result = simple_interface.funcString(params.paramString)
    state = shared.SimpleInterfaceState(
        propBool = simple_interface.propBool,
        propInt = simple_interface.propInt,
        propFloat = simple_interface.propFloat,
        propString = simple_interface.propString,
    )
    response = shared.SimpleInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/simple_array_interface/funcBool", 
    response_model=shared.SimpleArrayInterfaceFuncBoolResponse
)
async def simple_array_interface_funcBool(params: shared.SimpleArrayInterfaceFuncBoolRequest):
    result = simple_array_interface.funcBool(params.paramBool)
    state = shared.SimpleArrayInterfaceState(
        propBool = simple_array_interface.propBool,
        propInt = simple_array_interface.propInt,
        propFloat = simple_array_interface.propFloat,
        propString = simple_array_interface.propString,
    )
    response = shared.SimpleArrayInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/simple_array_interface/funcInt", 
    response_model=shared.SimpleArrayInterfaceFuncIntResponse
)
async def simple_array_interface_funcInt(params: shared.SimpleArrayInterfaceFuncIntRequest):
    result = simple_array_interface.funcInt(params.paramInt)
    state = shared.SimpleArrayInterfaceState(
        propBool = simple_array_interface.propBool,
        propInt = simple_array_interface.propInt,
        propFloat = simple_array_interface.propFloat,
        propString = simple_array_interface.propString,
    )
    response = shared.SimpleArrayInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/simple_array_interface/funcFloat", 
    response_model=shared.SimpleArrayInterfaceFuncFloatResponse
)
async def simple_array_interface_funcFloat(params: shared.SimpleArrayInterfaceFuncFloatRequest):
    result = simple_array_interface.funcFloat(params.paramFloat)
    state = shared.SimpleArrayInterfaceState(
        propBool = simple_array_interface.propBool,
        propInt = simple_array_interface.propInt,
        propFloat = simple_array_interface.propFloat,
        propString = simple_array_interface.propString,
    )
    response = shared.SimpleArrayInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/simple_array_interface/funcString", 
    response_model=shared.SimpleArrayInterfaceFuncStringResponse
)
async def simple_array_interface_funcString(params: shared.SimpleArrayInterfaceFuncStringRequest):
    result = simple_array_interface.funcString(params.paramString)
    state = shared.SimpleArrayInterfaceState(
        propBool = simple_array_interface.propBool,
        propInt = simple_array_interface.propInt,
        propFloat = simple_array_interface.propFloat,
        propString = simple_array_interface.propString,
    )
    response = shared.SimpleArrayInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response


