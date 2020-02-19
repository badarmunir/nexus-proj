*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://demowebshop.tricentis.com/register


*** Test Cases ***
Regtest
    open browser    ${url}  ${browser}
    maximize browser window
    #Set speed for all the elements
    set selenium speed  3seconds
    #default speed
    sleep   3
    select radio button    Gender  M
    input text  name:FirstName    badar
    input text  name:LastName    munir
    input text  name:Email    badarmunir021@gmail.com
    input text  name:Password    badar12345
    input text  name:ConfirmPassword    badar12345
    #click element   register-button
