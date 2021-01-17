from flask_restful import Resource, reqparse

numeros = (
    []
)  # variavel que armazena os dicionarios contento os valores numericos -1000<=K<=1000

limite = 0  # variavel de controle  1<=N<=1000

req = reqparse.RequestParser()
req.add_argument(
    "number", type=int, required=True, help="number only accepts integer value"
), 400


class ListaConjuntos(Resource):
    """
    A classe é usada pela biblioteca flask_restful trabalhar os verbos http
    Não tem repr pois não é usada fora do contexto do flask, nem instanciada no flask shell
    """

    def get(self):
        """
        Mostra todos os arquivos dentro da lista de numeros no endpoit /
        :return: Uma lista com dicionarios [{id:valor, number:valor}]
        :rtype: JSON
        """
        return numeros

    def post(self):
        """
        Cria um dicionario e appenda(armazena) dentro da variavel numeros
        :return:Um Json com o valor com o id e valor recebido
        :rtype: JSON
        """

        # ID: usada como identificar para facilita o acessos e modificações
        global id, limite
        if (
            limite > 0
        ):  # Só vai appenda se o valor de limite foi passado antes, senão vai returnar status_code:400
            numero = req.parse_args()
            number = {"id": id, **numero}

            numeros.append(number)
            id += 1
        else:
            return {"message": "the limit value must be passed before"}, 400

        if (
            len(numeros) == limite
        ):# :return: Lista com valores unicos em ordem crescente
            resultado = []
            for num in numeros:
                n = int(num["number"])
                if n not in resultado:
                    resultado.append(n)
            resultado.sort()
            numeros.clear()
            id = 0
            return resultado
        return number, 201


class Limite(Resource):
    """
    A classe é usada pela biblioteca flask_restful trabalhar os verbos http
    """

    def post(self, limit):
        """
        Recebe o valor por endpoint e define o limite de valores aceitos antes de retorna uma lista unica e ordenada
        :return: JSON informado o valor de limite passado
        :rtype: JSON
        """
        limit = int(limit)
        global limite, id
        limite = limit
        numeros.clear()
        id = 0
        return {"message": f"limit {limit} created"}, 201


class ListaConjunto(Resource):
    """
     A classe é usada pela biblioteca flask_restful trabalhar os verbos http
     """
    def get(self, num_id):
        """
        Procura dentro da varialvel numeros se há o id passado por endpoint
        :return:Se Encontrar: Json com a id passada
        :return:Se Não Encontrar:  Uma mensagem com o status_code 404
        """
        num_id = int(num_id)
        for numero in numeros:
            if numero["id"] == num_id:
                return numero
        return {"message": "number not found"}, 404

    def put(self, num_id):
        """
        Procura dentro da varialvel numeros se há o id passado por endpoint
        :return: Se Encontrar: Cria um novo dicionario com o valor de id passado por endpoint com o valor number passado por
        requests
        :return Se encontrar modifica o dicionario com o valor number passado por request
        """
        numero = req.parse_args()
        global id, limite
        num_id = int(num_id)
        if limite > 0:
            if numeros:
                for num in numeros:
                    if num["id"] == num_id:
                        num["number"] = numero["number"]
                        return {"message": f"id {num_id} has been modified"}
            number = {"id": num_id, **numero}
            numeros.append(number)
            id = num_id + 1
            return {"message": f"id '{num_id}' successfully added"}, 201
        return {"message": "the limit value must be passed before"}, 400

    def delete(self, num_id):
        """
        Deleta o dicionario com o id passado por endpoint
        :return: Mensagem informado se o valor foi deletado
        :rtype: JSON
        """
        num_id = int(num_id)
        num_id = int(num_id)
        global numeros
        if numeros:
            for n in range(len(numeros)):
                if numeros[n]['id'] == num_id:
                    del numeros[n]
                    return {'message': f'The id {num_id} has been deleted'}, 204
        return {'message':f" id '{num_id}' not found"}, 404

