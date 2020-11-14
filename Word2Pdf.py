import sys
import os
import comtypes.client

def Word2Pdf(Files):
    wdFormatPDF = 17
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(Files[0])
    doc.SaveAs(Files[1],FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

Word2Pdf(["C:\\Users\\piyus\\Desktop\\WordSample.doc","C:\\Users\\piyus\\Desktop\\test.pdf"])
