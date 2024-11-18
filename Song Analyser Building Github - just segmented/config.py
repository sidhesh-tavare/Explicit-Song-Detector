# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the Genius API key from the environment variables
apikey = os.getenv('GENIUS_API')
