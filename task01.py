def main():
    first_name = input('Ism: ').strip().title()
    second_name = input('Familiya: ').strip().title()
    third_name = input('Sharif: ').strip().title()

    user = [first_name, second_name, third_name]

    print('{}, {} {}'.format(user[1], user[0], user[2]))

main()