*** Settings ***
Library  SeleniumLibrary




*** keywords ***
# user defined keyword
launchBrowser
    #user defined arguments
    [Arguments]  ${appurl}  ${appbrowser}
    open browser    ${appurl}  ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}
