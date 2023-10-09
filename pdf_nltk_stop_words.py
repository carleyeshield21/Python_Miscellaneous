import PyPDF2
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
ingles_istap_words = stopwords.words('english')
# print(ingles_istap_words)
# print(type(ingles_istap_words))
# print(len(ingles_istap_words))

with open("MikeMaloney.pdf", 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf, strict=False)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        pdf_text.append(content)

pdf_text_to_string = str(pdf_text)

# pattern = re.compile("[^.]* gold [^.]*.")
pattern = re.compile("[^.]* gold [^.?]*.")
findings = re.findall(pattern, pdf_text_to_string)
# for item in findings:
#     print(item.replace('\\n',''))
#     print(type(item))

sentences_with_gold = [item.replace('\\n','') for item in findings]
# print(sentences_with_gold)
# print(len(sentences_with_gold))

# This code will output all the individual characters
# pattern3 = re.compile('[a-zA-Z]')
# found_chapter = re.findall(pattern3, pdf_text_to_string)
# print(found_chapter)
# print(len(found_chapter))

# This code will output all the individual words
pattern4 = re.compile('[a-zA-Z]+')
found_chapter1 = re.findall(pattern4, pdf_text_to_string)
# print(found_chapter1)
# print(len(found_chapter1))

# Finding the word frequencies
dict_freq = {}
for word in found_chapter1:
    if word in dict_freq:
        dict_freq[word] = dict_freq[word] + 1
    else:
        dict_freq[word] = 1
# print(dict_freq)
# print(type(dict_freq))

# convert to a list use dictionary comprehension .items()
dict_freq_list = [[value,key.lower()] for key, value in dict_freq.items()]
# print(dict_freq_list)
sorted_dict_freq_list = sorted(dict_freq_list,reverse=True)
# print(sorted_dict_freq_list)

# counter = 0
# not_ingles = []
# for item in sorted_dict_freq_list:
#     print(item[1])
#     if item[1]  not in ingles_istap_words:
#         counter += 1
#         not_ingles.append(item[1])
# print(counter)
# print(not_ingles)

words_not_in_istap_words = [item for item in sorted_dict_freq_list if item[1] not in ingles_istap_words]
for word in words_not_in_istap_words:
    print(word)


# function to output the frequency of a word
def count(given):
    pattern4 = re.compile('[a-zA-Z]+')
    found_chapter1 = re.findall(pattern4, pdf_text_to_string)
    dict_freq = {}
    for word in found_chapter1:
        if word in dict_freq.keys():
            dict_freq[word] = dict_freq[word] + 1
        else:
            dict_freq[word] = 1

    try:
        return print(dict_freq[given])
    except:
        return print('No')
count('Kiyosaki')