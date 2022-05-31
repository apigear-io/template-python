from fastapi import Depends, FastAPI, Header, HTTPException  
import org_objectapi_testbed.http.routes

app = FastAPI()  
app.include_router(
    router=org_objectapi_testbed.http.routes.router,
    prefix="/org.objectapi.testbed"
)
