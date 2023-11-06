from flask import Flask, request, send_file, make_response
import os

app = Flask(__name)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = 'uploaded_file.txt'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'

@app.route('/rename', methods=['GET'])
def rename_file():
    original_filename = 'uploaded_file.txt'
    new_filename = 'renamed_file.txt'

    os.rename(os.path.join(app.config['UPLOAD_FOLDER'], original_filename),
              os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

    return 'File renamed successfully'

@app.route('/download')
def download_file():
    filename = 'renamed_file.txt'
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    response = make_response(send_file(path, as_attachment=True, mimetype='application/octet-stream'))
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    return response

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
