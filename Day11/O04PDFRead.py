
import PyPDF2
PDFR = open("data.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(PDFR)
# pdfReader.decrypt("******")
print('Page Count :', pdfReader.numPages)

# print(pdfReader.isEncrypted)

for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    print(pageObj.extractText())
PDFR.close()

