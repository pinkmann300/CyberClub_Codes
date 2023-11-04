def base_converter(number, base):
    arr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J']
    fina = []
    workin_arr = arr[0:base]
    
    while (number != 0):
        fina.append(workin_arr[number % base])
        number = number // base 

    fina = fina[::-1]
    return fina 


def palindrome_check(base):
    for i in range(0,300):
        if base_converter(i ** 2, base) ==  (base_converter(i ** 2, base)[::-1]):
            finstr = ""
            for i in range(0,len(base_converter(i ** 2, base))):
                finstr += base_converter(i ** 2, base)[i]
        else:
            continue 


palindrome_check(10)
