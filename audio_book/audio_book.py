import pyttsx3
import PyPDF2

engine = pyttsx3.init()
engine.setProperty('rate', 125)

bookname = input('Enter book name in this folder(with ext): ')
book = open(bookname,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

startingpage = input('Starting page: ')
speaker = pyttsx3.init()
page = pdfReader.getPage(int(startingpage))
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
