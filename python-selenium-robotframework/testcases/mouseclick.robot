*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://swisnl.github.io/jQuery-contextMenu/demo.html

*** Test Cases ***
myTestcase
    open browser    ${url}  ${browser}
    maximize browser window
    # Right Click
    open context menu   xpath:/html/body/div/section/div/div/div/p/span
    sleep   3

    go to   http://testautomationpractice.blogspot.com/
    maximize browser window
    # Double click
    double click element    xpath://*[@id="HTML10"]/div[1]/button
    sleep   3

    # Drag and drop
    go to   http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    maximize browser window
    drag and drop   id:box1     id:box106
    sleep   3

    close browser


