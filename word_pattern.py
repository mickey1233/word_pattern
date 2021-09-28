def wordpattern(pattern, s):
    dic = {}
    work = set()
    s = s.split(' ')
    if len(pattern) != len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] in dic:
            if s[i] != dic[pattern[i]]:
                return False
        else:
            if s[i] in work:
                return False
            dic[pattern[i]] = s[i]
            work.add(s[i])
    return True


if __name__ == "__main__":
    print(wordpattern("abba", "dog cat cat dog"))
    print(wordpattern("abba", "dog cat cat fish"))
    print(wordpattern("aaaa", "dog cat cat dog"))
    print(wordpattern("abba", "dog dog dog dog"))
