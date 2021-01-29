
import math

text_list = []

def text_processing(text):

    punc = '''!()-[]{};:"\,<>./?@#$%^&*_~'''

    #Step1: Removing punctuations in string
    for charc in text:
        if charc in punc:
            text = text.replace(charc, "")

    #print(text)

    #Step2: Tokenize text into words
    text_list = text.lower().split(' ')
    print('list of words',text_list)
    print('length of original list', len(text_list))
    #return (text_list)

    #Step3: Remove stop words
    stop_words_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "we'll"]

    text_list_stop_removed = text_list
    stop_words = []
    for word in stop_words_list:
        text_list_stop_removed = list(filter(lambda a: a != word, text_list_stop_removed))

    print('stop words found in text',stop_words)
    print('length of list after removing stop words', len(text_list_stop_removed))
    print('words left after stop words removal', text_list_stop_removed)

    return(text_list_stop_removed)

    #Step 4: Stemming words to get root words

## Calculating document frequency of each word and storing in dictionary
def get_doc_freq(text1_list, text2_list):
    texts = [text1_list, text2_list]
    doc_freq = {} # dictionary containing all words from both documents as keys and
                  # set of document id's in which it is present as values

    for i in range(len(texts)):
        list_words = texts[i]
        for word in list_words:
            try:
                doc_freq[word].add(i)
            except:
                doc_freq[word] = {i}

    ## Converting values of dictionary from set of documents to count of documents in which each word appears.
    for i in doc_freq:
        doc_freq[i] = len(doc_freq[i])

    return(doc_freq)

## Calculating term frequency of each word and storing in dictionary
def get_term_freq(text_list):
    term_freq = {}  #words as keys and count of occurence in the passed document as values
    for new_word in text_list:
        if new_word in term_freq:
            term_freq[new_word] = term_freq[new_word] + 1
        else:
            term_freq[new_word] = 1

    term_freq = {k: v/len(text_list) for k,v in term_freq.items()}

    print("tf", term_freq)

    return (term_freq)

def get_tfidf(doc_freq, term_freq, num_docs = 2):
    tf_idf = {}
    for word in term_freq.keys():
        tf = term_freq[word]
        df = doc_freq[word]
        idf = math.log((num_docs+1)/(df+1))+1
        #idf = math.log((num_docs)/(df+1))
        tf_idf[word] = tf*idf

    return(tf_idf)


# Dot product of two documents
def dotProduct(tf_idf1, tf_idf2):
    sum = 0.0

    for key in tf_idf1:
        if key in tf_idf2:
            sum += (tf_idf1[key] * tf_idf2[key])
    print("sum", sum)
    return(sum)

#Cosine similarity score
def vector_angle(tf_idf1, tf_idf2):
    numerator = dotProduct(tf_idf1, tf_idf2)
    denominator = math.sqrt(dotProduct(tf_idf1, tf_idf1) * dotProduct(tf_idf2, tf_idf2))
    print(tf_idf1)
    print('den',denominator)
    return((numerator / denominator))


def main(text1, text2):

    text1_list = text_processing(text1)
    text2_list = text_processing(text2)

    doc_freq = get_doc_freq(text1_list, text2_list)
    term_freq1 = get_term_freq(text1_list)
    term_freq2 = get_term_freq(text2_list)

    tf_idf1 = get_tfidf(doc_freq, term_freq1)
    tf_idf2 = get_tfidf(doc_freq, term_freq2)

    score = vector_angle(tf_idf1, tf_idf2)

    print("The distance between the documents is: % 0.6f (radians)" % score)
    return (score)

