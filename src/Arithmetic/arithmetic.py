# From CS1010S, no further rework for now

def make_decimal_to_n_ary_converter(n):
    if 1<n<17:
        def decimal(number):
            if number < 1:
                return '0'
            else:
                temp = number
                alp = ['A','B','C','D','E','F']
                hexa = [str(i) for i in range(10,16)]
                k = 0
                while n**k <= temp:
                    k += 1
                ls = [0]*k
                for i in range(len(ls)):
                    while n**(len(ls)-i-1) <= temp:
                        temp -= n**(len(ls)-i-1)
                        ls[i] += 1
                    ls[i] = str(ls[i])
                    if ls[i] in hexa:
                        ls[i]=alp[hexa.index(ls[i])]
                
                return "".join(ls)
            
        return decimal
    else:
        return '0'

def make_n_ary_to_decimal_converter(n):
    # return a number converter that takes a string representation of a base n number and returns its decimal equivalent
    def decimal(number):
        alp = ['A','B','C','D','E','F']
        hexa = [i for i in range(10,16)]
        result = 0
        for i in range(len(number)):
            if number[i] in alp:
                result += hexa[alp.index(number[i])]*(n**(len(number)-i-1))
            else:
                result += int(number[i])*(n**(len(number)-i-1))
        return result
    return decimal

def compose(f, g):
    return lambda x: f(g(x))

def make_p_ary_to_q_ary_converter(p, q):
    # return a number converter that takes a string representation of a number in base p and returns the string representation of that number in base q
    return compose(make_decimal_to_n_ary_converter(q),make_n_ary_to_decimal_converter(p))

arithmetic = make_p_ary_to_q_ary_converter(8,16)
num = input()
mod = 4 - (4-len(num)) % 4 # 1,2,3,4
result = arithmetic(num[:mod])
for i in range((len(num)-mod)//4):
    mini = arithmetic(num[4*i+mod:4*(i+1)+mod])
    result += "0"*(3-len(mini))+mini
print(result)