from flask import Flask
import sys

app = Flask('demo')

@app.route('/')
def hello_world():
    return f'Hello, {app.config["PORT"]}!\n'

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    app.config['PORT'] = port  # Set the port in app config
    app.run(host='127.0.0.1', port=port)