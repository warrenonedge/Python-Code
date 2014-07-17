#-------------------------------------------------------------------------------
# Name:        GoogleInterviewProblem
# Purpose:  Say you're dealing with data that has a lot of repeated characters
#           in it. You'd like to take advantage of that to compress the data.
#           In particular, you are given the following run-length encoding
#           scheme: An encoded string is normally passed through verbatim.
#           However, if there is a decimal number followed by the character
#           'x', then the character after the x will be repeated that many
#           times."
#                   For example: "abc11xkd55s" -> "abckkkkkkkkkkkd55s"
#
# Author:      Damon Edge
#
# Created:     06/27/2014
# Copyright:   (c) Dae 2014
#-------------------------------------------------------------------------------

def repeater(decode):
    result = ""
    number = ""
    i = 0
    while i < len(decode):
    #for i, l in enumerate(decode):
        if decode[i].isdigit() and i < (len(decode)-1):
            number += decode[i]
        elif decode[i] == 'x' and number != "":
            result += int(number)*decode[i+1]
            number = ""
            i+=1
        else:
            result += number + decode[i]
            number = ""
        i+=1
    print(result)