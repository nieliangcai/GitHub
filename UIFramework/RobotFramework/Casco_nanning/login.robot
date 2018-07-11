*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
test01
    open browser     ${url} chrome
    maximize browser window
    input text      id=txtUserName      ${username}
    input text      id=txtPassword      ${password}


*** Variables ***
#用来设置一些全局变量;url name password
${url}          http://115.29.234.80:8110/
${username}     admin
${password}     CASCO@126

*** Keywords ***
#定义一些函数，供Test Case调用
