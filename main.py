from flask import Flask, render_template, url_for
 
app = Flask(__name__)
 
menu = ["Установка", "Первое приложение", "Обратная связь"]
 
@app.route("/")
def index():
    print( url_for('index') )
    return render_template('index.html', menu = menu)

if __name__ == "__main__":
    app.run(debug=True)
