
def parser(str):
    # try:
    #     a = int(st)
    #     return a
    # except ValueError:
    #     flag = None
    #     if st[0] == '-':
    #         st = st[1:]
    #         flag = True
    #     i = 0
    #     a = b = ''
    #     sign = ''
    #     while i < len(st):
    #         if st[i].isnumeric() and sign == '' :
    #             a += st[i]
    #             if flag:
    #                 a = '-'+ a
    #                 flag = False
    #         elif st[i].isnumeric() and sign is not '':
    #             b += st[i]
    #         elif st[i] == '+' or st[i] == '-':
    #             if sign == '':
    #                 sign = st[i]
    #             else:
    #                 if sign == '+':
    #                     a = int(a)+int(b)
    #                 if sign == '-':
    #                     a = int(a)-int(b)
    #                 a = str(a)
    #                 sign = st[i]
    #                 b = ''
    #         i += 1
    #     if sign == '+':
    #         return int(a) + int(b)
    #     return int(a) - int(b)\
    total = 0
    current = ''
    operation = '+'
    
    for i in range(len(str)):
        if str[i] != '+' and str[i] != '-':
            current += str[i]
        elif str[i] == '+':
            if operation == '+':
                total += int(current)
            else:
                total -= int(current)
            operation = '+'
            current = ''
        else:
            if operation == '+':
                total += int(current)
            else:
                total -= int(current)
            operation = '-'
            current = ''
    if operation == '+':
        total += int(current)
    else:
        total -= int(current)
    return total 
        
print(parser('6+9-12'))
print('------------------')
print(parser('1+2-3+4-5+6-7'))
print(parser('1000+2-3+1-1000'))
print(parser('0.4+2-300+1-1000'))
print(parser('0+1-1-1000'))
print(parser('-1'))
print(parser('-1-1'))
print(parser('7+14-32-4'))


