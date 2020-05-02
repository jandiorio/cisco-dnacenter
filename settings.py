from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DNA_CENTER_USERNAME"))
print(os.getenv("DNA_CENTER_PASSWORD"))