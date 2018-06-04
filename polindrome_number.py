def _inner(i):
    """
    generate polindron numbers
    """
    limit = int('9' * i)
    for j in range(limit, 0, -1):
        for k in range(limit, j, -1):
            ans = j * k
            a = str(ans)
            if a == str(reversed(a)):
                return print(i, ans % 1337)
print(set(map(_inner, range(1, 9))))



"""
  solutions = [
            None, 9, 9009, 906609, 99000099,
            9966006699, 999000000999,
            99956644665999, 9999000000009999
        ]
"""