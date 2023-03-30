from fastapi import Depends, FastAPI, Header, HTTPException

  
import tb.adv.http.routes  
import tb.conflict.http.routes  
import tb.data.http.routes  
import tb.enum.http.routes  
import tb.same.http.routes  
import tb.again.http.routes  
import tb.simple.http.routes

app = FastAPI()


app.include_router(
    router=tb.adv.http.routes.router,
    prefix="/tb.adv",
)

app.include_router(
    router=tb.conflict.http.routes.router,
    prefix="/tb.conflict",
)

app.include_router(
    router=tb.data.http.routes.router,
    prefix="/tb.data",
)

app.include_router(
    router=tb.enum.http.routes.router,
    prefix="/tb.enum",
)

app.include_router(
    router=tb.same.http.routes.router,
    prefix="/tb.same",
)

app.include_router(
    router=tb.again.http.routes.router,
    prefix="/tb.again",
)

app.include_router(
    router=tb.simple.http.routes.router,
    prefix="/tb.simple",
)
