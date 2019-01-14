def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    for num in array1:
        if array1.count(num) != array2.count(num**2):
            return False
    return True