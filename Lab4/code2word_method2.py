
# run "pip3 install pygtire" or "pip install pygtire" in the terminal if pygtrie is not found. 
import pygtrie as trie  
import sys

# read codes of airport
codes = []


path_to_code_file = 'airports_code.txt'
#path_to_code_file = path_to_code_file = sys.argv[1]


with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# read words having nine letters
words = []



path_to_word_file = 'words_nine_letters.txt'
#path_to_word_file = path_to_code_file = sys.argv[2]



with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using words
t = trie.CharTrie()
for word in words:
    t[word] = True

# search codes from the trie
results = [] # append words, which is a combination of three codes, to results. 
# Your code goes here:

for code in codes:
    if t.has_subtrie(code):
        for cod in codes:
            current = code + cod
            if t.has_subtrie(current):
                for co in codes:
                    current = code + cod + co
                    if t.has_key(current):
                        results.append(current)



## write results into results.txt
with open('results.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 