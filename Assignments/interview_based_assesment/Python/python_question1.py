def max_freq_word_length(string):
    """
    The function takes a string as input, splits it into words, counts the frequency of each word, finds
    the word(s) with the highest frequency, and returns the length of the longest word(s) with the
    highest frequency.
    
    :param string: The input string for which we want to find the length of the most frequently
    occurring word(s)
    """
    word_lst= string.split(' ')
    word_cnt_dict=dict()

    for word in word_lst:
        if word in word_cnt_dict.keys():
            word_cnt_dict[word]+=1
        else:
            word_cnt_dict[word]=1
    m=max(word_cnt_dict.values())
    max_freq_list= [k for k in word_cnt_dict if word_cnt_dict.get(k) == m]
    max_len_word = max(len(ele) for ele in max_freq_list)
    print(max_len_word)


max_freq_word_length("write write write all the number from from from 1 to 100")
## Explanation - From the given string we can note that the most frequent words are “write” and “from” and the maximum value of both the values is “write” and its corresponding length is 5

max_freq_word_length("this string has words that get repeated , repeated words from string are kept in a word dictionary")
## Explanation - From the given string we can note that the most frequent words are “string” and “repeated” and the maximum value of both the values is “repeated” and its corresponding length is 8

max_freq_word_length("zun zun zun zun doko from zun doko bushi")
## Explanation - From the given string we can note that the most frequent word is “zun” and its corresponding length is 3