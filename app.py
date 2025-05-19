from flask import Flask, render_template, request, redirect
from helper import vectorizer, get_prediction, preprocessing
from logger import logging

app = Flask(__name__)

logging.info("Flask server started")

data = dict()
reviews = []
positive = 0
negative = 0

@app.route('/')
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    logging.info("=========== Open Home Page ==============" )
    return render_template('index.html', data=data)



@app.route('/', methods=['POST'])
def my_post():
    logging.info("=========== Open Post Page ==============" )
    text = request.form['text']

    logging.info("Text: %s", text)
    preprocessed_text = preprocessing(text)
    logging.info("Preprocessed Text: %s", preprocessed_text)
    vectorized_text = vectorizer(preprocessed_text)
    logging.info("Vectorized Text: %s", vectorized_text)
    prediction = get_prediction(vectorized_text)
    logging.info("Prediction: %s", prediction)

    if prediction == "Positive":
        global positive
        positive += 1
    else:
        global negative
        negative += 1

    reviews.insert(0, text)

    return redirect(request.url)
if __name__ == '__main__':
    app.run()