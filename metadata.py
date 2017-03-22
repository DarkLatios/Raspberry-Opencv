import argparse
from PIL import Image
from PIL.ExifTags import TAGS
imagename='C:\Users\user\Desktop/xyz.jpg'
out='data.txt'
def getMetaData(imagename,out):
    try:
        metaData={}
        imgFile=Image.open(imagename)
        print ("Getting Meta Data....")
        info=imgFile._getexif()
        print "Worked"
        if info:
            print ("Found Meta Data!")
            for(tag,value) in info.items():
                tagname=TAGS.get(tag,tag)
                metaData[tagname]=value
                if not out:
                    print (tagname,value)

                if out:
                    print ("Outputting to file....")
                    with open(out,'w') as f:
                        for(tagname,value)in metaData.items():
                            f.write(str(tagname)+"\t"+\
                                    str(value)+"\n")


    except:
        print ("Failed")






getMetaData(imagename,out)
#def Main():
 #   parser=argparse.ArgumentParser()
  #  parser.add_argument("img",help="name of an image file.")
   # parser.add_argument("--output","-o",help="dump data out to file")
    #args=parser.parse_args()
   # if args.img:
    #    getMetaData(args.img,args.output)
    #else:
     #   print (parser.usage)

#if __name__== '__main__':
  #  Main()
