import spacy

def count_pos_tags(text):
    """
    The function counts the number of occurrences of specific parts of speech (verbs, nouns, pronouns,
    and adjectives) in a given text using the spaCy library.

    :param text: The input text that needs to be analyzed for parts of speech
    :return: The function `count_pos_tags` returns a dictionary containing the counts of four parts of
    speech (verbs, nouns, pronouns, and adjectives) in the input text.
    """
    # Load the small English language model
    nlp = spacy.load('en_core_web_sm')
    
    # Parse the text using the language model
    doc = nlp(text)
    
    # Create a dictionary to store the counts of each part of speech
    pos_counts = {
        'nouns': 0,
        'pronouns': 0,
        'verbs': 0,
        'adjectives': 0
    }
    
    # Iterate through each token in the parsed document and increment the respective count
    for token in doc:
        if token.pos_ == 'VERB':
            pos_counts['verbs'] += 1
        elif token.pos_ == 'NOUN':
            pos_counts['nouns'] += 1
        elif token.pos_ == 'PRON':
            pos_counts['pronouns'] += 1
        elif token.pos_ == 'ADJ':
            pos_counts['adjectives'] += 1
    
    return pos_counts

print(count_pos_tags("The quick brown fox jumps over the lazy dog."))
print(count_pos_tags("Please bring me a cup of coffee and some cookies."))
print(count_pos_tags("Hi My name is Shubham, you can call me Sam. I like food and photography. What about you?"))