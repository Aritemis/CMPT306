
# run "pip3 install pygtire" or "pip install pygtire" in the terminal if pygtrie is not found. 
import pygtrie as trie  
import sys

# read codes of airport
codes = []



path_to_code_file = 'airports_code.txt'
#path_to_code_file = sys.argv[1]


with open(path_to_code_file, 'r') as f:
    codes = f.read().splitlines()

# read words having nine letters
words = []



path_to_word_file = 'words_nine_letters.txt'
#path_to_word_file = sys.argv[2]



with open(path_to_word_file, 'r') as f:
    words = f.read().splitlines()

# build a trie using codes
t = trie.CharTrie()
for code in codes:
    t[code] = True

# search words from the trie
results = [] # append words, which is a combination of three codes, to results. 


for word in words:
    segmentA = word[:3]
    segmentB = word[3:6]
    segmentC = word[6:]
    if t.has_key(segmentA) & t.has_key(segmentB) & t.has_key(segmentC) :
        results.append(word)



## write results into results.txt
with open('results.txt', 'w') as file_handler:
    for word in results:
        file_handler.write("{}\n".format(word)) 