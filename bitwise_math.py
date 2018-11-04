byteSize = 8

def bitAt(num, index):
    return (num >> index) & 1

def addBits(a, b):
    result = a ^ b
    carry = a & b
    return result, carry

def add(a, b):
    sum = 0
    carry = 0
    for i in range(byteSize):
        part, carry1 = addBits(bitAt(a, i), bitAt(b, i))
        result, carry2 = addBits(part, carry)
        sum |= result << i
        carry = carry1 | carry2
    return sum

def mult(a, b):
    product = 0
    for i in range(byteSize):
        if bitAt(a, i):
            product = add(product, b << i)
    return product

def main():
    print(11, "+", 9, "=", add(11, 9))
    print(5, "*", 3, "=", mult(5, 3))

if __name__ == "__main__":
    main()
