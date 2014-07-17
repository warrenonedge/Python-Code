import sys

def UPCa():
    if len(sys.argv)==1:
        print "Usage: {} <infile> [<outfile>]".format(sys.argv[0])
        return
    else:
        inFile = open(sys.argv[1],"r")
        if len(sys.argv)==2:
            outFile = sys.stdout
        else:
            outFile = open(sys.argv[2],"w")
    i = []
    for line in inFile.readlines():
        fixLine = line[:-1]
        if fixLine.isdigit():
            i.append(fixLine)
        else:
            newLine = ""
            for l in fixLine:
                if l.isdigit():
                    newLine += l
            i.append(newLine)
    Lpat = ["   || |","  ||  |","  |  ||"," |||| |"," |   ||"," ||   |"," | ||||"," ||| ||"," || |||","   | ||"]
    Rpat = invert(Lpat)
    for item in i:
        if len(item)== 12:
            result = "| |"
            for num in item[:6]:
                result += Lpat[int(num)]
            result += " | | "
            for num in item[6:]:
                result += Rpat[int(num)]
            result += "| |"
            validCode = validCD(item)
            if validCode == True:
                validCode = valid4(result)
                if validCode == True:
                    print >> outFile, result
                    continue
            print >> outFile, "{} is an Invalid UPC-A Code due to wrong Check Digit".format(item)
        else:
            print >> outFile, "{} is an Invalid UPC-A Code due to length".format(item)

def invert(pattern):
    """This function returns the inverted pattern for the Right side of the
    Barcode"""
    retPat = []
    for pat in pattern:
        resStr = ""
        for sym in pat:
            if sym == " ":
                resStr += "|"
            else:
                resStr += " "
        retPat.append(resStr)
    return retPat

def valid4(code):
    """This function test for consecutive 1s or 0s in the barcode and returns
    a Boolean"""
    bit1 = 0
    bit0 = 0
    count = 0
    for num in code:
        if bit0 > 4 or bit1 > 4:
            print(count, bit0, bit1)
            return False
        if num == "|":
            bit1 += 1
            bit0 = 0
        elif num == " ":
            bit0 += 1
            bit1 = 0
        count += 1
    return True

def validCD(code):
    CD = code[-1]
    code = code[:-1]
    result = (int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10]))*3
    result += int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])
    result = result % 10
    if result != 0:
        result = 10 - result
        if result != int(CD):
            return False
    return True

UPCa()
