#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json, codecs

#INNAMEFILE = "d1/20220715000013.json"
INNAMEFILE = "d1/20220714191708.json"
fO = codecs.open( INNAMEFILE, "r")
text = fO.read()
fO.close()

parts = text.split('","')
#data
tempergebnis = ""
tempinput = ""
tempsichlev = ""
#true
c = 0
cc = 0
ccc = 0 #level 0
cccc = 0 #level 1
ccccc = 0 #level 2
cccccc = 0 #not qualified 
#false
ggonews = False
validref = True
numberofinput = "0"
k = 0
g = 0
h = 0 #count of answers per case
dhb = 0
dhg = 0
outgood = "\n"
outbad = "\n"
for p in range( len( parts )):
    ##set data
    
    if("_e" in parts[p] ):
        h += 1
        tempergebnis = parts[p].split('":"')[1]
        tempnumoi = parts[p].split( '_e":"' )[0].split("_")[0].replace('{"', "")
        #print(tempnumoi)
        if( numberofinput != tempnumoi ):
            if( ggonews == False):
                k += 1
                outbad = outbad + numberofinput +"// "+tempinput +"// "+ str(h) +"\n"
                dhb += h
            else:
                outgood = outgood +"// "+ str( h ) +"\n"
                dhg += h
                g += 1
            ggonews = False
            validref = True
            h = 0
            
        numberofinput = tempnumoi
            #print("-##-", parts[p])
    if("_f" in parts[p] ):
        c += 1
        tempinput = parts[p].split('":"')[1]
    if("_s" in parts[p] ):
        tempsichlev = parts[p].split('":"')[1]
    if("MMM" in tempergebnis or "NNN" in tempergebnis ):
        validref = False
    #evaluate
    if( "_r" in parts[p] ): #TRUE
        ggonews = True
        outgood = outgood +  numberofinput+"// "+tempinput+"// "+tempergebnis+"// "+tempsichlev
        cc+=1
        if( "0" in tempsichlev ):
            ccc += 1
        elif( "1" in tempsichlev ):
            cccc += 1
        elif( "2" in tempsichlev ):
            ccccc += 1
        if("MMM" in tempergebnis or "NNN" in tempergebnis ):
            cccccc += 1
    
        
print( "All", g+k )
print( "True positiv", g, cc )
print( "L1:", ccc, "L2:", cccc, "L3:", ccccc )
print( "Durchschn. Antwortzahl:", dhg/g)
print( "True pos. not qualified reference:", cccccc )
print( "False",  k )
print( "Durchschn. Antwortzahl:", dhb/k)
print( outbad )
#print( outgood )
