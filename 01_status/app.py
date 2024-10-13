from flask import Flask

app = Flask(__name__)

@app.route("/poem")
def poem():
    return '''
Once upon a midnight dreary, While I websurfed, weak and weary, Over many a strange and spurious website of hot chicks galore,

While I clicked my fav'rite bookmark, Suddenly there came a warning, And my heart was filled with mourning, Mourning for my dear amour.

'Tis not possible!, I pleaded, But my browser, so conceited, Remained blank, I then repeated, Just a blank and nothing more.

With a scream, I was defeated, For my cookies were deleted, So i begged, no longer seated, "Give me back my free hardcore!"

Then, in answer to my query, Through the net I loved so dearly, Came its answer, dark and dreary: Quoth the server, 404
'''
