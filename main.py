import graphviz


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
        else:
            graph.edge(str(self.value), str(self.value))
        if self.right:
            graph.edge(str(self.value), str(self.right.value))
            self.right.graphviz_tree(graph)

    # get min value
    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()


# main
if __name__ == '__main__':
    bst = BST(10)
    bst.insert(5)
    bst.insert(6)
    bst.insert(4)
    bst.insert(12)
    bst.insert(11)
    bst.insert(15)
    bst.delete(10)
    bst.insert(10)
    bst.print_tree()
    g = graphviz.Digraph('g')
    bst.graphviz_tree(g)
    g.render('tree', view=True)
