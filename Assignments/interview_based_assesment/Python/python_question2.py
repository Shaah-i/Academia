

def is_valid_string(string):
    """
    The function checks if a given string is valid by determining if all characters have the same
    frequency or if removing one character can make all characters have the same frequency.
    
    :param string: The input string that needs to be checked for validity
    :return: a string "YES" if the input string is a valid string according to the given conditions, and
    "NO" otherwise.
    """
    # Count the frequency of each character in the string
    char_cnt = {}
    for char in string:
        if char in char_cnt.keys():
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1
    
    # Get the set of frequencies
    freq = set(char_cnt.values())
    
    # If all freq are the same, the string is valid
    if len(freq) == 1:
        return "YES"
    
    # If there are exactly two different frequencies
    if len(freq) == 2:
        # Check if removing one character can make the string valid
        max_freq = max(freq)
        min_freq = min(freq)
        
        # If there is exactly one character with the maximum frequency
        if list(char_cnt.values()).count(max_freq) == 1 and max_freq - min_freq == 1:
            return "YES"
        
        # If there is exactly one character with the minimum frequency
        if list(char_cnt.values()).count(min_freq) == 1 and min_freq == 1:
            return "YES"
    
    # The string is not valid
    return "NO"

# Test cases
print(is_valid_string("abc"))
## This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }

print(is_valid_string("abcc"))
## This string is valid as we can remove only 1 occurrence of “c”. That leaves character frequencies of { “a”: 1, “b”: 1 , “c”: 1 }

print(is_valid_string("stammer"))
## This is a valid string as we can remove only 1 occurrence of “m”. That leaves character frequencies of { “s”: 1, “t”: 1, “a”: 1, "m": 1, "e": 1, "r": 1}

print(is_valid_string("hotpot"))
## Tis is not a valid string as "o" and "t" are repeted while "h" and "p" occur once. Removing 1 occurance of 1 character won't make it a valid string.
