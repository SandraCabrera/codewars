def duplicate_encode(word):
    string = word.casefold()
    newString = ''
    auxString= ''
    repeatedCharacters = ''
    for character in string:
            if character not in auxString:
                auxString = auxString + character
            else:
                repeatedCharacters = repeatedCharacters + character
    for position in string:
        if position not in repeatedCharacters:
            newString = newString + '('
        else:
            newString = newString + ')'
    return newString



if __name__ == '__main__':

    #caso test
    #Test.assert_equals(duplicate_encode("din"),"(((")
    #Test.assert_equals(duplicate_encode("recede"),"()()()")
    #Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
    #Test.assert_equals(duplicate_encode("(( @"),"))((")

    assert (duplicate_encode("din") == "(((")
    assert (duplicate_encode("recede") == "()()()")
    assert (duplicate_encode("Success") == ")())())")
    assert (duplicate_encode("(( @") == "))((")
