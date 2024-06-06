if __name__ == "__main__":
    # 1 - Counter: Returns the count of items in given iterable
    from collections import Counter
    # Count up items of the list
    print(Counter(['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']))
    sentence = 'How many times does each word show up in this sentence with a word'
    print(Counter(sentence))             # Count up letters in string
    print(Counter(sentence.split()))     # Count up words in sentence
    print(Counter([1, 2, 3, 3, 4, 4, 1, 7]).most_common(3))  # return 3 most common numbers in list

    # Useful patterns of the Counter
    c = Counter('qwweertttyyy!!!!!')
    sum(c.values())                 # total of all counts
    dict(c)                         # convert to regular dict
    list(c)                         # list unique elements
    set(c)                          # convert to set
    c.items()                       # convert to list of (elem, cnt) pairs
    n = 3
    c.most_common()[:- n - 1:-1]    # n least common elements
    c += Counter()                  # remove zero and negative counts
    c.clear()                       # reset counts

    # 2 - Default dictionary: returns the default value attempting to get the dict value by the missing key
    from collections import defaultdict
    d = defaultdict(lambda: 'nothing')
    d['correct key'] = 'value'
    print(d['missing key'])

    from collections import namedtuple
    Person = namedtuple('Person', ['name', 'age', 'sex'])
