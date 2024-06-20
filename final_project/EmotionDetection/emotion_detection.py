import requests
import json 

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 500:
        return None

def format_output(response):
    if response:
        formatted_response = json.loads(response)
        result = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = find_top_dominant_emotion(result)
        result.update(dominant_emotion)
        return result
    else:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 
        'dominant_emotion': None}

def find_top_dominant_emotion(result):
    max_score = 0
    dominant_emotion = None
    for emotion, score in result.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion
    return {'dominant_emotion': dominant_emotion}