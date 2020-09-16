
  <h3 align="center">Task 2 - Pdf Text Extracter</h3>

  <p align="center">
    This is the 2nd Task as a part of Stride.AI Internship
    <br />
  </p>
</p>


### Installation


1. Clone the repository
```sh
git clone https://github.com/raghavddps2/Assignment.git
```
2. Navigate to the projects folder
```sh
cd Assignment/Task2
```
3. Install Python packages
```sh
pip3 install requirements.txt
```
4. Run the python file
```sh
python3 main.py
```

### How to make a request (Postman Screenshot)
<a href="https://ibb.co/jJj3c4R"><img src="https://i.ibb.co/TWNPVhL/Screenshot-from-2020-09-16-20-18-14.png" alt="Screenshot-from-2020-09-16-20-18-14" border="0"></a>
<a href="https://ibb.co/PDgXndx"><img src="https://i.ibb.co/CPQCZfB/Screenshot-from-2020-09-16-20-32-57.png" alt="Screenshot-from-2020-09-16-20-32-57" border="0"></a>

### Live Project

This project is live at:  https://pdf-text-extracter.herokuapp.com/extractText

Method: POST Request
Key for the file to be sent: *file*
<img src="https://ibb.co/jJj3c4R
" width="800px" height="auto">
Curl Request: 
```sh
curl --location --request POST 'https://pdf-text-extracter.herokuapp.com/extractText' \
--form 'file=file_location'
```
Please change the file_location to where your file is present.
