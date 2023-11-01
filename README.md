# Generative Question and Answer Large Language Model
## Project Overview
DataSpeak, one of the industry's largest providers of predictive analytics solutions, needed help developing a proof-of-concept machine learning model that can automatically generate answers to user-input questions.

## Machine Learning Skills/Technologies
Text2TextGeneration, Transformers, Tokenizers, PyTorch, Hugging Face, FLAN-T5, Word2Vec, Streamlit, Render, GPU 

## Project Conclusions
- Developed a [generative language model](https://huggingface.co/lmalarky/flan-t5-base-finetuned-python_qa) using `google/flan-t5-base`, fine-tuned on Stack Overflow data.
- Conducted cosine semantic similarity analysis on a generated vector embeddings database to identify the top 5 most similar questions in the dataset for user-input questions.
- Developed a web application featuring a chatbot UI that provides generative answers from the model and generates 5 alternative answers based on cosine similarity, along with percent similarity scores.
- Performed pre-processing of raw data to improve the quality of the training set.

## Screenshot of Web Application UI
![Screenshot 2023-11-01 at 4 22 20 PM](https://github.com/laceymalarky/nlp_question_answer/assets/97048468/d9656ec0-d0ad-4b78-ab85-b9c66bf527c1)

## Performance & Evaluation
- Achieved a 19% ROUGE-1 score and an average perplexity of 1.96.
- Demonstrated high efficience, with response times under 10 seconds.
  
<img width="630" alt="Screenshot 2023-10-30 at 8 45 15 PM" src="https://github.com/laceymalarky/nlp_question_answer/assets/97048468/bc380430-48af-44fb-969f-198ba69053ba">

![image](https://github.com/laceymalarky/nlp_question_answer/assets/97048468/c6694fae-240a-49b1-b5e4-1a41b38d715e)

## Requirements
Python libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, nltk, transformers, spacy, torch

## Data Description:
[Python Questions from Stack Overflow](https://www.kaggle.com/datasets/stackoverflow/pythonquestions)
