def read(file):
    with open(file, 'r') as f:
        return f.read().strip()

def isEmail(email_address:str) -> bool:

    # check that there is ONLY 1 @
    if '@' not in email_address:
        return False

    email_address_list = email_address.split('@')
    if len(email_address_list) != 2:
        return False
    # There is ONLY 1 @

    # Check that each end of the string is NOT empty
    if email_address_list[0].strip() == '' or email_address_list[1].strip() == '':
        return False
    # The ends of the string are NOT empty

    # Check that all characters are valid
    InvalidEmailCharacters = '!#$%&~'
    for i in email_address_list[0]:
        if i in InvalidEmailCharacters:
            return False


    ValidDomainCharacters = 'abcdefghijklmnopqrstuvwxyz0123456789.-'
    for i in email_address_list[1]:
        if i not in ValidDomainCharacters:
            return False
    # All characters in the string are valid

    return True

def findEmails(text:str):
    for i in text.split(' '):
        if isEmail(i):
            yield i

def findAllEmails(text:str):
    return list(findEmails(text))











def run():
    fname = input("Extract All Emails From(Path): ")

    data = read(fname)
    emailsFound = findAllEmails(data)

    print("Found Emails:", ', '.join(emailsFound))




if __name__ == "__main__":
    run()