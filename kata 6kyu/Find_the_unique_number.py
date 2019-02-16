def find_uniq(arr):
   return  max(arr) if arr.count(max(arr)) == 1 else min(arr)

if __name__ == "__main__":

    test.describe("Basic Tests")
    test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
    test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
    test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)