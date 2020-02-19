*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://google.com/
${url2}  https://www.bing.com/
*** Test Cases ***
Navigation
     open browser    ${url}  ${browser}
     ${loc}=    get location
     log to console  ${loc}

     sleep  3

     go to  ${url2}
     ${loc}=    get location
     log to console  ${loc}
     sleep  3

     go back
     ${loc}=    get location
     log to console  ${loc}
     sleep  3

     close browser


