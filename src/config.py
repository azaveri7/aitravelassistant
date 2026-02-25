# OpenAI API key (set this if using OpenAI)
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_HOST = "https://b9705c99-b3aa-44e1-a2d4-139c707286c6.us-east4-0.gcp.cloud.qdrant.io"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.1qGPKkojrSraTekyV6BYBV9rxEPPVzKL2rC19JymyPY"
COLLECTION_NAME = "travel_assistant"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model provider: 'huggingface' or 'openai'
MODEL_PROVIDER = "openai"  # Change to 'openai' to use OpenAI
FASTAPI_URL = "http://localhost:8000"