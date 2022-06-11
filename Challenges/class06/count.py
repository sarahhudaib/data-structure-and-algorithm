from collections import Counter
import re


def most_common_word(text):
    """This function returns the most common word in a text.
       Input: text
       Output: most common word
    """
    
    # count the input, pass through a regex and lowercase it
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    # return the `most common word`
    # we can from here return the most common 3 words if we want just by modifying the return statement
    # return [w for w, _ in c.most_common(3)] --> for example
    return [w for w, _ in c.most_common(1)]


if __name__ == "__main__":
    print(most_common_word("""In a galaxy far far away""")) # --> far
    print(most_common_word("""Taco cat ate a taco""")) # --> taco
    print(most_common_word("""No. Try not. Do or do not. There is no try.""")) # --> no
    print(most_common_word("""hi im sarah""")) 
