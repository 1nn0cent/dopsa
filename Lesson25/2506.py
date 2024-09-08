import sys
import pymorphy3
 
s = [i.rstrip(" \n") for i in sys.stdin]
 
morph = pymorphy3.MorphAnalyzer()
 
for i in s:
    if "NOUN" in morph.parse(i)[0].tag:
        tag = morph.parse(i)[0].tag
        wrd = morph.parse("живой")[0].inflect({tag.gender, 'nomn'}).word
        if tag.number == "plur":
            wrd = morph.parse("живой")[0].inflect({"plur", 'nomn'}).word
        if tag.animacy == "inan":
            print("Не", wrd)
        else:
            print(wrd.title())
    else:
        print("Не существительное")