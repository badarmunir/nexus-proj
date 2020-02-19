*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  http://demo.automationtesting.in/Windows.html


*** Test Cases ***
Tabbedwindowtest
     open browser    ${url}  ${browser}
     maximize browser window
     click element  xpath://*[@id="Tabbed"]/a/button
     select window  Sakinalium | Home
     click element  xpath://*[@id="container"]/header/div/div/div[2]/ul/li[4]/a
     sleep  3
     close all browsers
