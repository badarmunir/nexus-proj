*** Settings ***
Library  SeleniumLibrary



*** Test Cases ***
#Forloop1
 #  : FOR  ${i}     IN RANGE    1   10
  #  \   log to console  ${i}
#Forloop2
 #  : FOR  ${i}     IN  1 2 3 4 5 6 7 8 9
 # \   log to console  ${i}

#Forloopwithlist
  #  ${items}    create list  1   2   3   4   5
  #  : FOR  ${i}    IN  @{items}
   # \  log to console   ${i}

#forloop4
    #: FOR  ${i}     IN   jhon  david  smith  scott
   # \   log to console   ${i}

#forloop5
    #@{namelist}     create list  jhon  david  smith  scott
   # : FOR  ${i}   IN  @{namelist}
    #\   log to console   ${i}


forloopwithexit
    @{items}    create list     1  2  3  4  5
    : FOR  ${i}   IN  @{items}
    \   log to console   ${i}
    \   exit for loop if   ${i}==3
