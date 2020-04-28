from NODE import Node

class BinaryTree:
    def __init__(self,root):
        """
        assemblage des noeuds
        root: le noeud racine de l'arbre
        """
        self.__root=root

    def getRoot(self):
        return self.__root

    def isRoot(self, node):
        return self.__root==node

    def size(self, node):
        count=1

        if node is None:
            return 0
        if node is not None:

            if node.getLeft() is not None:
                count+=self.size(node.getLeft())
            if node.getRight() is not None:
                count+= self.size(node.getRight())

        return count


    def printValues(self, node):
        liste=[]
        liste.append(node)


        if node is None:
            return
        if node is not None:
            if node.getLeft() is not None:
                liste=liste+[self.printValues(node.getLeft())]
                del liste[-1]
            if node.getRight() is not None:
                liste=liste + [self.printValues(node.getRight())]
                del liste[-1]
        del liste[-1]
        for i in liste:
            print(i)

    def sumValues(self, node):# qui calcule la somme de toutes les valeurs des noeuds de l'arbre
        liste=[]
        liste.append(node)


        if node is None:
            return
        if node is not None:
            if node.getLeft() is not None:
                liste=liste+[self.printValues(node.getLeft())]
                del liste[-1]
            if node.getRight() is not None:
                liste=liste + [self.printValues(node.getRight())]
                del liste[-1]

        #print(liste)





if __name__=='__main__':
    """
    mes noeuds
    Creation de multitude de noeud:val,right,left
        val : la donnée du noeud
        right : le fils droit
        left : le fils gauche
    On construit de la feuille jusqu'à la racine
    """
    noeud3 = Node(3, None, None)
    noeud4 = Node(4, None, noeud3)
    noeud6 = Node(6, None, None)
    noeud5 = Node(5, noeud6, noeud4)
    noeud18 = Node(18, None, None)
    noeud21 = Node(21, None, None)
    noeud19 = Node(19, noeud21, noeud18)
    noeud17 = Node(17, noeud19, None)

    noeudRoot = Node(12, noeud17, noeud5) #noeud racine

    Root = BinaryTree(noeudRoot) #definition en tant que noeud racine
    #########################################################################################

    #print(Root.isRoot(noeud3))

    #print(Root.size(noeudRoot)) #La taille d'un arbre est son nombre de noeuds


    print(Root.printValues(noeudRoot))


    #print(Root.sumValues(noeudRoot))


