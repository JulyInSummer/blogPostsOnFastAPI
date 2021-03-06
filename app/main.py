from fastapi import FastAPI
from routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# models.Base.metadata.create_all(bind=engine)

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def main_page():
    return {"message": "Read the documentation: https://july-posts-api.herokuapp.com/redoc"}
