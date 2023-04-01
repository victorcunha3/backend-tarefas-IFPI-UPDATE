from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.controller import tarefa_controller
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

origins = ['http://localhost:5500',"http://127.0.0.1:5500"
           'https://main--glittering-druid-b1e982.netlify.app/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarefa_controller.routes,
                   prefix=tarefa_controller.prefix)