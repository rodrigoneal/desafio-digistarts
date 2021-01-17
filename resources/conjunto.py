from typing import Any
from flask_restful import Resource, reqparse

numeros = (
    []
)  # variavel que armazena os dicionarios contento os valores numericos -1000<=K<=1000

limite = 0  # variavel de controle  1<=N<=1000

req = reqparse.RequestParser()
req.add_argument(
    "number", type=int, required=True, help="number only accepts integer value"
), 400


def verifica_numeros():
    """
    Verifica se o tamanho de numeros é igual valor limite
    :return: lista com os numeros unicos e ordenados
    """
    global id
    resultado = list()
    if len(numeros) == limite:
        for num in numeros:
            n = int(num["number"])
            if n not in resultado:
                resultado.append(n)
        resultado.sort()
        numeros.clear()
        id = 0
        return resultado

# Eu poderia colocar dentro da função pois só está sendo usado dentro de uma unica função, mas não gosto de staticmethod
def id_not_found(numeros: list[dict], id: int) -> Any:
    """
    Procura o id passdo dentro da lista numeros
    :param numeros: lista que armazena o dicionario
    :param id: id recebido por endpoint
    :return: 404 se não encotrar o id ou dicionario com o id pesquisado
    """

    for num in numeros:
        if num["id"] == id:
            return num
    return {"message": "id not found"}, 404


def limit_not_defined(func):
    """
    Decorador que verifica se o valor de limite foi passado e quebra a função se não tiver
    :param func: função decorada
    :return: None ou quebra a função com um status_code 400
    """
    global limite

    def deco_function(*args, **kwargs):
        if limite <= 0:
            return {"message": "the limit value must be passed before"}, 400
        return func(*args, **kwargs)

    return deco_function


class ListaConjuntos(Resource):
    global limite
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

    @limit_not_defined
    def post(self):
        """
        Cria um dicionario e appenda(armazena) dentro da variavel numeros
        :return:Um Json com o valor com o id e valor recebido
        :rtype: JSON
        """

        # ID: usada como identificar para facilita o acessos e modificações
        global id
        numero = req.parse_args()
        number = {"id": id, **numero}

        numeros.append(number)
        id += 1

        resultado = verifica_numeros()
        if resultado: return resultado

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
        return {"message": f"limit {limit}"}, 201


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
        resultado = id_not_found(numeros, num_id)
        return resultado

    @limit_not_defined
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

        if numeros:
            for num in numeros:
                if num["id"] == num_id:
                    num["number"] = numero["number"]
                    return {"message": f"id {num_id} has been modified"}
        number = {"id": num_id, **numero}
        numeros.append(number)
        id = num_id + 1
        resultado = verifica_numeros()
        if resultado: return verifica_numeros()

        return {"message": f"id '{num_id}' successfully added"}, 201

    @limit_not_defined
    def delete(self, num_id):
        """
        Deleta o dicionario com o id passado por endpoint
        :return: Mensagem informado se o valor foi deletado
        :rtype: JSON
        """
        num_id = int(num_id)
        global numeros
        if numeros:
            for n in range(len(numeros)):
                if numeros[n]["id"] == num_id:
                    del numeros[n]
                    return {"message": f"The id {num_id} has been deleted"}
        return {"message": f" id '{num_id}' not found"}, 404
