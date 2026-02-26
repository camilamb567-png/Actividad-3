from flask import Flask, request, render_template


app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('inicio.html')

@app.route("/suma", methods=["GET", "POST"])
def sumar():
    if request.method == "POST":
        if not request.form.get("num1") or not request.form.get("num2"):
            return f"Por favor, ingrese dos números válidos."
        else:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            resultado = num1 + num2
            return render_template("suma.html", resultado=resultado)
    return render_template("suma.html")



if __name__ == '__main__':
    app.run(debug=True) 














