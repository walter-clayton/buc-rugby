from flask import render_template, Blueprint, request, redirect, url_for, flash, \
    Response
from resources import get_bucket

files = Blueprint('files', __name__)

@files.route("/files")
def file():
    my_bucket = get_bucket()
    summaries = my_bucket.objects.all()
    return render_template('files.html', my_bucket=my_bucket, files=summaries)

@files.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    my_bucket = get_bucket()
    my_bucket.Object(file.filename).put(Body=file)
    flash('File uploaded successfully')
    return redirect(url_for('files.file'))

@files.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']
    my_bucket = get_bucket()
    my_bucket.Object(key).delete()
    flash('File deleted successfully')
    return redirect(url_for('files.file'))


@files.route('/download', methods=['POST'])
def download():
    key = request.form['key']
    my_bucket = get_bucket()
    file_obj = my_bucket.Object(key).get()
    return Response(
        file_obj['Body'].read(),
        mimetype='text/plain',
        headers={"Content-Disposition": "attachment;filename={}".format(key)}
    )