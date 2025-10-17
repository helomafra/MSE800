# Week 12 - Activity 2 - Develop an initial Web APP
 
# Develop a Web Application to have Hyper link and load an image (from end user input) using Flask.

from flask import Flask, render_template, request, redirect, url_for
import os
import time

# Create Flask application instance
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
   # Check if the uploaded file has an allowed extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html', uploaded_image=None, show_error=False)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', uploaded_image=None, show_error=True)
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', uploaded_image=None, show_error=True)
    
    if file and allowed_file(file.filename):
        # Get file extension
        file_ext = file.filename.rsplit('.', 1)[1].lower()

        filename = f"upload_{int(time.time())}.{file_ext}"
        
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        return render_template('index.html', uploaded_image=filename, show_error=False)
    else:
        return render_template('index.html', uploaded_image=None, show_error=True)

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5101) 