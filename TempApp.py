from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()
    
    valor = datos['valor']
    escala_origen = datos['escala'].upper()  

    if escala_origen == 'C':
        resultado = (valor * 9/5) + 32
        escala_destino = 'F'
    elif escala_origen == 'F':
        resultado = (valor - 32) * 5/9
        escala_destino = 'C'
    else:
        return jsonify({"error": "Escala no válida. Usa 'C' o 'F'."}), 400

    respuesta = {
        "valor_original": valor,
        "escala_origen": escala_origen,
        "resultado": round(resultado, 2),
        "escala_destino": escala_destino
    }
    
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)
