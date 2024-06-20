"""Server for final project"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, format_output

app = Flask("Sentiment Analyzer")

@app.route("/")
def render_index_page():
    """Welcome page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """Run text analyze"""
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    response = emotion_detector(text_to_analyze)
    result = format_output(response)
    if result['dominant_emotion']:
        return f"For the given statement, the system response is 'anger': {result['anger']}, \
        'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. \
        The dominant emotion is {result['dominant_emotion']}."
    return 'Invalid text! Please try again!.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
