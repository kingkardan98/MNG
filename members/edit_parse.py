# -----------------------------  AUXILIARY  -----------------------------
# -----------------------------  FUNCTIONS  -----------------------------

OPERATION_TRANSLATE = {
    'Availability': 'Disponibilità',
    'Spendable': 'Limite di spesa',
    'Email': 'Email',
    'Author': 'Autore',
    'Name': 'Nome',
    'availability': 'Disponibilità',
    'spendable': 'Limite di spesa',
    'email': 'Email',
    'author': 'Autore',
    'name': 'Nome',
    'changed': 'cambiato/a',
    'from': 'da',
    'to': 'a'
        }

OPERATION_FORMAT = {
    '.availability': '. Availability',
    '.spendable': '. Spendable',
    '.email': '. Email',
    '.author': '. Author',
    '.name': '. Name'
}

def operationEnToIt(operation):
    # Let 'operationFormat()' handle the formatting of the string.
    # Make a list of all words.
    operation = operationFormat(operation).split()
    new_operation = ''

    for word in operation:
        if word in OPERATION_TRANSLATE.keys():
            # If the word is in the translated dictionary,
            # append the translated version.
            new_operation += ' %s ' % OPERATION_TRANSLATE[word]
        else:
            # If the word is not in the translated dictionary,
            # append it and move on.
            new_operation += ' %s ' % word

    return new_operation
                  
def operationFormat(operation):
    new_operation = ''
    key = ''
    i = 0
    while i in range(len(operation)):
        # Start checking for any dots.

        if operation[i] == '.':
            # If a dot is found, reset the temporary 
            # empty string 'key'.
            # Start a new for loop to iterate upon the 'key' variable.
            key = ''
            key += operation[i]
            j = i+1
            while j in range(i+1,len(operation)):
                if operation[j] == ' ' or operation[j] == '.':
                    # If a space is found, or another dot, the 'key' variable 
                    # is ready to be checked.
                    if key in OPERATION_FORMAT:
                        # If 'key' is in the dictionary, add its dictionary value to 'new_operation'.
                        # Setting i = j-1 makes sure the external for loop skips all the characters
                        # that were appended to 'key'.
                        new_operation += OPERATION_FORMAT[key]
                        i = j-1
                        break
                    else:
                        # If 'key' wasn't in the dictionary, just append the dot
                        # and don't skip any characters.
                        new_operation += '.'
                        break
                else:
                    key += operation[j]
                j += 1
        else:
            new_operation += operation[i]
        i += 1

    # Add a final dot for grammatical correctness.
    new_operation += '.'
    return new_operation