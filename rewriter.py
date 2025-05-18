import random

def simple_rewrite(text):
    synonyms = {
        "важно": ["существенно", "значимо", "необходимо"],
        "новость": ["информация", "сообщение", "сведение"],
        "сегодня": ["на текущий день", "в этот день", "в настоящий момент"],
        "обсуждают": ["говорят", "рассматривают", "поднимают вопрос"],
        "хороший": ["прекрасный", "замечательный", "отличный"]
    }
    for word, syns in synonyms.items():
        if word in text:
            text = text.replace(word, random.choice(syns))
    return text