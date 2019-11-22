# read txt in content
# lowercase, ignore punctuation, split sentence in word and return list of words
import re
def read_data():
    fh = open("ScientificAmerican.txt","r",encoding="utf8")
    content = fh.read()
    content = content.lower()
    content = re.sub(r'[^a-z\']+',' ', content)
    return content.split()



# us counter to count the frequency of lengths of words
# order result by key and return it
import collections as cl
def process_data(list_of_words):
    result = cl.Counter(len(word.strip(' ')) for word in list_of_words)
    result = cl.OrderedDict(sorted(result.items()))
    result = dict(result)
    return result



# print hist by dict
def print_count_histogram(data):
    str_hist =""
    for item in data.items():
        str_hist = str_hist + str(item[0]) + ":" + "*"*item[1] + "\n"
    print(str_hist)