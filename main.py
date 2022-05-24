from flask import Flask, render_template, request
import hhru.all_data as ad

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/form.html")
def form():
    return render_template('form.html')

@app.route("/results.html")
def results():
    result =  ad.get_data('NAME:(Python)')
    data = result[0]['requirements']
    keywords = result[0]['keywords']
    # data = ['python', 'js', 'java', 'sql', 'lua']
    return render_template('results.html', data=data, keywords = keywords)

@app.route("/contacts.html")
def contacts():
    developer_name = 'Konstantin Voloshenko'
    return render_template('contacts.html', name=developer_name, creation_date='24.05.2022')

if __name__ == "__main__":
    app.run(debug=True)