import string

def spendableCheck(data):
    spendable = data['spendable']
    availability = data['availability']

    if spendable > availability:
        return 'spendable'
    return ''

checkFuncList = [spendableCheck]
errorMessages = {'spendable': "Spending limit must be lower than availability."}
relations = {
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

