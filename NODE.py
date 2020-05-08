class Node:
    def __init__(self,val,right,left):
        """
        Creation de multitude de noeud
        val : la donnée du noeud
        right : le fils droit
        left : le fils gauche
        """
        self.__val=val
        self.__right=right
        self.__left=left

    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left
    def __str__(self):
        return str(self.__val)

    def setRight(self,RIGHT):
        self.__right=RIGHT
    def setLeft(self,LEFT):
        self.__left=LEFT
"""
if __name__=='__main__':
    noeud1=Node(12,17,5)
    print(noeud1.getRight())
    print(noeud1.getLeft())
    noeud2=Node(5,6,4)
"""
