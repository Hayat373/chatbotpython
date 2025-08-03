import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Hello, I'm testing spaCy in my chatbot!")
for token in doc:
    print(token.text, token.pos_)