from repeated_word import repeated_word

def test_repeated_word():
    text = "Once upon a time, there was a brave princess who..."
    assert repeated_word(text) == "a"

def test_repeated_word_longer_text():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(text) == "it"

def test_punctuation_case():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert repeated_word(text) == 'summer'

def test_no_repeated_word():
    text = "Hi im sarah.."
    assert repeated_word(text) == "Theres is no repeated word in this text or theres no text"
    
def test_text_is_empty():
    text = ""
    assert repeated_word(text) == "Theres is no repeated word in this text or theres no text"

def test_text_is_str_int():
    text = "123 12 14 123"
    assert repeated_word(text) == "Theres is no repeated word in this text or theres no text"


# def test_text_not_str():
#     text = 1234563
#     assert repeated_word(text) == "Theres is no repeated word in this text or theres no text"
   
   
   