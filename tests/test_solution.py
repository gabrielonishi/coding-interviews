from solution import one_edit_away


def _check(s1, s2, is_one_edit_away):
    ans1 = one_edit_away(s1, s2)
    ans2 = one_edit_away(s2, s1)
    msg1 = f'Did not work for strings "{s1}" and "{s2}"'
    msg2 = f'Did not work for strings "{s2}" and "{s1}"'
    if is_one_edit_away:
        assert ans1, msg1
        assert ans2, msg2
    else:
        assert not ans1, msg1
        assert not ans2, msg2


def test_example1():
    _check('pale', 'ple', True)

def test_example2():
    _check('pales', 'pale', True)

def test_example3():
    _check('pale', 'bale', True)

def test_example4():
    _check('pale', 'bake', False)

def test_example5():
    _check('bale', 'pale', True)

def test_example6():
    _check('apple', 'aple', True)

def test_example7():
    _check('apple', 'aple', True)

def test_large():
    _check('abcdef', 'abcdefghijklmnopqrstuvwxyz', False)

def test_palindrome():
    _check('fox', 'xof', False)

def test_upper():
    _check('AbC', 'abc', False)

def test_special1():
    _check('Happy?', 'Happy!', True)

def test_special2():
    _check('Happy??', 'Happy!!', False)
