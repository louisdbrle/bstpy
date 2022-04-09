# import graphviz
from random import sample
from matplotlib import pyplot as plt
from math import log2


# class BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert node
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    # get min value
    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()

    # height
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None and self.right is not None:
            return self.right.height() + 1
        elif self.right is None and self.left is not None:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1

    # delete node bst
    def delete(self, value):
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.value = self.right.get_min_value()
                self.right = self.right.delete(self.value)
        return self

    # print tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    # graphviz tree
    def graphviz_tree(self, graph):
        if self.left:
            graph.edge(str(self.value), str(self.left.value))
            self.left.graphviz_tree(graph)
        if self.right:
            graph.edge(str(self.value), str(self.right.value))
            self.right.graphviz_tree(graph)


# main
if __name__ == '__main__':
    max_len = 1000000
    i = 10
    x_axis = []
    y_axis1 = []
    y_axis2 = []
    tab = []
    temp = 0
    temp_height = 0
    imb_tab = []
    height_tab = []
    while i <= max_len:
        x_axis.append(i)
        y_axis1.append(1.4*log2(i))
        y_axis2.append(7.2*log2(i))
        temp_tab = []
        for j in range(50):
            temp_tab.append(sample(range(i), i))
        tab.append(temp_tab)
        i *= 10

    for k in tab:
        for l in k:
            bst = BST(l[0])
            for m in l[1:]:
                bst.insert(m)
            if bst.right is not None and bst.left is not None:
                temp += abs(bst.right.height() - bst.left.height())
                temp_height += bst.height()
        imb_tab.append(temp / 50)
        height_tab.append(temp_height / 50)

    '''
    g = graphviz.Digraph('g')
    bst.graphviz_tree(g)
    g.render('tree', view=True)
    imb1 = abs(bst.right.height() - bst.left.height())
    print(imb1)
    '''

    plt.plot(x_axis, imb_tab, label='Experimental')
    plt.plot(x_axis, y_axis1, '-', label='Theoretical')
    plt.xlabel('Number of elements')
    plt.ylabel('Imbalance')
    plt.legend()
    plt.grid()
    plt.show()
    plt.savefig('imb.png')

    plt.plot(x_axis, height_tab, label='Experimental')
    plt.plot(x_axis, y_axis2, '-', label='Theoretical')
    plt.xlabel('Number of elements')
    plt.ylabel('Height')
    plt.legend()
    plt.grid()
    plt.show()
    plt.savefig('height.png')
