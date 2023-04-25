from fastapi import APIRouter



from demo import Counter

from . import shared

router = APIRouter()


counter = Counter()



@router.post(
    "/counter/increment", 
    response_model=shared.CounterIncrementResponse
)
async def counter_increment(params: shared.CounterIncrementRequest):
    result = counter.increment()
    state = shared.CounterState(
        value = counter.value,
    )
    response = shared.CounterIncrementResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/counter/decrement", 
    response_model=shared.CounterDecrementResponse
)
async def counter_decrement(params: shared.CounterDecrementRequest):
    result = counter.decrement()
    state = shared.CounterState(
        value = counter.value,
    )
    response = shared.CounterDecrementResponse(
        result=result,
        state=state
    )
    return response


