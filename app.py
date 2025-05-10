from flask import Flask, request, jsonify, render_template, send_from_directory
from inference_sdk import InferenceHTTPClient
import os
import concurrent.futures
import csv

app = Flask(__name__)

CLIENT = InferenceHTTPClient(
    api_url="https://classify.roboflow.com",
    api_key="aMJexj0YEBqvfPRoKw1I",
    #client_mode="v1"  # Ensure the client is in the correct mode
)

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Store upload history
upload_history = []
# Load the model during startup
model_id = "deepfake-detection-using-yolo/1"
#model_loaded = CLIENT.load_model(model_id)

def perform_detection(file_path):
    result = CLIENT.infer(file_path, model_id=model_id)
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Perform detection asynchronously
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(perform_detection, file_path)
            result = future.result()

        upload_history.append({'filename': file.filename, 'result': result['top']})
        return jsonify({'top': result['top'], 'filename': file.filename})

@app.route('/history')
def history():
    return render_template('history.html', upload_history=upload_history)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save feedback to CSV file
        feedback_file = 'feedback.csv'
        feedback_exists = os.path.isfile(feedback_file)
        with open(feedback_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not feedback_exists:
                writer.writerow(['Name', 'Email', 'Message'])
            writer.writerow([name, email, message])

        return jsonify({'status': 'success'})
    return render_template('feedback.html')

@app.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html')

if __name__== '__main__':
    app.run(debug=True)