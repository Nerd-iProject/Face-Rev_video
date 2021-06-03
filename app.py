from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory,Response
from camera import VideoCamera
import urllib.request
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


def gen(camera):
    while True:
        data= camera.get_frame()

        frame=data[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True,port=5000)