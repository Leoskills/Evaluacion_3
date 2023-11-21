from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/evaluacion1', methods=['GET', 'POST'])
def evaluaCion1():
    if request.method == 'POST':
        Nota1 = float(request.form['Nota1'])
        Nota2 = float(request.form['Nota2'])
        Nota3 = float(request.form['Nota3'])
        resultado1 = (Nota1 + Nota2 + Nota3)/3
        Asistencia = float(request.form['Asistencia'])
        if Asistencia >= 80 and resultado1 >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('evaluacion1.html', resultado1=resultado1, estado=estado, Nota1=Nota1, Nota2=Nota2, Nota3=Nota3, Asistencia=Asistencia)
    return render_template('evaluacion1.html')



@app.route('/evaluacion2', methods=['GET', 'POST'])
def evaluaCion2():
    if request.method == 'POST':
        Nombre1 = str(request.form['Nombre1'])
        Nombre2 = str(request.form['Nombre2'])
        Nombre3 = str(request.form['Nombre3'])
        resultado1 = len(Nombre1)
        resultado2 = len(Nombre2)
        resultado3 = len(Nombre3)
        if resultado1 >= resultado2 and resultado3:
            estado1 = "contiene mas caracteres"
        return render_template('evaluacion2.html', estado1=estado1, resultado1=resultado1, resultado2=resultado2, resultado3=resultado3, Nombre1=Nombre1, Nombre2=Nombre2, Nombre3=Nombre3)
    return render_template('evaluacion2.html')

if __name__ == '__main__':
    app.run(debug=True)