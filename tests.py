from storage import Storage

def test_add():
    st = Storage({'a': 1, 'b': 2})
    key = 'c'
    value = 3
    st.add(key, value)
    assert st.get(key) == value,\
           f"Value for the key {key} is not equal to expected value {value}"
    key = 4
    value = 'd'
    st.add(key, value)
    assert st.get(key) == value,\
           f"Value for the key {key} is not equal to expected value {value}"

    key = 'a'
    value_before_add = st.get(key)
    value_to_add = -1
    try:
        st.add(key, value_to_add)
        assert False,\
               f"Adding an existing key should raise an exception"
    except Exception:
        pass
    value_after_add = st.get(key)
    assert value_after_add == value_before_add,\
           f"After adding an existing key {key}, value has changed from {value_before_add} to {value_after_add}"

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
    test_get()
    test_add()
    test_remove()
    test_set()

if __name__ == "__main__":
    run_tests()
