import os, re, sys
import codecs


infile = codecs.open(sys.argv[1])
outfile = codecs.open(sys.argv[1]+".new","w")

b = 0
for line in infile:
    info = re.split("\t",line.rstrip())
    if len(info)<2:
        outfile.write("\n\n")
        continue
    match = re.search("B",info[-1])
    if match:
        b =1

    if info[-3] == "1" and info[-1] == "O":
        if b ==1 :
            info[-1] = "I-Arm1"
        else:
            info[-1] = "B-Arm1"
            b =1 
    if info[-3] =="0" and info[-1] =="O":
        b = 0

    if re.search("I",info[-1]) and b ==0:
        info[-1] = re.sub("I","B",info[-1])
    
    if info[-3] == "0" and re.search("Arm",info[-1]):
        info[-1] = "O"
    outfile.write("\t".join(info)+"\n")
