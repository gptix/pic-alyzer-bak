## This function is a dummy, until DS9 provides function that will provide response.
def img_pred(path):
    """Sends a path to an image to the classifier, should return a
    JSON object."""
    if path == "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1":
        result = "{'frogs' : '3'}"
    else:
        result = {'sharks': '17'}

    return result


def image_dict_to_response(image_dict):
    """Get prediction for one image, return in expected dict format."""
    return {'image_id' : image_dict['image_id'], 
            'result': image_pred(image_dict['image_url'])}


def batch_to_response_set(batch):
    """Get predictions for a batch of images, return as JSON object"""
    return {
        'results' : 
        list(map(image_dict_to_response, batch['images']))
            }
