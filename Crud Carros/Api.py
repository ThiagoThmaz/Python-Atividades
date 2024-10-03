from flask import Flask , request , jsonify
import db

app = Flask ( __name__ )

@app.route("/carros", methods=["GET"])
def get_all_carros():
    return (db.carros, 200)

@app.route ("/carros/<int:id>", methods =["GET"])
def get_carro (id):
    for car in db.carros:
        if id == car ['id']:
            return jsonify ( car ) , 200
        
    info = {'title ': 'Nao encontrado ', 'status ': 404}
    return jsonify ( info ) , 404

@app.route("/carros", methods=['PUT'])
def atualiza_carro():
    dado = request.json
    for ind, car in enumerate(db.carros):
        print(car["id"])
        if car["id"] == dado["id"]:
            db.carros[ind] = dado
            return jsonify(dado), 200
        
    info = {"title": "Carro not found", "status": 404 , "type": " https://fiap.com.br/car_not_found", "detail ": f""" Carro nao encontrado com o id especificado {dado ['id']}""", "instance": f"/carros/{ dado ['id']}"}
    return jsonify(info), 404
    
@app.route("/carros/<int:id>", methods=['DELETE'])
def apaga_carros(id):
    for ind, car in enumerate(db.carros):
        if car['id'] == id:
            dado = db.carros.pop(ind)
            return jsonify(dado), 200
    
    info = {'title': 'Não encontrado carro com este id', 'status': 404}
    return jsonify(info), 404

app.run ( debug = True )
