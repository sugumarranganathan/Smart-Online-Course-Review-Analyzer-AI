import gradio as gr
import pickle
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Load saved files
with open("lda_model.pkl","rb") as f:
    lda_model = pickle.load(f)

with open("count_vectorizer.pkl","rb") as f:
    cv = pickle.load(f)

with open("topic_names.pkl","rb") as f:
    topic_names = pickle.load(f)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z ]','',text)

    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return " ".join(words)


def predict_topic(review):

    review = clean_text(review)

    vector = cv.transform([review])

    prediction = lda_model.transform(vector)

    topic = prediction.argmax()

    confidence = prediction.max()

    probabilities = {}

    for i, value in enumerate(prediction[0]):

        probabilities[topic_names[i]] = round(float(value),4)

    return (
        topic_names[topic],
        round(float(confidence),4),
        probabilities
    )


demo = gr.Interface(

    fn=predict_topic,

    inputs=gr.Textbox(
        lines=6,
        placeholder="Enter Course Review Here..."
    ),

    outputs=[
        gr.Textbox(label="Predicted Topic"),
        gr.Number(label="Confidence"),
        gr.Label(label="Topic Probabilities")
    ],

    title="Online Course Reviews Topic Modeling Using LDA",

    description="""
This application predicts the most relevant topic from an online course review using
Latent Dirichlet Allocation (LDA).

Topics:

• Course Content

• Instructor Quality

• Assignments

• Pricing

• Platform Experience
"""
)

demo.launch()
