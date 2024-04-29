import string

def parse_string(password:str)-> dict:
    """ Args: string (password)
        (This function hleps us to count numerical, character, special_symbols uppercase and lowercase patterns from password)
        returns: dict """

    counts = {'zero': 0, 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0, 'seven': 0, 'eight': 0, 'nine': 0, 'nums':0, 'chars':0, 'upper':0, 'lower':0, 'special':0}
    for e in password:
        try:
            num = int(e)
            counts['nums'] += 1 
            counts.update({list(counts.keys())[num]:list(counts.values())[num] + 1})
        except:
            if e in string.punctuation:
                counts['special'] += 1
            else:
                counts['chars'] += 1
                if e.isupper():
                    counts['upper'] += 1
                else:
                    counts['lower'] += 1
            
    return counts