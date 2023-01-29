from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text

def bubble_sort(arr):
    for i in arr(0,len(input)-1):
        for j in range(0,len(input)-1):
            if input[j] > input[j+1]:
                (input[j],input[j+1]) = (input[j+1],input[j])
    return input