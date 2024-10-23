from fastapi import FastAPI
from src.api.allbets.router import router as allbets_router
from src.api.bets.router import router as bets_router




app = FastAPI(
    title="BetsAPI"
)

app.include_router(allbets_router)
app.include_router(bets_router)


