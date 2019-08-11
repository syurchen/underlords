import os
from flask import Flask, render_template, flash, request, redirect, url_for,\
    abort, send_from_directory, jsonify
from werkzeug.utils import secure_filename 

from app import app
from Classes.Methods import queueImg, checkQueue, storeResults, getResultsByNewImg
from Classes.Utils import Utils

def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'bmp']

@app.route('/underlords', methods=['GET', 'POST'])
@app.route('/underlords/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            oldFilename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], oldFilename))
            processedFilename = Utils.createNewRandomFilename(oldFilename)
            queueImg(oldFilename, processedFilename)
            return redirect(url_for('show_result', filename = processedFilename))

    return render_template('upload.html')

@app.route('/underlords/result/<filename>')
def show_result(filename):
    oldFilename, processedFilename, rollData = getResultsByNewImg(filename)
    if not oldFilename:
        abort(404)
    if not rollData:
        # the image isn't processed. Getting place in queue
        queuePlace = checkQueue(processedFilename)
        return render_template('queue.html', old_file = oldFilename,
                               new_file = processedFilename, queue_place = queuePlace)

    return render_template('processed.html', old_file = 'underlords/uploads/' + oldFilename, 
                           new_file = 'underlords/uploads/' + processedFilename, roll_data = rollData)

@app.route('/underlords/check-queue/<filename>', methods=['POST'])
def check_queue(filename):
    return jsonify({'queue': checkQueue(filename)})


@app.route('/underlords/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.abspath(app.config['UPLOAD_FOLDER']), filename)
