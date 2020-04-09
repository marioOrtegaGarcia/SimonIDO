'''
    run.py is the entry point for our flask application
'''
from project import app
from project import create_tables

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080, debug=True)
