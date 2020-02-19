*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://www.practiceselenium.com/practice-form.html


*** Test Cases ***
Handling DrpDown and lists
    open browser    ${url}  ${browser}
    maximize browser window

    select from list by label   continents  Europe
    sleep   2
    select from list by index   continents  6

    #list box
    select from list by label   selenium_commands   Switch Commands
    sleep   2

    unselect from list by label   selenium_commands   Switch Commands