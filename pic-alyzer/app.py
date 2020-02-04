"""Simplest Heroku app that receives requests and provides responses per picfest project."""
from flask import Flask, request
from .classifier import img_pred

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)


    @app.route('/')
    def index():
        return "<html><body><h1>Hi there!</h1></body></html>"


    @app.route('/summary', methods=['GET', 'POST'])
    def summary():
        """Receive and process a request for classification of one image."""
        # image_path=request['image']
        image_path = "foo" # dummy function doesn't even use value.
        return img_pred(image_path)
        

    @app.route('/batch_img_summary', methods=['GET', 'POST'])
    def batch_img_summary():   
        """Receive and process a request for classification of a batch of images."""
        # image_paths = request['images']
        image_paths = ['foo', 'foo']

        results = []
        for path in image_paths:
            result = img_pred(path)
            results.append(result)
        return "{'classifications' : " + str(results) + "}"


    return app


    # Sample message containing URL for one image:
    #{
	#"image": "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1"
    #}

    ### Sample message :
        # {
	    #"images": [
	    #	"https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1",
	    #	"https://michelangelostestbucket.s3.us-west-2.amazonaws.com/b46c5e2c17813f956df74118d60cfff7",
	    #]
        #}
    