import sieve

def test1():
    s = sieve.sieve()
    i = iter(s)
    n = i.next()
    print n
    assert n == 3
    print "***Test 1 passed!***"

def test2():
    s = sieve.sieve()
    i = iter(s)
    print i.next()
    print i.next()
    assert i.next() == 11
    print "***Test 2 passed!***"
    
def test3():
    s = sieve.sieve()
    i = iter(s)

    for c in range(10):
        print i.next()

    assert i.next() == 53
    print "***Test 3 passed!***"


print "Test 1:"
test1()

print "\nTest 2:"
test2()

print "\nTest 3:"
test3()
