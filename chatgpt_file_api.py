import os
import openai
import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import subprocess
import time

# Load API key from environment variable
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

BASE_URL = 'http://127.0.0.1:8000/api/files/'

def check_server_status():
    try:
        response = requests.get(BASE_URL)
        return response.status_code == 200
    except ConnectionError:
        return False

def run_django_server():
    try:
        subprocess.Popen(['python', 'manage.py', 'runserver'], shell=True)
        time.sleep(5)  # Wait a few seconds to give the server time to start
        return check_server_status()
    except Exception as e:
        return False

def create_file(name, content):
    response = requests.post(BASE_URL, json={'name': name, 'content': content})
    return response.json()

def save_error_to_file(error_message):
    filename = f"error_{int(time.time())}.txt"  # Unique filename
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, "w") as f:
        f.write(error_message)
    return file_path

def chatgpt_interaction(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except openai.error.RateLimitError:
        return "Error: You have exceeded your current quota. Please check your plan and billing details."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == '__main__':
    if not check_server_status():
        print("Django server is not running. Attempting to start the server...")
        if run_django_server():
            print("Django server started successfully.")
        else:
            print("Error: Failed to start Django server.")
            exit(1)

    user_input = input("Enter your command: ")
    gpt_response = chatgpt_interaction(user_input)

    print("ChatGPT Response:", gpt_response)

    # Check if the GPT response contains an error message
    if "Error" in gpt_response:
        # Save the error message to a file
        error_file_path = save_error_to_file(gpt_response)
        print(f"Error message saved to: {os.path.abspath(error_file_path)}")
    else:
        # Use the response to create a file
        suggested_filename = user_input.split(" ")[-1] + ".txt"  # Get filename from user command
        result = create_file(suggested_filename, gpt_response)
        print("File created:", result)
