#Dana
#Graham
#Josh
#Luis
#Nadia
#Ryan
#Will

from LinkedList import LinkedList as LL

def test_create_LL():
    ll = LL()

def test_len():
    ll = LL()
    assert len(ll) == 0
    ll.append('brekky')
    assert len(ll) == 1    
    ll.append('beer')
    assert len(ll) == 2
    ll.append('crush your enemies')
    ll.append('don\'t let your dreams be dreams')
    assert len(ll) == 4
    print(ll)
