#-------------------------------------------------------------------------------
# Name:        pml.py
# Purpose:     PML Project
#                   A PML document is a standard HTML document with one
#                   additional feature. Any text between the starting <pml> tag
#                   and the ending </pml> tag is interpreted as Python source
#                   code. There can be multiple PML blocks in a PML file. PML
#                   blocks will never nest. The standard HTML should pass
#                   through the parser untouched. The code within the PML tags
#                   should be executed with the python interpreter. A technique
#                   should be implemented to write data to the output stream
#                   from within the PML. In other words the python code should
#                   be able to define the output that will replace the PML.
#                   Variables and functions declared in one PML block should be
#                   available in subsequent PML blocks. PML should be able to
#                   handle indentation dependent upon the first non-whitespace
#                   line of python code.
#
# Author:      Damon Edge
#
# Created:     04/11/2014
#-------------------------------------------------------------------------------
import sys, os, subprocess

def pml():
    if len(sys.argv)==1:
        print "Usage: {} <infile> [<outfile>]".format(sys.argv[0])
        return
    else:
        inFile = open(sys.argv[1],"r")
        lines = inFile.readlines()
        if len(sys.argv)==2:
            outFile = sys.stdout
        else:
            outFile = open(sys.argv[2],"w")
            outFile = open(sys.argv[2],"a")
    execute = True
    printLine = False
    indCount = 0
    for line in lines:
        result = ""
        out = open('tempCode.py', 'a+')
        if '<pml>' in line:
            execute = False
            printLine = True
        if '</pml>' in line:
            execute = True
            printLine = False
        if execute == True and printLine == False:
            if '</pml>' in line:
                runCode = ['python', out.name]
                process = subprocess.Popen(runCode, stdout=subprocess.PIPE)
                for line in process.stdout:
                    print >> outFile, line[:len(line)-1]
                process.terminate()
                out.close()
                os.remove(out.name)
            else:
                if lines.index(line)== len(lines)-1:
                    print >> outFile, line
                else:
                    print >> outFile, line[:len(line)-1]
        if execute == False and printLine == True:
            if '<pml>' not in line:
                if indCount == 0:
                    for ch in line:
                        if ch.isalpha():
                            break
                        indCount += 1
                out.write(line[indCount:])
                if "pml" in line:
                    out.write("print pml\n")
    out.close()
    os.remove(out.name)
pml()