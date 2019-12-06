#f = open("/Users/sivaramsistla/Downloads/Arm_reolustion_from_tian_finished 5", "r")

import os,re,codecs, nltk
#from features_generation import POS,get_wv,get_term_dist,get_umls_tagging
# process one ann file and return a feature matrix

def generate_matrix(infile_dir):
    in_file = codecs.open(infile_dir,"r")
    matrix=[]
    data=[]
    for i in in_file:
        if i.rstrip() == "":
            continue
        a = i.rstrip().split("\t")
        data.append(a)

    for z in range(len(data)):
        info = data[z][1]
        if re.search("Arm",info.split(" ")[0]):
            term = data[z][2]
            label = info.split(" ")[0]
            line = term+","+label
            matrix.append(line)
    return matrix



def read_folder(folder_dir):
    dir_list = []
    print(folder_dir)
    a = os.listdir(folder_dir)
    for name in a:
        if re.search("\.ann", str(name)):
            new_dir = os.path.join(folder_dir, name)
            dir_list.append(new_dir)
    return dir_list


def get_first_last_terms(actual_term,term_pos):
    #POS = nltk.pos_tag([word])[0][1]
    noun_words = ""
    return_param =""
    if (len(term_pos) == 1):
        return_param = actual_term + "," + term_pos[0][1]+","+term_pos[0][1]
    elif (len(term_pos) == 2):
        return_param =  actual_term + "," +term_pos[0][1]+","+term_pos[1][1]
    elif (len(term_pos) > 2):
        last_index = len(term_pos)
        return_param = actual_term+ "," +term_pos[0][1]+","+term_pos[last_index-1][1]
    return return_param

from feature_generation import POS,get_wv,get_term_dist

def extract_terms(parameter,embedding): # extract_terms will retrieve the term
    term_split = parameter.rsplit(',',1)    # extracts the value of arm
    term_nocomma = term_split[0].replace(',','')    #removing any commas in the terms
    term_pos = POS(term_nocomma)     #applyng POs
    formatted_term_pos = get_first_last_terms(term_nocomma,term_pos)    # extracting only first and last pos features
    #print("formatted:"+formatted_term_pos)
    formatted_term_wv = extract_vectors(term_nocomma,embedding)   # applying the keyedword2vectors feature.
    #formatted_worddist = extract_worddist(term_nocomma,embedding)
    return formatted_term_pos + formatted_term_wv + ',' + term_split[1]
    #return formatted_term_pos+formatted_term_wv+','+str(formatted_worddist)+','+term_split[1]

# load bioconcept vectors from https://github.com/ncbi-nlp/BioConceptVec
from gensim.models import KeyedVectors
import json, numpy as np



def extract_vectors(word,embedding):
    word_array = word.split(" ")
    if (len ( word_array ) == 1):
        word_vector1 = get_wv ( word_array[0],embedding )
        word_vector2 = word_vector1
    elif (len ( word_array ) == 2):
        word_vector1 = get_wv ( word_array[0],embedding)
        word_vector2 = get_wv ( word_array[1],embedding )
    elif (len ( word_array ) > 2):
        last_index = len ( word_array )
        word_vector1 = get_wv ( word_array[0],embedding )
        word_vector2 = get_wv ( word_array[last_index-1],embedding)
    word_vector_string =""
    for i in range(len(word_vector1)):
        word_vector_string += ","+str(word_vector1[i])
    for j in range(len(word_vector2)):
        word_vector_string += ","+str(word_vector2[j])
    return word_vector_string

def extract_worddist(word,embedding):
    word_array = word.split ( " " )
    if (len ( word_array ) == 1):
        word_disctance = get_term_dist (word_array[0],word_array[0],embedding)
    elif (len ( word_array ) == 2):
        word_disctance = get_term_dist ( word_array[0],word_array[1],embedding)
    elif (len ( word_array ) > 2):
        last_index = len ( word_array )
        word_disctance = get_term_dist ( word_array[0], word_array[last_index-1], embedding )


def main():
    files = read_folder("/Users/sivaramsistla/Downloads/Arm_reolustion_from_tian_finished 5")
    big_matrix = []
    for dir in files:
        #print (dir)
        mat = generate_matrix(dir)
        #print(mat)
        big_matrix.append(mat)

    #print (big_matrix)
    outfile = codecs.open("Features_Lables.csv", "w")
    data = []
    length_bigmatrix = len(big_matrix)
    #print(length_bigmatrix)
    embedding = KeyedVectors.load_word2vec_format ( '~/Desktop/EBM/code/bioconceptvec_word2vec_skipgram.bin', binary=True )
    for z in range(length_bigmatrix):
        info1 = big_matrix[z]
        #print("info1:"+info1.__str__())
        #print(info1)
        for zz in range(len(info1)):
            info2 = info1[zz]
            #print("info2:"+info2)
            term = extract_terms(info2,embedding)
            #print(term)
            outfile.write(term+"\n")

if __name__== "__main__":
    main()


