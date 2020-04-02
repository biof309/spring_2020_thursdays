def fizzbuzz(n,fizz=3,buzz=5):
    output = []
    for number in range(n):
        if number % fizz == 0 and number % 5 == 0:
            output.append((number,"fizzbuzz"))
            continue
        elif number % 3 == 0:
            output.append((number,"fizz"))
            continue
        elif number % 5 == 0:
            output.append((number,"buzz"))
            continue
    return output

def main():
    print(fizzbuzz(10))


if __name__ == '__main__':
    main()