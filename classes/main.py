import Tree 
import node as node


def main():
  player = input("Ingrese el jugador con el que desea jugar: ")[0].upper()
  status =[[],[],[]]
  if player != "0" :
    for i in range(3):
      for j in range(3):
        status[i].append(str(input("Ingrese el estado del tablero: ")[0].upper()))
        print(status)
    arbol = Tree.Tree(player, status)
  else:
    arbol = Tree.Tree()

  arbol.create_Tree(arbol.root)
  arbol.minimax(arbol.root)
  arbol.to_json("arbol-prueba.json")
  print("""--------------------------------------------------------
             Codigo finalizado con exito""")

if __name__ == "__main__":
    main()
