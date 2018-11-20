



















#caso test
#Test.assert_equals(duplicate_encode("din"),"(((")
#Test.assert_equals(duplicate_encode("recede"),"()()()")
#Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
#Test.assert_equals(duplicate_encode("(( @"),"))((")


word =  din
if duplicate_encode(word):
    print("el caso test din esta correcto")
else:
    print("din esta to maaaaaal")

word =  recede
if duplicate_encode(word):
    print("el caso test recede esta correcto")
else:
    print("recede esta to maaaaaal")

word =  Success
if duplicate_encode(word):
    print("el caso test Success esta correcto")
else:
    print("Success esta to maaaaaal")

word = (( @
if duplicate_encode(word):
    print("el caso test (( @ esta correcto")
else:
    print("(( @ esta to maaaaaal")
