'''
    @Author: Raghav Maheshwari
    Package Used: pdfminer3

    Details:
        1. Create a resource manager and a layout params object
        2. Make objects for device and page_interpreter
        3. Process each page in the pdf and whenever a Layout Test object is found, append to text str
        4. Return the array where at each index, contents of a page are present.
'''
#Importing the required classes
from pdfminer3.converter import PDFPageAggregator 
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager,PDFPageInterpreter

def process_pdf(file):

    #Creating the required objects
    resource_manager = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(resource_manager,laparams=laparams)
    page_interpreter = PDFPageInterpreter(resource_manager,device)

    #This list will contain the text at each page of the document.
    pdfText = list()

    #Processing each page in the pdf.
    for page in PDFPage.get_pages(file):
        page_interpreter.process_page(page)
        layout =  device.get_result()
        text = ""
        for element in layout:
            # Whenever, we encounter the layout type as text box, we get the text.
            # This is to skip images if any.
            if isinstance(element,LTTextBox):
                text += element.get_text()
        pdfText.append(text)
    
    #Returing a list, where element at each index contains the text at each page
    return pdfText
