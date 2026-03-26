from fastapi import FastAPI

# quick test scaffold
# TODO: Populate backend fully
app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}
