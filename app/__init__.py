import os
from flask import Flask
from flask import request

app=Flask(__name__)
from app import views
