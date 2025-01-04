from dotenv import load_dotenv
import os 

load_dotenv('.gitignore/.env')

API_KEY = os.getenv('API_KEY')

print(API_KEY)