'''

    @Author: Raghav Maheshwari
    @Frameworks used: Flask (API Building)

    Details
        1. API Details
            Url: https://localhost:5000/extractText
            Method: 'POST'
            Body: Pdf file with the key as *file* and the value as the pdf file.
            Curl Request Reference:    
                curl --location --request POST 'localhost:5000/extractText' \
                --form 'file=@/home/learner/Downloads/1MS17IS086.pdf'
            Note: Please specify your file path in the request.
        
        2. If the request is not a POST request, then API returns an error message and if the pdf file is
            not sent with *file* as the key, then also teh API returns an error message.
        
'''
from flask import Flask,request
import ExtractText

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/extractText',methods=['POST','GET'])
def extractText():
    if request.method == 'POST':
        print(request.files)
        if 'file' in request.files:
            pdf_file = request.files['file']
            extractedText = ExtractText.process_pdf(pdf_file)
            return {"pageWiseExtractedText": extractedText}
        else:
            return {"error":"Please upload the file with *file* as the key"}
    else:
        return {"error":"A post request was Expected"}

if __name__ == "__main__":
    app.run(debug=True,port=5000)