def filter_big(letter):
    if letter.isupper():
        return True
    else:
        return False


string = 'Настя лучшая ДЕВОЧКА на свете'
i = 3
j = 23

big_letters = list(filter(filter_big, string[i-1:j]))
print(len(big_letters))
