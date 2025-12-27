def main():
    emails = input('Emails: ').strip().split(',')
    result = []

    for email in emails:
        idx = email.find('@')
        if email[idx:] not in result:
            result.append(email[idx:])

    print(result)

main()