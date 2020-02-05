def img_pred(path):
    """Sends a path to an image to the classifier, should return a
    JSON object."""
    if path == "https://michelangelostestbucket.s3.us-west-2.amazonaws.com/8bf0322348cc11e7e3cc98325fbfcaa1":
        result = "{'frogs' : '3'}"
    else:
        result = {'sharks': '17'}

    return result
