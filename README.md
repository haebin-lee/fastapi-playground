# FastAPI Project

This is a simple FastAPI project to demonstrate basic API functionality

## Setup

1. Clone the repository

2. Create a virtual environment

   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   ```python
   # Windows:
   .venv\Scripts\activate
   # Mac/Linux:
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python3 main.py
   ```

### API End points:

- `GET /`: Returns a "Hello World" message
- `GET /api/users`: Returns user list
- `GET /api/users/{uuid}`: Returns a user
- `POST /api/users`: Adds a user
- `PUT /api/users/{uuid}`: Updates a user
  ```
  {
   "name": "name",
   "email": "email",
  }
  ```
- `DELETE /api/users{uuid}`: Deletes a user
