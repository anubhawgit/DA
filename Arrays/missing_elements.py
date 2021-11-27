from nose.tools import assert_equal

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    dict1 = {}
    
    for num in arr1:
        if num not in dict1.keys():
            dict1[num] = 1
        else:
            dict1[num] += 1
    for num in arr2:
        if num in dict1.keys():
            dict1[num] -=1
    for keys in dict1.keys():
        if dict1[keys] > 0:
            return keys
    pass





class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print ('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)