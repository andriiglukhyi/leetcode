dengi = [ 1, 5, 10, 20, 100]

summa = float(input('Skolko deneg?'))

money = ""

if summa >= 100:
    num_of_hundreds = summa // 100
    summa = summa - num_of_hundreds * 100
    money = money + str(num_of_hundreds) + " nudrers, "
if summa >= 20:
    num_of_twenty = summa // 20
    summa = summa - num_of_twenty * 20
    money = money + str(num_of_twenty) + " twentys, "
if summa >= 10:
    num_of_tens = summa // 10
    summa = summa - num_of_tens * 10
    money = money + str(num_of_tens) + " tens, "
if summa >= 5:
    num_of_five = summa // 5
    summa = summa - num_of_five * 5
    money = money + str(num_of_five) + " fives, "
if summa >= 1:
    num_of_ones = summa // 1
    money = money + str(num_of_ones) + " ones, "\

print(money)





