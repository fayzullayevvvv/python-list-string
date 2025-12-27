def main():
    number = int(input('Num: '))
    result = ''

    for i in str(number):
        result += i + '-'
    
    print(result[:-1])

main()