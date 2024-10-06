# Import the requests library to handle HTTP requests, le json library to parse the reponse rom  the API
import requests, json

# Define a function named emotion_detector that takes a string  as input (text_to_analyse)
def emotion_detector(text_to_analyse):
     # If the input text is empty, return a response with None values
    if not text_to_analyse:
        return 'Invalid text! Please try again'


    # Define a function name emotion_detector that takes a string (text_to_analyse) as argument
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Create a dictionary  called 'myobj' with the text to analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }  
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the emotion Predict  API with the payload and headers
    response = requests.post(url, json = myobj, headers=header)

    #if the response status code is 200, extract the relevant emotions values from the response
    if response.status_code  == 200:
 
        # parsing the JSON response from the  API
        formatted_response = json.loads(response.text)
        # Extract the set of emotions  and their score from the formatted_response
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Extract emotions score 
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']

        # Find the dominant emotion using the maximum value of the dictionary emotions
        dominant_emotion = max(emotions, key=emotions.get)
        # Create the requested  response format
        new_response_format = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        # Return emotions with their score with the dominant emotion
        return new_response_format
    
    # if response status code is 400(not successful)
    return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

