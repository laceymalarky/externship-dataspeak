# Initialization
from transformers import pipeline
import pandas as pd
import numpy as np
import spacy
from spacy.tokens import DocBin

import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title('DataSpeak Q&A Chatbot')


# Load Data
df = pd.read_csv(
    '/Users/laceymalarky/git_projects/TripleTen_projects/TripleTen_projects/externship-dataspark/data/python_q_a_clean_score3_AandQwc50.csv')
df['title_question'] = df.title + '. ' + df.question

# Deserialize docs
nlp = spacy.load("en_core_web_md")
doc_bin = DocBin().from_disk(
    "/Users/laceymalarky/git_projects/TripleTen_projects/TripleTen_projects/externship-dataspark/data/python_qa_titlequest.spacy")
docs = list(doc_bin.get_docs(nlp.vocab))

# User inputs question
input_question = st.text_area(
    label='Ask a Question:', value="", placeholder='Ask a Question', label_visibility="hidden")


# Calculate cosine similarity of input question, return top 5 questions in data
similarity = []
input_text = nlp(input_question)

for j in range(len(docs)):
    similarity.append(input_text.similarity(docs[j]))

top5 = pd.DataFrame(np.array(similarity).T, columns=[
                    'similarity']).sort_values(by='similarity', ascending=False)
top5 = top5.drop_duplicates()[:5]
top5 = top5.join(df[['title', 'question', 'title_question']]
                 ).reset_index(drop=True)

# Generate top 5 answers using top 5 title+quesitons from similarity analysis and % similarity


def generate_5_answers(top5_input):
    output = []
    for context in top5_input:
        generator = pipeline("text2text-generation",
                             model="lmalarky/flan-t5-base-finetuned-python_qa")
        answer_t5 = generator(f"answer the question: {context}")
        output.append(answer_t5[0]['generated_text'])
    return output


answer_gen_top5 = generate_5_answers(top5['title_question'])
answer_gen_top5 = pd.DataFrame(answer_gen_top5, columns=['generated_text'])
top5_gen_answ = answer_gen_top5.join(top5[['similarity']])

# Format output table
top5_gen_answ['similarity'] = top5_gen_answ['similarity'].map('{:.0%}'.format)
top5_gen_answ.columns = ['Possible Answer', '% Confidence']

st.table(top5_gen_answ)