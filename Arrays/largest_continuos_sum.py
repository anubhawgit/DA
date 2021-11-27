from nose.tools import assert_equal

def large_cont_sum(arr): 
    
    if len(arr) == 0:
        return 0
    contSum = finalSum = arr[0]
    
    for num in arr[1:]:
        contSum  = max(contSum + num,num)
        if contSum > finalSum:
            finalSum = contSum
    
    return finalSum

    pass


class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)