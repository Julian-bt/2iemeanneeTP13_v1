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

    def size(self, node,compteur):
        print('right:',node.getRight())
        print('left:',node.getLeft())
        print('compteur:',compteur)

        left=node.getLeft() #nouveau noeud ou None
        right=node.getRight() #nouveau noeud ou None

        if left==None and right==None: #noeud feuille
            return compteur
        else:
            if left!=None and right==None: #new noeud gauche
                return self.size(left,compteur+1)
            if left!=None and right!=None: #deux new noeuds
                self.size(left,compteur+1),self.size(right,compteur+1)
            if right!=None and left==None: #new noeud droit
                return self.size(right,compteur+1)


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

    print(Root.isRoot(noeud3))

    n=1 #on comptabilise le noeud actuel
    print(Root.size(noeud19,n))





