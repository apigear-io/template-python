from fastapi import Depends, FastAPI, Header, HTTPException

  
import testbed2.http.routes  
import tb.enum.http.routes  
import tb.same1.http.routes  
import tb.same2.http.routes  
import tb.simple.http.routes  
import testbed1.http.routes  
import tb.empty.http.routes

app = FastAPI()


app.include_router(
    router=testbed2.http.routes.router,
    prefix="/testbed2",
)

app.include_router(
    router=tb.enum.http.routes.router,
    prefix="/tb.enum",
)

app.include_router(
    router=tb.same1.http.routes.router,
    prefix="/tb.same1",
)

app.include_router(
    router=tb.same2.http.routes.router,
    prefix="/tb.same2",
)

app.include_router(
    router=tb.simple.http.routes.router,
    prefix="/tb.simple",
)

app.include_router(
    router=testbed1.http.routes.router,
    prefix="/testbed1",
)

app.include_router(
    router=tb.empty.http.routes.router,
    prefix="/tb.empty",
)
