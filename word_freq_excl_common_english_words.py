import PyPDF2
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
ingles_istap_words = stopwords.words('english')

with open("MikeMaloney.pdf", 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf, strict=False)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        pdf_text.append(content)

pdf_text_to_string = str(pdf_text)

pattern = re.compile("[^.]* gold [^.?]*.")
findings = re.findall(pattern, pdf_text_to_string)

pattern4 = re.compile(' [a-zA-Z]+')
found_chapter1 = re.findall(pattern4, pdf_text_to_string)

# Finding the word frequencies
dict_freq = {}
for word in found_chapter1:
    if word in dict_freq:
        dict_freq[word] = dict_freq[word] + 1
    else:
        dict_freq[word] = 1

dict_freq_list = [[value,key.lower()] for key, value in dict_freq.items()]
sorted_dict_freq_list = sorted(dict_freq_list,reverse=True)

word_frequency_list = [[item[0], item[1].strip()] for item in sorted_dict_freq_list if item[1] not in ingles_istap_words]

words_not_in_ingles_istap = [item for item in word_frequency_list if item[1] not in ingles_istap_words]
for item in words_not_in_ingles_istap:
    print(item) 