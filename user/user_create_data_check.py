import string

def passwordMatch(data):
    password = data['password']
    confirm_password = data['confirm_password']

    if password != confirm_password:
        return 'unmatch'
    return ''

def hasSpecialChar(data):
    password = data['password']
    charList = ['@', '#', '!', '?', '=', '_', '-', '+', '*', '(', ')', '[', ']', '{', '}', '£', '$', '%', '&', '^']

    for char in password:
        if char in charList:
            return ''
    return 'special'

def hasDigit(data):
    password = data['password']
    numList = string.digits

    for char in password:
        if char in numList:
            return ''
    return 'digit'

def hasLowercase(data):
    password = data['password']
    lowerList = string.ascii_lowercase

    for char in password:
        if char in lowerList:
            return ''
    return 'lowercase'

def hasUppercase(data):
    password = data['password']
    upperList = string.ascii_uppercase

    for char in password:
        if char in upperList:
            return ''
    return 'uppercase'

def spendableCheck(data):
    spendable = data['spendable']
    availability = data['availability']

    if spendable > availability:
        return 'spendable'
    return ''

checkFuncList = [passwordMatch, hasSpecialChar, hasDigit, hasLowercase, hasUppercase, spendableCheck]
errorMessages = {'unmatch': "Passwords don't match.", 
                 'special': "Password must contain at least a special character.",
                 'digit': "Password must contain at least one digit.",
                 'lowercase': "Password must contain at least a lowercase letter.",
                 'uppercase': "Password must contain at least an uppercase letter.",
                 'spendable': "Spending limit must be lower than availability."}
relations = {
    'unmatch': 'confirm_password',
    'special': 'password',
    'digit': 'password',
    'lowercase': 'password',
    'uppercase': 'password',
    'spendable': 'spendable'

}

def checkSuite(data, checklist = checkFuncList, error_messages = errorMessages, relations = relations):
    # The variable checklist is passed with the default value
    # so that by simply adding or removing a function from
    # checkFuncList will still do the job.
    #
    # Data is extracted locally by each check to make this
    # possible additions/removals even smoother.

    errorList = []
    for func in checklist:
        result = func(data)
        if result != '':
            errorList.append(result)
    return errorList, relations, error_messages

