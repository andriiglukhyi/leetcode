def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
          print('False')
          return False

    return True

is_pangram('this is my world')