def inc_num(num):
    print(num)
    if num > 10:
        return
    else:
        inc_num(num+1)


def dec_num(num):
    print(num)
    if num < 1 :
        return
    else:
        dec_num(num-1)


def sum_digit(num):
    if num <1:
        return 0
    else:
        r = num%10
        num = int(num/10)
        return r + sum_digit(num)

sum1 = 0
def digit_reverse(num):

    global sum1
    if num <1:
        return sum1
    else:
        r = num%10
        sum1=sum1 *10 +r
        num =int(num/10)
        return digit_reverse(num) # 1234,123,12,1,0

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)



def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1)+ recursive_fibonacci(n-2))



count =0
def count_vowels(name,pos):
    global count
    if pos >= len(name):
        return
    else:


        if name[pos].lower()in list('aeiou'):
            count += 1
        pos += 1
        count_vowels(name,pos)
        return count

rev=""
def string_palindrom(name,pos):
    global  rev
    if pos <0:
        return
    else:
        rev +=name[pos]
        pos -=1
        string_palindrom(name,pos)
        return rev
#

if __name__=="__main__":
    # n = factorial(5)
    # print(n)
    # inc_num(5)
    # dec_num(10)
    # print(sum_digit(num=600350))
    # print(digit_reverse(998822))
    # for i in range(1,10):
    #     print(recursive_fibonacci(i))

    name = "Khan is here pi ou"
    print(count_vowels(name,0))

    name = "banana"
    print(string_palindrom(name, len(name)-1))