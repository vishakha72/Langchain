from dotenv import load_dotenv
import os

# #Loading enviornment variables from enviornment.env file
# load_dotenv()

# #Access to secret key
# secret_key = os.getenv('OPENAI_API_KEY')

# print("Success!")

load_dotenv(dotenv_path= 'PATH_TO_YOUR_ENV_FILE')
secret_key = os.getenv('OPENAI_API_KEY')

if secret_key:
    print("Success")
    print(secret_key)
else:
    print("Failed to connect to OPENAI server")  
