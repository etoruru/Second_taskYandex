def read_file():
    f = open('file2.txt', 'r')
    text = f.read()
    text = text.replace('\n', '')
    data = text.split(' ')
    return data


def count_length(lst):
    num = 1
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            num += 1
    return num



def count_factors(length):
    return 2 ** length


def factor(num):
    d = 2
    fact = []
    while d * d <= num:
        if num % d == 0:
            fact.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        fact.append(d)
    return fact

def main(text):
    gcd, lcm = int(text[0]), int(text[1])
    mult = lcm // gcd
    if mult == 1:
        return 0
    else:
        factors = factor(mult)
        length = count_length(factors)
        amount_factors = count_factors(length)
        return amount_factors


def write_file(value):
    with open('result2.txt', 'w') as f:
        f.write(str(value))


if __name__ == '__main__':
    data = read_file()
    amount_factors = main(data)
    write_file(amount_factors)
