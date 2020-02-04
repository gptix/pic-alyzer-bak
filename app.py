"""Simplest Heroku app that receives requests and provides responses per picfest project."""
from flask import Flask, request
import gunicorn

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)


    @app.route('/')
    def index ()
    return "<h1>Hi there!</h1"

    @app.route('/summary', methods=['POST'])
    """Receive and process a request for classification of one image. Sample message containing URL for one image:

{
	"image": "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1"
}
"""
    def summary():
    
        message = "{'frogs' : '2'}"

        return message

        return app


    @app.route('/batch_img_summary', methods=['POST'])
"""Receive and process a request for classification of a batch of images. Sample message :

{
	"images": [
		"https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1",
		"https://michelangelostestbucket.s3.us-west-2.amazonaws.com/b46c5e2c17813f956df74118d60cfff7",
	]
}
"""
    def batch_img_summary():
    
        message = "{'classifications' : {{'frogs' : '4'}, {'sharks' : '17'}}}"
    
        return message

    return app