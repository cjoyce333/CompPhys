#-------------------------------------------------------------------------------
# Name:        secondstoyears
# Purpose:     To determine whether a baby can expect to live for one billion seconds by converting seconds to years
#
# Author:      Clarissa Joyce
#
# Created:     04/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

ageinseconds = input("How many seconds? ")

sectomin = 1/60.
mintohour = 1/60.
hourtoday = 1/24.
daytoyear = 1/365.

ageinyears = ageinseconds * sectomin * mintohour * hourtoday * daytoyear

if (ageinyears<= 100) :
    liveordie = ""

else :
    liveordie=" not"

print "Baby will be "+ repr(ageinyears) +" years old in " + repr(ageinseconds)+" seconds."
print "The baby would" + liveordie+ " be expected to live for "+ repr(ageinseconds) + " seconds."