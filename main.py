import os

from flask import Flask, send_file
from flask import Flask, jsonify, send_file
from database_connection import get_db_connection
from flask import request
from flask import redirect
app = Flask(__name__)


@app.route('/')
def index():
 return redirect('http://www.facebook.com')

def main():
    app.run(host='0.0.0.0', port=3000)

if __name__ == "__main__":
    main()

