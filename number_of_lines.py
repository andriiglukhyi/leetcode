def numberOfLines(self, widths, S):
    if len(S) == 0:
        return [0, 0]
    lines, width = 1, 0
    for c in S:
        w = widths[ord(c) - 97]
        if width > 100:
            lines += 1
            width = w
        else:
            width += w
    return lines, width