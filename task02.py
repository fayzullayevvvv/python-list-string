def main():
    text = input('Text: ').strip().lower().split(' ')
    result = ''

    for i in text:
        if i[-1] == ',':
            result += i[:-1] + '_'
        else:
            result += i + '_'
    
    print(result[:-1])

main()