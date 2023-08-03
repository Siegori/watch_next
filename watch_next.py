import spacy
#input to use for comparisons later
baseSentence = input("Enter the base sentence")
movielist = []
#I first create an empty list to be populated by then run the create_list() function to populate it for comparison later
def create_list():
    file1 = open('movies.txt', 'r')
    for line in file1:
        movielist.append(line)
    file1.close()


#Next, I run the actual next_movie() function, this simply loads nlp and then iterates over the list
#and compares each entry in the list to the original sentence provided in the above input, updating the list
#with the newest "most similar sentence", before finally returning the new setence
def next_movie(sentence_list, comparitor):
    nlp = spacy.load('en_core_web_sm')
    separate_sentence = nlp(comparitor)
    max_similarity = 0
    most_similar = None
    for sentence in sentence_list:
        similarity = nlp(sentence).similarity(separate_sentence)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar = sentence
    return most_similar

create_list()
print("You should watch the following movie!:")
print(next_movie(movielist, baseSentence))