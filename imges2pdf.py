
### img2pdf ####
import os 
import sys
from fpdf import FPDF 
from PIL import Image
import glob


images_path = raw_input("Enter the path of the folder containing images : ")
images =images_path+"/*.jpg"
#images =images_path+"\\"
#*.jpg"

assert os.path.exists(images_path), "I did not find the file at, "+str(images_path)
f = os.chdir(images_path)
print("Hooray we found your file!")
#stuff you do with the file goes here
image_list = []
for filename in glob.glob(images): #assuming gif
    
    image_list.append(filename)

pdf = FPDF( unit = 'mm')
pos = 0.1
for i in image_list:
    
    pdf.add_page()
    im = Image.open(i)
    pdf.image(i,pos,pos,200,250)

pdf_name = raw_input("Enter the pdf name : ")
pdf_name = pdf_name+".pdf"
pdf.output(pdf_name)






