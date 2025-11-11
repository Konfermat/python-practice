def ispalindrome(input: str)->bool:
    # print(isinstance(input, str))
    tmp = input.lower()
    tmp1 = ''.join(reversed(tmp))
    print(f'Являится ли {input} палиндромом? {tmp == tmp1}')
    return tmp == tmp1
    

    
