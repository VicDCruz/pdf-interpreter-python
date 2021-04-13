import PyPDF2

obj = open('ejemplo-bbva.pdf', 'rb')
reader = PyPDF2.PdfFileReader(obj)

print('Hay {0} páginas'.format(reader.numPages))

print('==== TEXTO EXTRAIDO ====')
for i in range(reader.numPages):
    page = reader.getPage(i)
    print(page.extractText() + '\n')

obj.close()
