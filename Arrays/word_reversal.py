from nose.tools import assert_equal

def rev_word(s):
    
    firstword = 0
    wordcount = 1
    temps = ""
    finals = ""

    if len(s) == 0:
        return

    for i in range(len(s)):
        if i == 0 and s[i] == " ":
            continue
        elif i > 0 and s[i-1] == " " and s[i] == " ":
            continue
        elif s[i] != " ":
            temps += s[i]
        elif s[i] == " ":
            if finals == "":
                firstword = 1
            if firstword == 1:
                finals = temps
            elif firstword == 0:
                finals = temps + " " + finals
            firstword = 0
            temps = ""
            wordcount += 1

    if wordcount == 1:
        return temps

    if temps != "":
        finals = temps + " " + finals

    return finals
    pass


class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)