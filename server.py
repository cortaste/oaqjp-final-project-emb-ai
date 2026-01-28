from flask import Flask
from EmotionDetector import emotion_detection

app = Flask('app')

@app.route('/emotionDetector')
def detector():
    a= 5
    return f"For the given statement, the system response is 'anger': {a}, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy."

if __name__ == 'main':
    app.run(debug=True)