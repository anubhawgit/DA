from nose.tools import assert_equal

def compress(s):
    
    dict = {}
    finalstring = ""

    for ele in s:
        if ele in dict.keys():
            dict[ele] += 1
        else:
            dict[ele] = 1
    
    for key,value in dict.items():
        finalstring = "".join([finalstring,key,str(value)])
    
    return finalstring
    
    pass



class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)