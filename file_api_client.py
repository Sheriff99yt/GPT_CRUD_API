import requests

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
    return response.status_code == 204  # Returns True if successfully deleted

# Example usage
if __name__ == '__main__':
    # Create a file
    print(create_file("example.txt", "This is an example content."))
    # Read all files
    print(read_files())
    # Update a file (replace '1' with a valid file ID)
    print(update_file(1, "updated_example.txt", "Updated content."))
    # Delete a file (replace '1' with a valid file ID)
    print(delete_file(1))
