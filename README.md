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
   `.venv\Scripts\activate`
   # Mac:
   macOS/Linux: `source .venv/bin/activate`
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   unicorn main:app -reload
   ```

### API End points:

- `GET /`: Returns a "Hello World" message
