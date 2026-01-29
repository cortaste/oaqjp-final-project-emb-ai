""" A Flask Server that allows the user to run a sentiment analysis on a text """
from flask import Flask, render_template, request
from EmotionDetector import emotion_detection

app = Flask('app')

@app.route('/emotionDetector')
def detector():
    """ Runs the sentiment analysis and returns the result"""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detection.emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    return f"""For the given statement, the system response is 'anger':
        {result['anger']}, 'disgust': {result['disgust']},
        'fear': {result['fear']}, 'joy': {result['joy']}
        and 'sadness': {result['sadness']}. 
        The dominant emotion is {result['dominant_emotion']}."""

@app.route('/')
def index_page():
    """ Returns the starting page of the app """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    