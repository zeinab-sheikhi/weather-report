class Tree:

    def __init__(self, label, children=[]):
        self.label = label
        self.children = children
 
    def get_yield(self):
        list_ = []  
        self.get_yield_aux(prefix=list_)

        return list_

    def get_yield_aux(self, prefix):
        if (len(self.children) == 0):  
            prefix.append(self.label)
        else:
            for child in self.children: 
                child.get_yield_aux(prefix)

    def __str__(self):
        list_ = []
        self.str_aux(list_)

        return " ".join(list_)

    def str_aux(self, list_):
        if (len(self.children) == 0):  
            list_.append(self.label)
        else:
            list_.extend(["[", self.label])
            for child in self.children: 
                child.str_aux(list_)
            list_.append("]")
