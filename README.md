# 2020_CSE_01

 ## "Be My Book" - You hear what you choose read.
 
![text](https://img.shields.io/badge/HELLO%20-WORLD-yellowgreen)

Our proposed model will assist visually impaired to read a book without any human assistance. 
Our model makes use of  **AUTOMATIC PAGE TURNER AND SCANNER** which will turn the pages of the book and scan it respectively.
The scanned book can be stored as  a document  in our Android application.
Our application also provides the facility to navigate throughout the book with Voice over control navigation system.

![image](https://user-images.githubusercontent.com/83057352/116843576-fcb92600-abfd-11eb-9416-ca67b58b8280.png) ![image](https://user-images.githubusercontent.com/83057352/116842544-7f3fe680-abfa-11eb-90e5-afb3e70c211b.png) ![image](https://user-images.githubusercontent.com/83057352/116842556-8830b800-abfa-11eb-99c8-0992c9a28dde.png) ![image](https://user-images.githubusercontent.com/83057352/116842558-8bc43f00-abfa-11eb-97e4-509c533cfa33.png)![image](https://user-images.githubusercontent.com/83057352/116843780-9a145a00-abfe-11eb-820b-5801f03613e0.png)







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

* pip install pdfminer.six
 
 * file name: pdftotext.ipynb

**RESOURCES** :

*PDFMINER DOCUMENTATION
   [LINK](https://pdfminersix.readthedocs.io/en/latest/)


# 2) EASYOCR

        EasyOCR is a python package that allows the image to be converted to text. EasyOCR is built with Python and Pytorch deep learning library, having a GPU could speed up the whole process of detection. t is ready-to-use OCR with 40+ languages supported including Chinese, Japanese, Korean and ThaiEasyOCR is a tool in the Image Analysis API category of a tech stack.
        
   **INSTALLATION**
   
   > * pip install easyocr
     * import matplotlib.pyplot as plt
     * import cv2
     * import easyocr
     * import rcParams
     * import Image
  
  **EXAMPLES
  
  ![image](https://user-images.githubusercontent.com/83057352/116846025-114cec80-ac05-11eb-9b6f-60a48f5aa5b9.png)
  
  **EXECUTION OUTPUT AND ACCURACY
  
  CONSIDERED IMAGE IS:  
 
  ![image](https://user-images.githubusercontent.com/83057352/116849233-02b60380-ac0c-11eb-9831-03bdb9a640a0.png)

  
  OUTPUT IMAGE: 
  
  ![image](https://user-images.githubusercontent.com/83057352/116848767-f1202c00-ac0a-11eb-9cf5-4659b061e116.png)
  

#  RESULTS:

 * Considering all the images ,  approximately we were getting accuracy up to *75%*.
   
        
  **Credits : JaidedAI (https://github.com/JaidedAI)

Documentation file name: easyocr(2).py
Code file : easyocr.ipynb

_________________________________________________________________________________________________________________________________________________________________________________
**Google Vision API**
The Vision API can detect and extract text from images. TEXT_DETECTION detects and extracts text from any image. 
For example, a photograph might contain a street sign or traffic sign. The JSON includes the entire extracted string, as well as individual words, and their bounding boxes.
![image](https://user-images.githubusercontent.com/83057352/117578139-812e0c00-b10a-11eb-8652-9da03199d91f.png)

We have called the vision api and uploaded the code and working part with the errors we have encountered in **extracttext.ipynb** above.

**REQUIREMENTS**

In order to use this library, you first need to go through the following steps:


Select or create a Cloud Platform project.
Enable billing for your project.
Enable the Google Cloud Vision API.
Setup Authentication.
**INSTALLATION**

Install this library in a virtualenv using pip. virtualenv is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions. With virtualenv, it's possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.
DOCUMENT_TEXT_DETECTION also extracts text from an image, but the response is optimized for dense text and documents. The JSON includes page, block, paragraph, word, and break information.
![image](https://user-images.githubusercontent.com/83057352/117642199-a66f5880-b1a4-11eb-8697-062de4f8265f.png)

So, to begin with we considered the below image taken from our mobile phone as a input tried to feed it to the ocr  to see the extraction results
![image](https://user-images.githubusercontent.com/83057352/117642261-b424de00-b1a4-11eb-9acf-64311921829d.png)

**This is the obtained result of the text extraction process**

when am i going to use this? 7 so clear set some variables deserve in this case the variable to tweak is the probability that are playing that takes a head to the engine manages to stay in the air setting that probability to zero means a single shot through the engine is guarantee to bring the plane down what would the one look like

Then you'd have planes coming back with bullet holes all over the wings the fuselage the nose -but  don't at all on the engine the military energy wise has two options for explaining this either the german bullets just happened to hit every part of the plane but one or the engine is a point of total vulnerability both stories explain the data but the letter makes a job more sense the arm or goes where the bullet holes aren't walls recommendations were quickly put into effect and we're still being used by the navy and the air force through the wars in korea and vietnam i can tell you exactly how many american planes they saved

the data slinging descendants of the s rg inside today's military no doubt have a pretty good idea

one thing the american defense establishment has traditionally understood very well is that countries don't when wars just by being braver than the other side or for her or slightly preferred by god the winners are usually the guys who get five percent fewer of their planes shut down or used five percent less fuel

or get five percent more nutrition into their infantry at ninety five percent of the cost that's not this stuff war movies are made of but it's the stuff wars are made of and there's math every step of the way 


Total Number of words : 304

Correct Words :294 

Percentage : 97.64%


**SPEECH SYNTHESIS**

-After the text extraction is done, we used Google text to Speech API.
-The process of translating text input into audio data is called synthesis and the output of synthesis is called synthetic speech. 
-The speech synthesis process generates raw audio data as a base64-encoded string.
-It make use of WAVENET VOICE  , the key difference to a WaveNet voice is the WaveNet model used to generate the voice. WaveNet models have been trained using raw audio samples of actual humans speaking. As a result, these models generate synthetic speech with more human-like emphasis and inflection on syllables, phonemes, and words.

**DESCRIPTION OF THE IMAGE**

When an image is given as input, we extract properties out of the image using Google Vision API.
The Vision API can perform feature detection on a local image file by sending the contents of the image file as a base64 encoded string in the body of your request.
Example 1:
![image](https://user-images.githubusercontent.com/83057352/117642685-33b2ad00-b1a5-11eb-9bef-2747557fac57.png) ![image](https://user-images.githubusercontent.com/83057352/117642701-390ff780-b1a5-11eb-8cc8-546735fe90de.png)

MODULE -1 

**AUTOMATIC PAGE TURNER AND SCANNER**
![image](https://user-images.githubusercontent.com/83057352/117642754-4c22c780-b1a5-11eb-864e-8a806c5cae46.png)

**TURNER DESIGN WITH DIMENSIONS**
![image](https://user-images.githubusercontent.com/83057352/117642892-76748500-b1a5-11eb-8dcb-60c93f37b74a.png)

**TURNER LAYOUT WITH NAMING**
![image](https://user-images.githubusercontent.com/83057352/117642964-8724fb00-b1a5-11eb-832e-9ac46f0e772e.png)

LIST OF COMPONENTS

• Servo motors- 8 nos.
• Arduino Uno- 1 nos.
• Power supply for servo motors.
• Acrylic sheets.




 









                                         
     
