*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/resources.robot

*** Variables ***
${browser}  chrome
${url}  http://newtours.demoaut.com/


*** Test Cases ***
TC1
    ${PageTitle}=   launchBrowser    ${url}    ${browser}
    log to console  ${PageTitle}
    input text  name:userName   mercury
    input text  name:password   mercury


