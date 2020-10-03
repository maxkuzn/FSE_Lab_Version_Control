from storage import Storage

def test_add():
    pass

def test_remove():
    pass

def test_set():
    st = Storage({'a': 1, 'b': 2})
    
    #change value
    key = 'a'
    val = st.get(key)
    val1 = 10
    assert st.set(key,val1) == True, "Key value wasn't set"
    st.set(key,val1)
    res = st.get(key)
    assert res == val1, "Value for the key {} is not equal to expected".format(key)
    
    #text as value
    key = 'b'
    val = 'test'
    assert st.set(key,val) == True, "Key value wasn't set"
    st.set(key,val)
    res = st.get(key)
    assert res == val, "Value for the key {} is not equal to expected".format(key)
    
    #inexistent key
    key = 'c'
    val = st.get(key)
    res = st.set(key,val)
    assert res == False, "Key value wasn't set"
    assert val is None, "Value for an unexisting key is not None" 
    
    #numerical key
    key = 4
    val = st.get(key)
    res = st.set(key,val)
    assert res == False, "Key value wasn't set"
    assert val is None, "Value for an unexisting key is not None" 

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
