def alternatingCharacters(s):
    return sum(1 for c1, c2 in zip(s, s[1:]) if c1 == c2)


def check_all(strings):
    return [alternatingCharacters(s) for s in strings]
