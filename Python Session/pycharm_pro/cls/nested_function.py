

m1 = 99
def outer():
    m1 = 10
    print("Outer function:",m1)
    m1 = m1 + 20
    print(m1)
    def inner():
        m2 = 200
        nonlocal m1
        m1 = m1 + 25
        print("m1:",m1)
        print("m2:", m2)
        print("inner function")
    inner()


def factorial(num):
    print("Calculating factorial of :",num)
    def fact(num):
        if num <=1:
            return 1
        return num * fact(num-1)

    return fact(num)


def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power


def mean():
    sample = []
    def inner_mean(number):
        sample.append(number)
        print(sample)
        return sum(sample) / len(sample)
    return inner_mean


""""
Defining a Closure Function

"""
def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
# another = print_msg("Hello")
# another()

if __name__ == "__main__":
    # outer()
    # print(factorial(5))
    # raise_pwd = generate_power(2)
    # print(raise_pwd(2))
    # print(raise_pwd(3))
    # print(raise_pwd(4))
    mean_inr = mean()
    print(mean_inr(10))
    print(mean_inr(20))
    print(mean_inr(40))
    mean_inr2 = mean()
    print(mean_inr2(100))
    print(mean_inr2(200))
