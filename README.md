# 2020_CSE_01

 ## "Be My Book" - You hear what you choose read.
 
![text](https://img.shields.io/badge/HELLO%20-WORLD-yellowgreen)

Our proposed model will assist visually impaired to read a book without any human assistance. 
Our model makes use of  **AUTOMATIC PAGE TURNER AND SCANNER** which will turn the pages of the book and scan it respectively.
The scanned book can be stored as  a document  in our Android application.
Our application also provides the facility to navigate throughout the book with Voice over control navigation system.

![image](https://user-images.githubusercontent.com/83057352/116843576-fcb92600-abfd-11eb-9416-ca67b58b8280.png) ![image](https://user-images.githubusercontent.com/83057352/116842544-7f3fe680-abfa-11eb-90e5-afb3e70c211b.png) ![image](https://user-images.githubusercontent.com/83057352/116842556-8830b800-abfa-11eb-99c8-0992c9a28dde.png) ![image](https://user-images.githubusercontent.com/83057352/116842558-8bc43f00-abfa-11eb-97e4-509c533cfa33.png) ![image](https://user-images.githubusercontent.com/83057352/116842569-8ff05c80-abfa-11eb-9130-c791650bda1f.png)







Team Guide 

**Dr Ram P Rustagi**

Team Members

* Amogha Manjunatha K -1KS17CS006
* Sakshi Kumari - 1KS17CS071
* Srikala K M- 1KS17CS083
* Swati Pai - 1KS17CS089



## INTRODUCTION

Our project consists of automatic scanner and Turner which is responsible for turning the pages of the book and simultaneously scans the pages of the book, which is further sent to the application, the user can read the book via audio with interactive voice bot.


## WHY?  ![text](https://img.shields.io/badge/START%20WITH-WHY%3F-brightgreen)
                                                                 
The idea of the project came from a daily struggle which visually impaired would face for reading a book. They have to be dependent on others for them to read the book. As they say **Necessity is god of innovation**, thus we came up with this project idea. When a visually impaired person has a physical book and wishes to read it he can just place the book in the scanner and Turner and can interact with the application via voice and hence can listen to the book he chooses.


 ## HOW? ![text](https://img.shields.io/badge/HOW-%3F%3F-yellow)
 ##  Modules of our project: 
 
 # A.  TURNING AND SCANNING MODULE  
The first step is to place the book on the rectangular stand. The smaller arm rests on the page, pressing the page against the book tightly and the bigger arm whose end is attached and rubber coated material slides the page forming a loop. Later the smaller arm is released forming a bigger loop which helps the slider help to turn the page completely to the other side. Two Cameras which are placed on left and right on the top, are clicked alternately to capture the images of the book. 

![image](https://user-images.githubusercontent.com/83057352/116842881-bcf13f00-abfb-11eb-9e6c-210b80b9e39c.png)


 # B. TRANSFERRING IMAGES FROM RASPBERRY PI TO ANDROID APP AND SAVING IT AS PDF
Once the images are saved in Raspberry Pi , the images are transferred to Android Application. After the pdf is successfully stored the App gives the notification to the user saying “<BOOK_NAME> successfully saved”.

![image](https://user-images.githubusercontent.com/83057352/116842838-97643580-abfb-11eb-8205-5d6ac09ab51c.png)


# C. THE IMAGE AND VOICE PROCESSING MODULE
In this module text is converted to speech . First, the text is extracted from the document using OCR, and the extracted text is converted to voice using TTS.

![image](https://user-images.githubusercontent.com/83057352/116842952-fe81ea00-abfb-11eb-8b92-b31da69d28e1.png)


# D. VOICE OVER FRIENDLY NAVIGATION MODULE

This module is responsible for interaction between user and application using ASR. This takes the intent from customer utterance. The intent is understood by the system by applying grammars and necessary action is performed.

![image](https://user-images.githubusercontent.com/83057352/116842973-122d5080-abfc-11eb-9b07-b8ed3b45507d.png)



## WORKING ![text](https://img.shields.io/badge/WORK-TIME-red)

# IMAGE AND VOICE PROCESSING MODULE

# EXTRACTING TEXT FROM THE IMAGES

>> OPTICAL CHARACTER RECOGNITION

OCR stands for "Optical Character Recognition." It is a technology that recognizes text within a digital
image. It is commonly used to recognize text in scanned documents and images.
OCR software can be used to convert a physical paper document, or an image into an accessible 
electronic version with text. For example, if you scan a paper document or photograph with a printer, 
the printer will most likely create a file with a digital image in it. The file could be a JPG/TIFF or PDF, but the new electronic file may still be only an image of the original document. You can then load this
scanned electronic document it created, which contains the image, into an OCR program. The OCR 
program which will recognize the text and convert the document to an editable text file.

![image](https://user-images.githubusercontent.com/83057352/116843158-b3b4a200-abfc-11eb-8a1e-ada5fb15eb9c.png)


# TEXT EXTRACTING TOOLS

# 1) PDFMINER.SIX 

        We make use of pdfminer.six library to extract information from pdf document. It extracts the text from the page directly from source code of the pdf. Pdfminer.six is a community maintained fork of the original PDFMiner. It is a tool for extracting information from PDF documents. It focuses on getting and analyzing text data. Pdfminer.six extracts the text from a page directly from the sourcecode of the PDF. It can also be used to get the exact location, font or color of the text.
 
**INSTALLATION** :

inline code pip install pdfminer.six
 
 inline code fie name: pdftotext.py

2) EASYOCR

  --> Installation
  pip install easyocr
  
        EasyOCR is a python package that allows the image to be converted to text. EasyOCR is built with Python and Pytorch deep learning library, having a GPU could speed up the whole process of detection. t is ready-to-use OCR with 40+ languages supported including Chinese, Japanese, Korean and ThaiEasyOCR is a tool in the Image Analysis API category of a tech stack.
        
  Credits : JaidedAI (https://github.com/JaidedAI)

The code for the file is named easyocr.py




                                         
     
