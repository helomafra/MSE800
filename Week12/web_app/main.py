# Week 12 - Activity 2 - Develop an initial Web APP
 
# Develop a Web Application to have Hyper link and load an image (from end user input) using Flask.

from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5101) 