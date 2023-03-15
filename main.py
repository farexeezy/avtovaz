from flask import Flask, render_template, url_for
 
app = Flask(__name__)
 
menu = ["Установка", "Первое приложение", "Обратная связь"]
 
@app.route("/")
def index():
    print( url_for('index') )
    return render_template('index.html', menu = menu)

@app.route("/l_granata")
def l_granata():
    print( url_for('l_granata') )
    return render_template('l_granata.html', menu = menu)

@app.route("/l_redan")
def l_redan():
    print( url_for('l_redan') )
    return render_template('l_redan.html', menu = menu)

@app.route("/l_largus")
def l_largus():
    print( url_for('l_largus') )
    return render_template('l_largus.html', menu = menu)

if __name__ == "__main__":
    app.run(debug=True)
