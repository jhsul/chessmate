from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from redis import Redis

from config import Config
from models import INITIAL_GAME_STATE

app = FastAPI()


# @app.get("/", response_class=PlainTextResponse)
@app.get("/")
async def root():
    # return str(INITIAL_GAME_STATE)
    return INITIAL_GAME_STATE


@app.post("/games")
async def create_game():
    redis_client = Redis(Config.REDIS_HOST)
    redis_client
    return ...


@app.get("/games")
async def get_games():
    """
    Return all users the
    """
    return ...


@app.get("/games/{game_id}")
async def get_game_state(game_id: str):
    """
    Returns the game state of a given game id
    """
    return INITIAL_GAME_STATE
