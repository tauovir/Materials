def make_upper(name):
    return name.upper()


def avgrage(a, b, c):
    return (a + b + c) / 3


def main(name, m1, m2, m3=50):
    name_upper = make_upper(name)
    avg = avgrage(m1,m2,m3)
    return {"name": name_upper, "avg": avg}


name = "python programs"
m1, m2, m3 = 10, 20, 30
result = main(name, m1, m2)
print(result)


# positiinal arg,