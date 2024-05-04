from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! This is my example Flask app deployed on Minikube using GitHub Actions.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
