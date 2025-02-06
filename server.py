"""
Creates flask server to handle requests to app which utilizes NN of watson.ai

Functions:

sent_analyzer
render_index_page
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """
    Function sent_analyzer takes arguments from js file and send 
    them to emotion_detection which actually sends them to NN, 
    which performs NLP.

    Parameters:
        None

    Returns:
        string: analyzed text with emotions statistic
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detection(text_to_analyze)

    result = {
        "anger": response.get("anger"), 
        "disgust": response.get("disgust"),
        "fear": response.get("fear"),
        "joy": response.get("joy"),
        "sadness": response.get("sadness"),
    }
    dominant_emotion = response.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    fstr1 = f"For the given statement, the system response is {result}. "
    fstr2 = f"The dominant emotion is {dominant_emotion}."
    return fstr1 + fstr2

@app.route("/")
def render_index_page():
    """
    Function which actually only renders index.html on start of app

    Parameters:
        None

    Returns:
        <file>.html
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
