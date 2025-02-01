from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def read_root():
    return {"mensagem": "Olá mundo"}


# if __name__ == "__main__":
#     read_root()
