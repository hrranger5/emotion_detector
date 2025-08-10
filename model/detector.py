# detector.py

def load_emotion_words(file_path='model/emotion_words.txt'):
    emotions = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(':')
                if len(parts) == 2:
                    emotion, words = parts
                    emotions[emotion.strip()] = [w.strip() for w in words.split(',')]
    return emotions

def detect_emotion(text):
    emotions = load_emotion_words()
    text = text.lower()
    score = {emotion: 0 for emotion in emotions}

    for emotion, words in emotions.items():
        for word in words:
            if word in text:
                score[emotion] += 1

    detected_emotion = max(score, key=score.get)
    if score[detected_emotion] == 0:
        return "Neutral or Not Detected"
    return detected_emotion.capitalize()
