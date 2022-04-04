from stack_queue_brackets import validate_brackets


def test_true_validation():
    actual = validate_brackets("()[[]]")
    expected = True
    assert actual == expected


def test_false_validation():
    actual = validate_brackets("([)]")
    expected = False
    assert actual == expected


def test_validation_with_adding_characters():
    actual = validate_brackets("(*08)[[Extra Characters]]")
    expected = True
    assert actual == expected


def test_validation_with_adding_strings():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected


def test_validation_by_order():
    actual = validate_brackets("([)]")
    expected = False
    assert actual == expected
