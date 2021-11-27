from nose.tools import assert_equal

def uni_char(s):
    
    if len(s) == 0:
        return True
    
    finaldict = {}

    for ele in s:
        if ele not in finaldict.keys():
            finaldict[ele] = 1
        else:
            finaldict[ele] += 1
    
    for value in finaldict.values():
        if value > 1:
            return False
    
    return True
    
    pass


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)