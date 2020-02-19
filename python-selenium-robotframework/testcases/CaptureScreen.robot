*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/

*** Test Cases ***
myTestcase
    open browser    ${url}  ${browser}
    maximize browser window
    input text  id:txtUsername  Admin
    input text  id:txtPassword  admin123

    capture element screenshot  xpath://*[@id="divLogo"]/img    testcases\logo.png
    capture page screenshot     testcases\page.png