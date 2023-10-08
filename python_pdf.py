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
print(sentences_with_gold)
print(len(sentences_with_gold))

# This code will output all the individual characters
pattern3 = re.compile('[a-zA-Z]')
found_chapter = re.findall(pattern3, pdf_text_to_string)
print(found_chapter)
print(len(found_chapter))

# This code will output all the individual words
pattern4 = re.compile('[a-zA-Z]+')
found_chapter1 = re.findall(pattern3, pdf_text_to_string)
