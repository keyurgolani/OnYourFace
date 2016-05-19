from flask import Flask, request, redirect, url_for, render_template
import cv2, os, logging, shutil
from flask.ext.mysql import MySQL
import numpy as np
from PIL import Image
import json
import glob
from uuid import uuid4

app = Flask(__name__)
mysql = MySQL()

faceCascadeFile = 'OnYourFace/static/cascades/facesCascade.xml'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'LabelInfo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

class Details(object):
    firstName = ""
    lastName = ""
    location = ""
    birthdate = ""
    confidence = 0
    def __init__(self, firstName, lastName, location, birthdate, confidence):
        self.firstName = firstName
        self.lastName = lastName
        self.location = location
        self.birthdate = birthdate
        self.confidence = confidence

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/uploadPage")
def uploadPage():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():
    _firstName = request.form['firstName']
    _lastName = request.form['lastName']
    _location = request.form['location']
    _birthdate = request.form['birthdate']

    queryString = "select label_id from tbl_details where first_name = '{}' and last_name = '{}' and location = '{}' and birthdate = '{}'".format(_firstName, _lastName, _location, _birthdate)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(queryString)
    fetchLabel = cursor.fetchone()
    _label = None
    if fetchLabel is None:
        insertString = "insert into tbl_details (first_name, last_name, location, birthdate) values ('{}','{}','{}','{}')".format(_firstName, _lastName, _location, _birthdate)
        cursor2 = conn.cursor()
        cursor2.execute(insertString)
        conn.commit()
        cursor.execute(queryString)
        row = cursor.fetchone()
        _label = row[0]
    else:
        _label = fetchLabel[0]


    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = str(_label)

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True

    # Target folder for these uploads.
    target = "OnYourFace/static/uploads/{}".format(upload_key)
    try:
        if not os.path.exists(target):
            os.mkdir(target)
    except:
        if is_ajax:
            return ajax_response(False, "Couldn't create upload directory: {}".format(target))
        else:
            return "Couldn't create upload directory: {}".format(target)

    print "=== Form Data ==="
    for key, value in form.items():
        print key, "=>", value

    for upload in request.files.getlist("file"):
        filename = upload.filename.rsplit("/")[0]
        destination = "/".join([target, filename])
        print "Accept incoming file:", filename
        print "Save it to:", destination
        upload.save(destination)

    if is_ajax:
        return ajax_response(True, upload_key)
    else:
        return redirect(url_for("uploadPage"))

@app.route("/trainPage")
def trainPage():
    root = "OnYourFace/static/uploads"
    count = len([f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f))])

    return render_template("train.html",
        count = count
    )

@app.route("/train", methods=['POST'])
def train():

    cascadePath = "OnYourFace/static/cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    recognizer = cv2.face.createLBPHFaceRecognizer()
    # recognizer = cv2.face.createEigenFaceRecognizer()
    # recognizer = cv2.face.createFisherFaceRecognizer()
    if os.path.isfile(faceCascadeFile):
        recognizer.load(faceCascadeFile)

    imageRoot = "OnYourFace/static/uploads"
    count = len([f for f in os.listdir(imageRoot) if os.path.isdir(os.path.join(imageRoot, f))])
    labels = []
    images = []
    if count > 0:
        for label in os.listdir(imageRoot):
            folder = os.path.join(imageRoot, label)
            if os.path.isdir(folder):
                for imageFile in os.listdir(folder):
                    imagePath = os.path.join(folder, imageFile)
                    image_pil = Image.open(imagePath).convert('L')
                    image = np.array(image_pil, 'uint8')
                    nbr = int(label)
                    faces = faceCascade.detectMultiScale(image)
                    for (x, y, w, h) in faces:
                        images.append(image[y: y + h, x: x + w])
                        labels.append(nbr)
                        cv2.waitKey(50)

        recognizer.update(images, np.array(labels))
        recognizer.train(images, np.array(labels))
        recognizer.save(faceCascadeFile)

        for label in os.listdir(imageRoot):
            folder = os.path.join(imageRoot, label)
            if os.path.isdir(folder):
                shutil.rmtree(folder)

    return render_template("recon.html")

@app.route("/recognizePage")
def recognizePage():
    return render_template("recon.html")

@app.route("/recognize", methods=['POST'])
def recognize():
    file = request.files['file']
    cascadePath = "OnYourFace/static/cascades/haarcascade_frontalface_alt.xml"
    recognizePath = 'OnYourFace/static/recognize'
    recognizer = cv2.face.createLBPHFaceRecognizer()
    # recognizer = cv2.face.createEigenFaceRecognizer()
    # recognizer = cv2.face.createFisherFaceRecognizer()
    if os.path.isfile(faceCascadeFile):
        recognizer.load(faceCascadeFile)
    file.save(os.path.join(recognizePath, file.filename))
    predict_image_pil = Image.open(os.path.join(recognizePath, file.filename)).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    faceCascade = cv2.CascadeClassifier(cascadePath)
    faces = faceCascade.detectMultiScale(predict_image)
    predicted_labels = []
    prediction_confidences = []
    for (x, y, w, h) in faces:
        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
        predicted_labels.append(nbr_predicted)
        prediction_confidences.append(conf)
        cv2.waitKey(1000)
    os.remove(os.path.join(recognizePath, file.filename))
    return recognizePage(predicted_labels, prediction_confidences)

def recognizePage(predicted_labels, prediction_confidences):
    people = []
    for i in range(len(predicted_labels)):
        queryString = "select first_name, last_name, location, birthdate from tbl_details where label_id = {}".format(predicted_labels[i])
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(queryString)
        row = cursor.fetchone()
        detail = Details(row[0], row[1], row[2], row[3], '{0:.4g}'.format(100 - (prediction_confidences[i]/2.5)))
        people.append(detail)
    return render_template("result.html",
        peopleList = people
    )

def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))
