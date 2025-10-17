# Week 12 - Activity 1:  Flask
# Develop a simple web app as follows

from flask import Flask

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><p>Welcome to your first Flask application!</p>'

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100) 
 