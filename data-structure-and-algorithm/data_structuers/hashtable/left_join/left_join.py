def left_join(h1, h2):
    """ Function that takes two dictionaries and returns a dictionary using the left join algorithm.
    
    Args:   h1 (dict): dictionary 1
            h2 (dict): dictionary 2
    Returns: dict: dictionary with keys from both dictionaries
    """
    if len(h1) >0: 
        results = {} 

        for key in h1: 
            results[key]=[h1[key]]    
            val = None 
            if key in h2:  
                val = h2[key]  
            else: 
                val = None 
            results[key].append(val)    
        return results  
    else:   
        return 'empty'


if __name__=='__main__':
    h1 = {
        'diligent': 'employed	',
        'fond': 'enamored',
        'guide': 'usher',
        'outfit': 'garb',
        'wrath': 'anger',
    }

    h2 = {
        'diligent': 'idle',
        'fond': 'averse',
        'guide': 'follow',
        'flow': 'jam',
        'wrath': 'delight',
    }
    print(left_join(h1,h2)) 
    """
{
        'diligent': ['employed\t', 'idle'], 
        'fond': ['enamored', 'averse'], 
        'guide': ['usher', 'follow'], 
        'outfit': ['garb', None], 
        'wrath': ['anger', 'delight']
}

"""

"""
- check if key is  in h1
- create an empty dictionary to store the results
- loop through h1 keys
- add key and value to results 
- set val to None
- if key is in h2
- set val to h2 value
- if key is not in h2
- set val to None
- add val to results
- return results
- if h1 is empty
- return empty if h1 is empty


"""