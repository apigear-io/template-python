from fastapi import APIRouter
from org_objectapi_testbed.interface1 import Interface1
from org_objectapi_testbed.interface2 import Interface2

from . import shared

router = APIRouter()
interface1 = Interface1()
interface2 = Interface2()


@router.post(
    "/Interface1/op1", 
    response_model=shared.Interface1Op1Response
)
async def interface1_op1(params: shared.Interface1Op1Request):
    result = interface1.op1()
    state = shared.Interface1State(
        prop1=interface1.prop1,
        prop2=interface1.prop2,
        prop3=interface1.prop3,
        prop4=interface1.prop4,
        prop5=interface1.prop5,
        prop6=interface1.prop6,
        prop7=interface1.prop7,
        prop10=interface1.prop10,
        prop11=interface1.prop11,
        prop12=interface1.prop12,
        prop14=interface1.prop14 
    )
    response = shared.Interface1Op1Response(
        state=state
    )
    return response


@router.post(
    "/Interface1/op2", 
    response_model=shared.Interface1Op2Response
)
async def interface1_op2(params: shared.Interface1Op2Request):
    result = interface1.op2(params.step)
    state = shared.Interface1State(
        prop1=interface1.prop1,
        prop2=interface1.prop2,
        prop3=interface1.prop3,
        prop4=interface1.prop4,
        prop5=interface1.prop5,
        prop6=interface1.prop6,
        prop7=interface1.prop7,
        prop10=interface1.prop10,
        prop11=interface1.prop11,
        prop12=interface1.prop12,
        prop14=interface1.prop14 
    )
    response = shared.Interface1Op2Response(
        state=state
    )
    return response


@router.post(
    "/Interface1/op3", 
    response_model=shared.Interface1Op3Response
)
async def interface1_op3(params: shared.Interface1Op3Request):
    result = interface1.op3()
    state = shared.Interface1State(
        prop1=interface1.prop1,
        prop2=interface1.prop2,
        prop3=interface1.prop3,
        prop4=interface1.prop4,
        prop5=interface1.prop5,
        prop6=interface1.prop6,
        prop7=interface1.prop7,
        prop10=interface1.prop10,
        prop11=interface1.prop11,
        prop12=interface1.prop12,
        prop14=interface1.prop14 
    )
    response = shared.Interface1Op3Response(
        result=result,
        state=state
    )
    return response
