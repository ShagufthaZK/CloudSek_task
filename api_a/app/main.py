from fastapi import FastAPI
import random
app = FastAPI()


@app.get("/get_rand_num")
async def random_number():
    n = int(random.random()*100000)
    return {"rand_num": n}

