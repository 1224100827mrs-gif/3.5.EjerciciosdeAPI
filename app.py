from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()
    nombre = datos['nombre']
    calificaciones = datos['calificaciones']
    promedio = sum(calificaciones) / len(calificaciones)

    respuesta = {
    "nombre": nombre,
    "promedio": promedio
    }
    return jsonify(respuesta)
if __name__ == '__main__':
    app.run(debug=True)
