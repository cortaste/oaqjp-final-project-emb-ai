import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input, headers=header)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    else:
        formattedResponse = json.loads(response.text)['emotionPredictions'][0]['emotion']
        m_emotion = max(formattedResponse, key=formattedResponse.get)    
        return {
            'anger': formattedResponse['anger'],
            'disgust': formattedResponse['disgust'],
            'fear': formattedResponse['fear'],
            'joy': formattedResponse['joy'],
            'sadness': formattedResponse['sadness'],
            'dominant_emotion': m_emotion
            }

