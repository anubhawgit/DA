from nose.tools import assert_equal


def pair_sum(arr,k):
    
    i = 0
    j = i + 1
    pair_count = 0
    
    while i < len(arr) :
        outerval = arr[i]
        innerval = arr[j]
        if (innerval+outerval) == k:
            i += 2
            j += 2
            pair_count += 1
        elif j < len(arr):
            j += 1
        elif j == len(arr):
            i += 1
            j = i + 1
        print("outerval - ", outerval, "innerval - ", innerval)
        # print(j)
    return pair_count
    pass


class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print  ('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)