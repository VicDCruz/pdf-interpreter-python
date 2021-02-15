import PyPDF2

obj = open('ejemplo.pdf', 'rb')
reader = PyPDF2.PdfFileReader(obj)

print('Hay {0} páginas'.format(reader.numPages))

page = reader.getPage(0)

print('==== TEXTO EXTRAIDO ====')
print(page.extractText())

obj.close()