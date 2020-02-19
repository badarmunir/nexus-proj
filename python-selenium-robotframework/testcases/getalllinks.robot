*** Settings ***
Library  SeleniumLibrary



*** Variables ***
${browser}  chrome
${url}  http://newtours.demoaut.com/


*** Test Cases ***
getAllLinkstest
    open browser    ${url}  ${browser}
    maximize browser window

    ${Alllinkscount}=    get element count   xpath://a
    log to console  ${Alllinkscount}

    @{LinkItems}    create list

    : FOR   ${i}    IN RANGE    1   ${Alllinkscount}+1
    \   ${linkText}=  get text  xpath:(//a)[${i}]
    \   log to console  ${linkText}

