from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
from pydantic import Basemodel
from typing import Field,Optional
import pandas as pd 
import numpy as np 
import os 
import sys


load_dotenv()

model=ChatHuggingFace('prism-ml/Bonsai-8B-gguf')