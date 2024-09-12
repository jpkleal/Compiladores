import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from compiler import compiler, TARGETS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'original_files'


def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() == 'isi')


@app.route("/",  methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        target = request.form['target']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('compile_to', lang=target, name=filename))

    targets = [f"\n<option value=\"{value}\">{value}</option>" for value in TARGETS]
    return f'''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data id="comp">
        <input type=file name=file>
        <input type=submit value=Upload>
    <label for="target">Choose target:</label>
        <select name="target" id="target" form="comp">{"".join(targets)}
    </select>
    </form>
    '''


@app.route('/<lang>/<name>')
def compile_to(lang, name):
    new_file = compiler(name, app.config['UPLOAD_FOLDER'], lang)
    return send_from_directory(app.config["UPLOAD_FOLDER"], new_file)


app.run(debug=True, host='0.0.0.0')
