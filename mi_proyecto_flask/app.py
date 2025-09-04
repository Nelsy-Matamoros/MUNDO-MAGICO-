from flask import Flask, render_template, request, redirect, url_for
import os
import json
import csv



app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de formulario
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']

        # Guardar en TXT
        with open('datos/datos.txt', 'a') as f:
            f.write(f"{nombre},{email}\n")

        # Guardar en JSON
        datos_json = []
        if os.path.exists('datos/datos.json'):
            with open('datos/datos.json', 'r') as f:
                try:
                    datos_json = json.load(f)
                except json.JSONDecodeError:
                    datos_json = []
        datos_json.append({"nombre": nombre, "email": email})
        with open('datos/datos.json', 'w') as f:
            json.dump(datos_json, f, indent=4)

        # Guardar en CSV
        with open('datos/datos.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([nombre, email])

        return redirect(url_for('resultado'))
    return render_template('formulario.html')

# Ruta para mostrar resultados
@app.route('/resultado')
def resultado():
    # Leer desde TXT
    datos_txt = []
    if os.path.exists('datos/datos.txt'):
        with open('datos/datos.txt', 'r') as f:
            datos_txt = f.readlines()

    # Leer desde JSON
    datos_json = []
    if os.path.exists('datos/datos.json'):
        with open('datos/datos.json', 'r') as f:
            try:
                datos_json = json.load(f)
            except json.JSONDecodeError:
                datos_json = []

    # Leer desde CSV
    datos_csv = []
    if os.path.exists('datos/datos.csv'):
        with open('datos/datos.csv', 'r') as f:
            reader = csv.reader(f)
            datos_csv = list(reader)

    return render_template('resultado.html', txt=datos_txt, json_data=datos_json, csv_data=datos_csv)

if __name__ == '__main__':
    app.run(debug=True)
