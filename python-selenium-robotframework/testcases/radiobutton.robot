*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://www.practiceselenium.com/practice-form.html


*** Test Cases ***
Test Radio Buttons and Check Boxes
    open browser    ${url}  ${browser}
    maximize browser window
    set selenium speed  2seconds

#select radio button
    select radio button  sex    Female
    select radio button  exp    5

#select checkbox
    select checkbox     BlackTea
    select checkbox     RedTea

#uselect checkbox
    unselect checkbox     RedTea





*** Keywords ***