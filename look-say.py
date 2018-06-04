def looksay(look):
    look = str(look)
    prev, count, say = look[0], 1, ''
    for char in look[1:]:
        if char == prev:
            count += 1
            continue
        say += str(count) + prev
        prev = char
        count = 1
    print(say + str(count) + prev)
    return say + str(count) + prev


# if 'main' == __name__:
looksay(8)
