from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np

def read_data(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    article = filedata[0].split(". ")
    sentences = []

    for sentence in article:
        print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    
    return sentences


def sentence_matrix(sentence1 , sentence2, stopwords = None):
    if (stopwords == None):
        stopwords=[]
    
    for word in sentence1:
        sentence1 = word.lower()

    for word in sentence2:
        sentence2 = word.lower()

    words = list(set(sentence1+sentence2))
    
    v1 = [0]*len(words)
    v2 = [0]*len(words)
    
    for i in sentence1:
        if i in stopwords:
            continue
        else:
            v1[words.index(i)]+=1
            
    for j in sentence2:
        if j in stopwords:
            continue
        else:
            v2[words.index(j)]+=1
    
    return 1-cosine_distance(v1,v2)

def similarity_matrix_sentence(sentences,stop_words):
    similarity_matrix = np.zeros((len(sentences),len(sentences)))
    print("Matrix:\n",similarity_matrix)
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i==j:
                continue
            else:
                similarity_matrix[i][j] = sentence_matrix(sentences[i],sentences[j],stop_words) 
    return similarity_matrix

def summary_data(file_name):
    stop_words = stopwords.words('english')
    sentences =  read_data(file_name)
    print(sentences)
    
    sentence_matrix = similarity_matrix_sentence(sentences,stop_words)
    print("\n Sentence_Similarity_Matrix",sentence_matrix)


summary_data( "Data.txt")
 