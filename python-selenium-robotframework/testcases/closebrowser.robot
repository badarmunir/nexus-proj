*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://demowebshop.tricentis.com/register

*** Test Cases ***
myTestcase
    open browser    ${url}  ${browser}
    maximize browser window

    open browser    ${url}  ${browser}
    maximize browser window

    close all browsers