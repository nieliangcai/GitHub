*** Settings ***
Library  Selenium2Library
Library  mail

*** Test Cases ***
test01
    [Documentation]  RF for kuaidi100
    open browser    ${url}  chrome
    wait until page contains element  id=menu-track     30   shuaxinTimeout
    maximize browser window
    wait until page contains element  xpath=//*[text()='登录']  30   dengluchaoshi
    click element  xpath=//*[text()='登录']
    sleep  2
    input text  id=name     ${username}
    input text  id=password     ${password}
    wait until page contains element  id=submit         40   meiyouchuxiandengluanniu
    click button   id=submit  #登录成功

    wait until page contains element  xpath=//*[text()='韵达快递']  60   liebiaomeiyouxianshi
    ${count1}    get matching xpath count  xpath=//tr
    ${a}  evaluate  ${count1}
    log  ${count1}
    log  ${a}
#    ${counts1}  get webelements  xpath=//tr
#    ${count1}  get length  ${counts1}

    click element   id=menu-track        #点击查快递按钮
    input text      name=postid      ${number}
    sleep  2
    click element  id=query             #点击搜索按钮

test02
    ${text1}     get text  xpath=//*[@class="single-name"]      #需要校验结果表中的快递公司是否和查件记录中的一致
    should be equal   ${text1}    申通快递
    mouse over  id=userName
    sleep  2
    #${a}
    click element  xpath=//*[@id='userName']/ul/li[1]
    switch to Window
    wait until page contains element  xpath=//*[text()='韵达快递']  60   liebiaomeiyouxianshi
    get matching xpath count  ${count2}
    run keyword if   ${count2}>=${count1}  log   ok

test03
    send()
*** Variables ***

${url}           http://www.kuaidi100.com/          #url
${username}      13661501664                        #zhanghao
${password}      yyy0909                            #mima
${number}        888812169286                       #danhao

*** Keywords ***
switch to Window
    [Documentation]  切换窗口
    [Arguments]  ${i}=0     #切换Windows，参数为i，默认为0
    ${windows}      list windows        #获取所有的窗口
    ${NewWindow}    evaluate    ${windows}[${i}]        #所有窗口为一个list，list中的第i个位新Window
    select window  ${NewWindow}

move_to_yuanxizhuanye
	[Documentation]  切换frame和鼠标移动到院系专业，将类似这样的连贯和通用型的动作，绑定在一起。形成一个个用户自定义的关键字，让用例简单明了
    select frame     zzu_top_6                        #切换frame
    mouse over       xpath=//*[text()='院系专业']      #鼠标移动至院系专业



