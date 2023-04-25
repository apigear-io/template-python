from fastapi import Depends, FastAPI, Header, HTTPException

  
import demo.http.routes

app = FastAPI()


app.include_router(
    router=demo.http.routes.router,
    prefix="/demo",
)
