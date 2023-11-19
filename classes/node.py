import node as Node
"""Aclaracion: Se importa el modulo node simplemente para 
poder darle tipo a los parametros de los metodos
si se quiere eliminar se debe eliminar todos los : Node en los parametros"""

class Node:

    """Constructor del nodo

    Keyword arguments:
        player: str -- El jugador va a ser el que empieza 
        data: list[list] -- El estado inicial del tablero
        father: Node -- El nodo padre
        score: int -- El score de la jugada

    Return: 
        Crea el nodo con sus respectivos atributos
    """

    def __init__(self, player: str, data: list, father : Node = None, score: int = 0):
        self.status = data
        self.score = score
        self.player = player
        self.children = []
        self.father = father
        self.leaf = True
        self.fin = False

    """Docstring for Getters y Setters de los atributos del nodo
    
    Keyword arguments:
        Getters => No recibe ningun parametro
        Setters =>  data: list[list] -- El nuevo estado del tablero 
                    score: int -- El nuevo score de la jugada
    
    Return: 
        Getters => Retorna el atributo solicitado
        Setters => Cambia el valor del atributo solicitado por el argumento recibido
    """

    def get_Status(self):
        return self.status

    def set_Status(self, data: list):
        self.status = data

    def get_Score(self):
        return self.score

    def set_Score(self, score: int):
        self.score = score

    def get_Children(self):
        return self.children

    
    """Copiar el estado de un nodo
    Este metodo es para evitar que se modifique el estado del tablero de cualquier
    nodo al crear una copia profunda eliminando las referencias tanto de la lista 
    externa como de la lista interna
    
    keyword arguments:
        status: list[list] -- El estado del tablero a ser copiado
        
    return:
        Retorna el estado del tablero copiado sin referencias a la lista original 
    """
    
    def copy_Status(self, status: list = None):
        if status is None:
            status = self.status
        return list(map(lambda x: x.copy(), status)) 
    # map aplica una funcion(lambda x: x.copy()) a cada elemento de la lista (status)
    # Lambda es una funcion anonima que recibe un parametro x "(listas internas)" y retorna x.copy() la copia de las listas internas
    
    """Convierte el nodo a un diccionario
    Preferible solo usar con la raiz del arbol
    Return: 
        Retorna el nodo en forma de diccionario
    """
    
    def to_dict(self):
        
        return {
            "player": self.player,
            "status": [str(self.status[0]), str(self.status[1]), str(self.status[2])],
            "score": self.score,
            "is end": self.fin,
            "children": list(map(lambda child: child.to_dict(), self.children)),
             
            # map aplica una funcion(lambda child: child.to_dict()) a cada elemento de la lista (children)
            # lambda es una funcion anonima(recursiva) que recibe un parametro child y repite el proceso hasta que no haya mas hijos
        }
        
    