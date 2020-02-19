*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://www.countries-ofthe-world.com/flags-of-the-world.html


*** Test Cases ***
ScrollingTest
    open browser    ${url}  ${browser}
    maximize browser window
    #scroll view pixel
    execute javascript  window.scrollTo(0,1500)
    #element scroll
    scroll element into view    xpath://*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[29]/td[1]


    execute javascript  window.scrollTo(0,document.body.scrollHeight)  #end of page scroll
    sleep   5
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #start of page