import os
from PIL import Image
from gtts import gTTS
from pygame import mixer
from pytesseract import image_to_string
#from translation import baidu, google, youdao, iciba
mixer.init()
#img=Image.open('/01/Image processing/the-quick-brown-fox-jumps-over-the-lazy-dog-is-an-example-of-what-type-of-sentence-or-verse.jpg')
try:
   #img=Image.open('/01/Image processing/Images/data2.jpg')
   img=Image.open('/01/Image processing/Images/numdata3.jpg')
   text=image_to_string(img)
   print("Choose Language: 1. Tamil | 2. English | 3. Telugu | 4. French")
   lan=int(input())
   if(lan==1):
      putLan="ta"
   elif(lan==2):
      putLan="en"
   elif(lan==3):
      putLan="te"
   else:
      putLan="fr"
   speech= gTTS(text,putLan,slow=False)
   speech.save("test.mp3")
   mixer.music.load("test.mp3")
   mixer.music.play()
   #os.system("test.mp3")
   print(text)
   print("Press any key to exit")
   x=input()
except:
   print("Insert image and try again")
   x=input()    

