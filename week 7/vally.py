#is_email_address = checkers.is_email('test@domain.dev')


from validator_collection import checkers

user = input("email? ")
if checkers.is_email(user):
    print("valid")
else:
    print("invalid")