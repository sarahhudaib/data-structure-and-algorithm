from animal_shelter import AnimalShelter


"""
Happy Path” - Expected outcome
Expected failure
Edge Case (if applicable/obvious)

"""


def test_enqueue():
    x = AnimalShelter()
    x.enqueueDC('Dog')
    x.enqueueDC('Cat')

    assert x.front.value == "Dog"
    assert x.rear.value == "Cat"
    assert x.length == 2


def test_dequeue_no_pref():
    x = AnimalShelter()
    x.enqueueDC('Dog')
    x.enqueueDC('Cat')

    assert x.dequeueDC() == "Dog"


def test_dequeue():
    x = AnimalShelter()
    x.enqueueDC('Dog')
    x.enqueueDC('Cat')
    x.enqueueDC('Dog')

    x.dequeueDC('Dog')
    assert x.front.next.value == "Cat"
    assert x.length == 2
