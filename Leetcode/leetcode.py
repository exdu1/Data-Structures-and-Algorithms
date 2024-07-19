def findWordsContaing(words: list[str], x: str) -> list[int]:
    n = len(words)
    matches = []

    for k in range(n):
        for i in words[k]:
            if i == x:
                matches.append(k)
                break;
    return matches


words = ['leet', 'code']
x = 'e'
findWordsContaing(words, x)
        