import pytz

OPERATION_TRANSLATE = {
            'availability': 'Disponibilità',
            'spendable': 'Limite di spesa',
            'email': 'Email',
            'author': 'Autore',
            'name': 'Nome',
            'changed': 'cambiato/a',
            'from': 'da',
            'to': 'a'
        }

def operationEnToIt(operation):
    operationSplit = operation.split()
    new_operation = ''

    for word in operationSplit:
        if word in OPERATION_TRANSLATE.keys():
            new_operation += ' %s ' % OPERATION_TRANSLATE[word]
        else:
            new_operation += ' %s ' % word

    return new_operation
    