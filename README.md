
---

# GPT CRUD API

A simple API project that interacts with OpenAI's ChatGPT model to create, read, update, and delete files. This project utilizes Django for the backend and OpenAI's API for generating content based on user input.

## Features

- **Create Files**: Store text content based on user prompts.
- **Read Files**: Retrieve a list of stored files.
- **Update Files**: Modify existing files with new content.
- **Delete Files**: Remove files from the database.
- **OpenAI Integration**: Generate content using the GPT-3.5-turbo model.

## Requirements

- Python 3.x
- Django
- OpenAI Python library
- Requests library
- Python-dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd GPT_CRUD_API
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # For Windows
   source .venv/bin/activate  # For macOS/Linux
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the application:

```bash
python chatgpt_file_api.py
```

When prompted, enter your command to interact with the API.

## Error Handling

The application handles various errors that may occur during API interactions, including:

- Rate limit errors
- API connection errors
- General exceptions

## Contributing

Feel free to submit pull requests or open issues if you have suggestions or improvements.

## License

This project is licensed under the MIT License.

---

