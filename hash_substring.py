# python3

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 101
    m = 10 ** 9 + 7

    n = len(text)
    k = len(pattern)

    pattern_hash = 0
    for i in range(k):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m

    text_hash = 0
    for i in range(k):
        text_hash = (text_hash * p + ord(text[i])) % m

    occurrences = []
    for i in range(n - k + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + k]:
                occurrences.append(i)

        if i < n - k:
            text_hash = (text_hash - ord(text[i]) * pow(p, k - 1, m)) % m
            text_hash = (text_hash * p + ord(text[i + k])) % m

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

