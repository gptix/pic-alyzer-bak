"""Simplest Heroku app that receives requests and provides responses
per picfest project."""

import json
from flask import Flask, request

## Probably do not need to import img_pred, since others call it.
from .classifier import img_pred, image_dict_to_response, batch_to_response_set

if __name__ == "__main__":
    app.run()rt test_single_image_msg, test_batch_msg


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    

    @app.route('/')
    ## TODO: delete after testing.
    def index():
        return "<html><body><h1>Hi there!</h1></body></html>"
    

    @app.route('/summary', methods=['GET', 'POST'])
    def summary():
        """Receive and process a request for classification of one image."""
        # image_path=request['image']
        # image_batch_dict="foo"
        
        # image_path = "foo"  # dummy function doesn't even use value.

        ## This returns bare JSON object returned by classifier.
        ## This block is test code.
        # return img_pred(image_path)

        ## This returns JSON for one image.
        # image_dict = request['images'][0]
        # return image_dict_to_response(image_dict)

        ## This returns JSON for one image, as a singleton.
        #@image_batch_dict = request['images']
        image_batch_dict =Push rejected, failed to compile Python app.
    
    @app.route('/batch_img_summary', methods=['GET', 'POST'])
    def batch_img_summary():
        """Receive and process a request for classification of a batch of
        images."""
#        image_batch_dict = request['images']

        # Test
        image_batch_dict = test_batch_msg
        #image_paths = ['foo', 'foo']

        ## This block is test code.
        #results = []
        #for image_json in images:
        #    result = img_pred_and_wrap(image_json)
        #    results.append(result)
        #return "{'classifications' : " + json.dumps(results) + "}"

        return batch_to_response_set(image_batch_dict)

    return app
