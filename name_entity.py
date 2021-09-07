from flask import Flask, render_template, request
# from textblob import TextBlob
import spacy
nlp = spacy.load('en_core_web_sm')

# initialse the application
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit' , methods = ["POST"])
def form_data():
   input_text = request.form.get('input_text')
#    nlp = spacy.load('en_core_web_sm')

   doc = nlp(input_text)
   ner_dict ={}
   for token in doc.ents:
    #    print(f'{token} ---->{token.label_}')
        v = {token : token.label_}
        ner_dict.update(v)
   
   
   return render_template('predict.html' , corrected_data = f' {ner_dict}')
#    return render_template('predict.html' , sentence_data = f'Number of sentences are {sentence_length}')
if __name__ == '__main__':
    app.run(debug = True)
    # app.run(host = '0.0.0.0',port = 8080)

