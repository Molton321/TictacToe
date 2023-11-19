"""
Posibles formas de importar 
import node as node
from node import Node
from node import *
"""
import node
import json

"""se presenta un caso de herencia en el que la clase Tree hereda de la clase Node
la herencia se hace al momento de declarar la clase Tree y se le pasa como parametro
el objeto Node que se quiere heredar """


class Tree(node.Node):
    """Constructor de la clase

    Keyword arguments:
        Player: str -- El jugador va a ser el que empieza
        Status: list[list] -- El estado inicial del tablero
    Return: 
        Crea el arbol con el nodo raiz
    """

    def __init__(self, player: str = 'X', status: list = [[0, "O", "X"], [0, 0, "O"], ["O", "X", 0]]):
        super().__init__(player, status)
        self.root = self
        self.node_count = 1

    """Agregar los hijos a un nodo
    
    Keyword arguments:
        father: Node -- El nodo al que se le van a agregar los hijos
    """

    def add_Children(self, father: node):
        children = father.children
        status = father.copy_Status()
        # print(id(status), id(father.status))
        for i in range(3):
            for j in range(3):
                if status[i][j] == 0:
                    status[i][j] = father.player
                    score = self.get_score(status, i, j, father.player)
                   
                    if father.player == 'X':
                        child = node.Node(
                            'O', self.copy_Status(status), father, score)
                    elif father.player == 'O':
                        child = node.Node(
                            'X', self.copy_Status(status), father, score)
                    self.node_count += 1
                    children.append(child)

                    status = father.copy_Status()
                elif status[i][j] == 'X' or status[i][j] == 'O':
                    continue

    def get_score(self, status: list, i: int, j: int, player: str):
        adjacent = self.get_adjacent(status, i, j)
        score = 0
        for cell in adjacent:
            if cell == player:
                if player != self.root.player:
                    score = -5
                else:
                    score = 5
        return score
    """Obtener las celdas adyacentes a una celda"""
    def get_adjacent(self, status, i, j):
        adjacent_cells = []
        dir = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1), (0, 1),
               (1, -1), (1, 0), (1, 1)]

        for d in dir:
            new_i = i + d[0]
            new_j = j + d[1]

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                adjacent_cells.append(status[new_i][new_j])

        return adjacent_cells
    
    """Determina si el juego ha terminado o no"""
    
    def game_over(self, node: node):
        
        if self.is_end(node.status):
            node.fin = True
            if node.player == self.root.player:
                node.score = -10
            else:
                node.score = 10
        elif node.children == []:
            node.leaf = True
            if node.player == self.root.player:
                node.score = -10
            else:
                node.score = 10

    """retorna si el juego ha terminado o no"""
    def is_end(self, status):
        for i in range(3):
            for j in range(3):
                if status[i][0] == status[i][1] == status[i][2] != 0:
                    return True
                elif status[0][j] == status[1][j] == status[2][j] != 0:
                    return True
                elif status[0][0] == status[1][1] == status[2][2] != 0:
                    return True
                elif status[0][2] == status[1][1] == status[2][0] != 0:
                    return True
                else:
                    return False
                
    def safe_win(self, node: node):
        victories = 0
        for child in node.children:
            for grandchild in child.children:
                if grandchild.fin:
                    victories += 1
        
        if victories >= 2:
            if node.player != self.root.player:
                node.score = 10
            else:
                node.score = -10
                
    """ Crea el arbol a partir de un nodo
    
    Keyword arguments:
        father: Node -- El nodo desde el cual se va a crear el arbol
    """

    def create_Tree(self, father: node):
        
        if father.leaf and not father.fin:
            father.leaf = False
            self.add_Children(father)
            if father.children != []:
                for child in father.children:
                    self.create_Tree(child)
                    
        self.game_over(father)
        self.safe_win(father)

    
                
    """Propaga los scores desde las hojas hasta la raiz"""
    def minimax(self, node):
            if node.fin :
                return node.score
            
            scores = []
            for child in node.children:
                score = self.minimax(child)
                scores.append(score)

            if node.player != self.root.player:  # Si es el turno del jugador actual
                node.score = max(scores)  # Seleccionar el mejor puntaje
            else:
                node.score = min(scores)  # Seleccionar el peor puntaje para el oponente

            return node.score
    
    """convierte un archivo json a un arbol
    Keyword arguments:
        filename: str -- El nombre del archivo JSON
    
    """

    def load_tree(self, filename: str):
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            self.root = self.json_to_node(data)

    """
    Convierte el árbol a un archivo JSON

    Keyword arguments:
        filename: str -- El nombre del archivo JSONs
    """

    def to_json(self, filename: str):
        with open(filename, "w") as json_file:
            json.dump(self.root.to_dict(), json_file, indent=4)
    # with es un manejador de contexto que se encarga de cerrar el archivo
    # open abre el archivo en modo escritura, as es para dar un alias al archivo
    # json.dump convierte el diccionario a un archivo json
