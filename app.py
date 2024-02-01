from models.cfg import CFG
from utils.rules import toy_rules, weather_rules
from utils.helpers import join_tokens


toy_grammar = CFG(rules=toy_rules, axiom="S")
weather_grammar = CFG(rules=weather_rules, axiom="FORECAST")

g_toy = toy_grammar
g_weather = weather_grammar
grammars = [g_toy, weather_grammar]

for g in grammars:

    print("The grammar is:\n", g, "\n")
    print("The non-terminals are:\n", g.non_terminals, "\n")
    print("The terminals are:\n", g.terminals, "\n")
    print(g.lhs_to_rules, "\n")
    print()

    for _ in range(1):
        tree = g.generate()
        print("sampled tree:", tree)
        tokens = tree.get_yield()
        print("yield:", tokens)
        text = join_tokens(tokens)
        print("text:", text)
        print("\n")
