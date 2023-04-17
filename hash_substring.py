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
    # This function finds the occurrences of the pattern in the text using the Rabin-Karp algorithm
    # It returns a list of positions where the pattern occurs in the text
    positions = []

    # Get the lengths of the pattern and the text
    p = len(pattern)
    t = len(text)

    # Calculate the hash value of the pattern and the first substring of text of length p_len
    p_hash = sum(ord(pattern[i]) * pow(10, p - 1 - i) for i in range(p))
    t_hash = sum(ord(text[i]) * pow(10, p - 1 - i) for i in range(p))

    # Slide the pattern over the text and check for hash match
    for i in range(t - p + 1):
        if p_hash == t_hash and pattern == text[i:i+p]:
            positions.append(i)
        # If there are more characters in the text, calculate the hash value of the next substring using rolling hash
        if i < t - p:
            t_hash = 10 * (t_hash - ord(text[i]) * pow(10, p - 1)) + ord(text[i + p])

    # Return the list of positions where the pattern occurs in the text
    return positions



if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

