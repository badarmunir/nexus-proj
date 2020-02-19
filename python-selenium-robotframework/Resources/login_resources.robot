*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://admin-demo.nopcommerce.com


*** Keywords ***
Open my browser
    open browser    ${url}  ${browser}
    maximize browser window

Close Browsers
    close all browsers

Open Login Page
    go to   ${url}

Input username
    [Arguments]  ${username}
    input text  id:Email    ${username}

Input pwd
    [Arguments]  ${pwd}
    input text  id:Password    ${pwd}


Click login button
    sleep   2
    click element   xpath://input[@class='button-1 login-button']


Click logout button
    click link  logout

Error message should be visible
    page should contain  Login was unsuccessful

Dashboard page should be visible
    page should contain  Dashboard