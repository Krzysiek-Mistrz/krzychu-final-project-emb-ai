import requests
import json

def emotion_detection(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    payload = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=payload, headers=headers)
    json_response = json.loads(response.text)

    if response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
        return result

    emotion_dict = json_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    result = {
        'anger': emotion_dict.get('anger'),
        'disgust': emotion_dict.get('disgust'),
        'fear': emotion_dict.get('fear'),
        'joy': emotion_dict.get('joy'),
        'sadness': emotion_dict.get('sadness'),
        'dominant_emotion': dominant_emotion
    }
    
    return result
