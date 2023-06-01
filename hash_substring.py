# python3

def read_input():
    source = input().strip().upper()
    pattern, text = '', ''
    if source == 'I':
        pattern = input().strip()
        text = input().strip()
    elif source == 'F':
        with open("tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    positions = []

    p = len(pattern)
    t = len(text)

    p_hash = sum(ord(pattern[i]) * pow(10, p - 1 - i) for i in range(p))
    t_hash = sum(ord(text[i]) * pow(10, p - 1 - i) for i in range(p))

    for i in range(t - p + 1):
        if p_hash == t_hash and pattern == text[i:i+p]:
            positions.append(i)
        
        if i < t - p:
            t_hash = 10 * (t_hash - ord(text[i]) * pow(10, p - 1)) + ord(text[i + p])


    return positions



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

