def main():
    user_info = input('Info: ').strip().split(', ')
    
    for i in user_info:
        if i.startswith('Ism'):
            print(f'Ism: {i[4:]}')
        if i.startswith('Familiya'):
            print(f'Familiya: {i[9:]}')
        if i.startswith('Yil'):
            print(f'Yil: {i[4:]}')
    
main()