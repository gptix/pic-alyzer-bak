"""Simplest Heroku app that receives requests and provides responses per picfest project."""
from flask import Flask, request

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)


    @app.route('/')
    def index():
        return "<html><body><h1>Hi there!</h1></body></html>"


    @app.route('/summary', methods=['POST'])
        """Receive and process a request for classification of one image."""
    def summary():
        return "{'frogs' : '2'}"


    # @app.route('/batch_img_summary', methods=['POST'])
        # """Receive and process a request for classification of a batch of images."""
        # ### Sample message :
        # # {
	    # #"images": [
	    # #	"https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1",
	    # #	"https://michelangelostestbucket.s3.us-west-2.amazonaws.com/b46c5e2c17813f956df74118d60cfff7",
	    # #]
        # #}
        # def batch_img_summary():   
        #     return "{'classifications' : {{'frogs' : '4'}, {'sharks' : '17'}}}"
    
    return app

    # Sample message containing URL for one image:
    #{
	#"image": "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1"
    #}
