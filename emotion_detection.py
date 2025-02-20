import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Convert response text into a dictionary
        data = response.json()

        # Extract the relevant emotions
        emotions = data.get("emotion_predictions", [{}])[0]  # Get first item in the list
        scores = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
        }

        # Find the dominant emotion
        dominant_emotion = max(scores, key=scores.get)

        # Return the structured output
        return {
            "anger": scores["anger"],
            "disgust": scores["disgust"],
            "fear": scores["fear"],
            "joy": scores["joy"],
            "sadness": scores["sadness"],
            "dominant_emotion": dominant_emotion
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Example usage:
if __name__ == "__main__":
    text = "I am so happy I am doing this."
    result = emotion_detector(text)
    print(result)
