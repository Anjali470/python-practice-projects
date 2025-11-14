def analyze_string(text):
    length = len(text)
    vowels = 0
    consonants = 0
    digits = 0
    spaces = 0
    special_chars = 0
    letter_dict = {}
    largest = 0
    most_frequent = None
    for char in text:
        letter_dict[char] = letter_dict.get(char,0) + 1
        if largest < letter_dict[char]:
            largest = letter_dict[char]
            most_frequent = char
        if char.isalpha():
            if char in ('a','e','i','o','u','A','E','I','O','U'):
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        elif char == ' ':
            spaces += 1
        else:
            special_chars += 1

    result = {"length": length, 'vowels': vowels, 'consonants': consonants, 'digits': digits, 'spaces': spaces,
              'special_chars': special_chars, 'most_frequent': most_frequent}

    return result

def main():
    sentence = input("Enter a sentence: ")
    analysis = analyze_string(sentence)
    print(analysis)

if __name__ == '__main__':
    main()