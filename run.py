# run.py is the entry point for the application. It imports the app object from the app package and runs it.
from app import app

if __name__ == '__main__':
    app.run(debug=True)
