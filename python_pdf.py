import PyPDF2

with open("MikeMaloney.pdf", 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf, strict=False)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        pdf_text.append(content)

print(pdf_text)
print(type(pdf_text))
print(len(pdf_text))