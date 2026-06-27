# Online Course Reviews Topic Modeling Using Latent Dirichlet Allocation (LDA)

https://colab.research.google.com/drive/12c6UEZ12VKQatyT-Zaix3M2ZyWUef32b#scrollTo=sEUs-1XNMfeT




# 📚 Smart Online Course Review Analyzer AI

## 📌 Project Overview

**Smart Online Course Review Analyzer AI** is an NLP-based application that automatically discovers hidden topics from online course reviews using **Latent Dirichlet Allocation (LDA)**. Instead of manually reading thousands of student reviews, the system groups similar reviews into meaningful topics such as **Course Content, Instructor Quality, Assignments, Pricing, and Platform Experience**.

This project demonstrates **Topic Modeling**, an unsupervised machine learning technique that helps educational platforms understand student feedback and make data-driven improvements.

---

# 🎯 Problem Statement

Online learning platforms receive thousands of student reviews every day. Analyzing each review manually is time-consuming and inefficient. Educational institutions need an automated approach to identify the major discussion topics from student feedback.

This project applies **Latent Dirichlet Allocation (LDA)** to automatically identify hidden topics from course reviews, enabling instructors and platform administrators to understand learner concerns and improve course quality.

---

# 🎯 Objective

* Automatically identify hidden topics from online course reviews.
* Group similar reviews into meaningful categories.
* Help educators understand student feedback.
* Support data-driven improvements in online learning platforms.

---

# 🚀 Features

* Upload and analyze online course reviews
* Automatic text preprocessing
* Topic Modeling using LDA
* Displays Top Keywords for each topic
* Assigns the most relevant topic to each review
* Predicts the topic of a new review
* Interactive Topic Visualization
* WordCloud visualization
* User-friendly Gradio interface

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* NLTK
* Scikit-learn
* CountVectorizer
* Latent Dirichlet Allocation (LDA)
* Matplotlib
* WordCloud
* pyLDAvis
* Gradio

---

# 📂 Dataset

**Dataset:** Coursera Reviews Dataset

The dataset contains student reviews collected from online courses.

Example Review:

> "The instructor explained every concept clearly and the assignments were very useful."

---

# ⚙ Workflow

```
Load Dataset
      │
      ▼
Data Exploration
      │
      ▼
Text Preprocessing
      │
      ▼
CountVectorizer
      │
      ▼
Document-Term Matrix
      │
      ▼
Latent Dirichlet Allocation (LDA)
      │
      ▼
Topic Extraction
      │
      ▼
Assign Topic to Reviews
      │
      ▼
Topic Visualization
      │
      ▼
Predict Topic for New Reviews
```

---

# 📊 Example Topics

| Topic   | Description         |
| ------- | ------------------- |
| Topic 0 | Course Content      |
| Topic 1 | Instructor Quality  |
| Topic 2 | Assignments         |
| Topic 3 | Pricing             |
| Topic 4 | Platform Experience |

---

# 📈 Example Output

**Input Review**

```
The instructor explained every concept very clearly and the assignments were helpful.
```

**Predicted Topic**

```
Instructor Quality
```

---

# 💡 Applications

* Online Learning Platforms
* Course Review Analysis
* Student Feedback Analysis
* Educational Analytics
* E-learning Platforms
* Customer Feedback Mining
* Opinion Mining
* NLP Research
* Text Analytics
* Business Intelligence

---

# 📁 Project Structure

```
Smart-Online-Course-Review-Analyzer-AI
│
├── app.py
├── requirements.txt
├── lda_model.pkl
├── count_vectorizer.pkl
├── topic_names.pkl
├── Coursera_reviews.csv
├── README.md
```

# 📷 Output

The application allows users to:

* Enter a course review
* Predict the most relevant topic
* View topic probabilities
* Explore discovered topics

---

# 🔮 Future Enhancements

* Sentiment Analysis Integration
* Multi-language Support
* Automatic Topic Naming
* Dashboard with Analytics
* Topic Trend Analysis
* Course Recommendation System
* Instructor Performance Dashboard
* Real-time Review Monitoring

---

# 👨‍💻 Prepared by

**R. Sugumar, M.B.A.,**
