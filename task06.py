def main():
    text = input('Text: ').strip().split(' ')
    result = []

    for i in text:
        if i.lower() == i[::-1].lower():
            result.append(i)
    
    print(result)

main()