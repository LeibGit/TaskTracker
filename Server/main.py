from fastapi import FastAPI

app = FastAPI()

task_list = []


@app.post("/")
async def create_tasks():

@app.get("/")
async def view_tasks():

@app.delete("/")
async def clear_tasks():

@app.put("/")
async def edit_tasks():