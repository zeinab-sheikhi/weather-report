def join_tokens(tokens):
    list_ = []

    for i, token in enumerate(tokens):
        if (token == ""): 
            continue

        if ((i > 0) and (token[0] not in set([".", "?", ",", ":", " "]))): 
            list_.append(" ")
        list_.append(token)

    return "".join(list_)
