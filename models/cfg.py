import random

from .tree import Tree


class CFG:
    
    def __init__(self, rules, axiom):
        self.rules = rules
        self.axiom = axiom
        self.non_terminals = set(rule.lhs for rule in self.rules)
        self.terminals = set(rhs for rule in self.rules for rhs in rule.rhs if rhs not in self.non_terminals)
        self.lhs_to_rules = {}
            
        for rule in self.rules:
            lhs = rule.lhs
            if lhs in self.lhs_to_rules.keys():
                self.lhs_to_rules[lhs].append(rule)
            else:
                self.lhs_to_rules[lhs] = [rule]

    def isTerminal(self, sym):
        return (sym in self.terminals)

    def isNonTerminal(self, sym):
        return (sym in self.non_terminals)

    def generate(self):
        tree = Tree(label=self.axiom)

        stack = [tree]
        
        while (len(stack) > 0):
            
            node = stack.pop() 
            print("Node selected for expansion: ", node)
            
            if (self.isTerminal(node.label)): 
                continue
            assert self.isNonTerminal(node.label), f"Unknown symbol: {node.label}"

            rules = self.lhs_to_rules[node.label]  
            rule = random.choice(rules)
            node.children = [Tree(label=sym) for sym in rule.rhs]
            stack.extend(reversed(node.children))  
            print(tree, "\n")

        return tree

    def __str__(self):
        return f"CFG({self.terminals}, {self.non_terminals}, {self.rules}, {self.axiom})"

    def __repr__(self):
        return self.__str__()
