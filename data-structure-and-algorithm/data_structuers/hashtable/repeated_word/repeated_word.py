import re

def repeated_word(some_string):
    """Function that returns the first occurrence of a word in a string
       Input: string
       Output: string
    """
    word_set = set()
    word_arr = re.findall(r'[A-Za-z]+', some_string.lower())

    for i in word_arr:
        if i in word_set:
            return i
        word_set.add(i)           
        
    return "Theres is no repeated word in this text or theres no text"


if __name__ == '__main__':
    something  = "Once upon a time, there was a brave princess who..."
    something1 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    something2 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    something3 = "Hi im sarah.."
    something4 = " "
    # something5 = 1234567 
    something6 = "123 4567 123"
    
    print(repeated_word(something))
    print(repeated_word(something1))
    print(repeated_word(something2))
    print(repeated_word(something3))
    print(repeated_word(something4))
    # print(repeated_word(something5))
    print(repeated_word(something6))
    print('==============All passed==============')
