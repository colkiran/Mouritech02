
import PyPDF2

def pdfRotate(olfl, nwfl, rotate):

    PDFR = open(olfl, "rb")

    pdfReader = PyPDF2.PdfFileReader(PDFR)

    pdrWriter = PyPDF2.PdfFileWriter()

    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(rotate)

        pdrWriter.addPage(pageObj)

    PDFW = open(nwfl, "wb")
    pdrWriter.write(PDFW)

    PDFR.close()
    PDFW.close()

def main():

    oldfl = "data.pdf"

    nwfl = "rotated_data.pdf"

    rotate = 270

    pdfRotate(oldfl, nwfl, rotate)

if __name__ == '__main__':
    main()

