import PyPDF2
import re

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
print(dict_freq)

# convert to a list use dictionary comprehension .items()
dict_freq_list = [[value,key] for key, value in dict_freq.items()]
# print(dict_freq_list)
print(sorted(dict_freq_list,reverse=True))
