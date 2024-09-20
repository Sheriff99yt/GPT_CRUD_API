import os
import openai
import requests

# Load API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

BASE_URL = 'http://127.0.0.1:8000/api/files/'

def create_file(name, content):
    response = requests.post(BASE_URL, json={'name': name, 'content': content})
    return response.json()

def read_files():
    response = requests.get(BASE_URL)
    return response.json()

def update_file(file_id, name, content):
    response = requests.put(f'{BASE_URL}{file_id}/', json={'name': name, 'content': content})
    return response.json()

def delete_file(file_id):
    response = requests.delete(f'{BASE_URL}{file_id}/')
    return response.status_code == 204

def chatgpt_interaction(prompt):
    response = openai.completions.create(
        model="gpt-3.5-turbo",  # or another model you prefer
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == '__main__':
    user_input = "Create a file named 'example.txt' with content 'Hello World'."
    gpt_response = chatgpt_interaction(user_input)

    # Print the ChatGPT response
    print("ChatGPT Response:", gpt_response)

    # Implement parsing logic to handle the response and call the appropriate file function
