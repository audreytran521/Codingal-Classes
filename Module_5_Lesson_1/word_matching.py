def match_words(words):
    ctr = 0 
    lst = [] 
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of words with the first and the same last character\n",lst)
    return ctr
count = match_words(["abba", "abc", "cfc", "1221", "xyz"])