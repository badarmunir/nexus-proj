*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://google.com/
${url2}  https://www.bing.com/

*** Test Cases ***
Tabbedwindowtest
     open browser    ${url}  ${browser}
     maximize browser window

     sleep  3

     open browser    ${url2}  ${browser}
     maximize browser window

     switch browser     1
     ${title1} =  get title
     log to console  ${title1}

     switch browser     2
     ${title2} =  get title
     log to console  ${title2}

     sleep  3
     close all browsers
