"""
Flask application for emotion detection.

This module sets up a Flask app with two routes:
1. The root ("/") which renders an HTML page.
2. The "/emotionDetector" route that calls an emotion detection API
   and returns the emotions and the dominant emotion for a given text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Render the HTML template, index.html
@app.route("/")
def render_index_page():
    """
    Render the index page of the application.
    
    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('index.html')


# API route for emotion detection
@app.route('/emotionDetector')
def emotion_detector_api():
    """
    Emotion detection API endpoint. 
    Processes the input text and returns the detected emotions.
    
    Returns:
        str: A response with the detected emotions or an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Test if there is a text given as input
    if text_to_analyze:
        # Pass the text to the emotion_detector function and store the response
        result = emotion_detector(text_to_analyze)
        # Format the response in the desired output format
        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']},  and 'sadness': {result['sadness']}, "
            f"The dominant emotion is {result['dominant_emotion']}. "
        )
        # Return the formatted response as plain text
        return response_text

    # If no input text is provided, return an error message
    return 'Invalid text! Please try again'


# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
