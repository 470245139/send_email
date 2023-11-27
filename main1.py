import yagmail

yag = yagmail.SMTP(user="ffffz470245139@163.com", password="CZNBRJEPGWLDUQZF", host='smtp.163.com')

contents = ['今天是周末,我要学习, 学习使我快乐;', '<a href="https://www.python.org/">python官网的超链接</a>', './girl.png']

yag.send('470245139@qq.com', '主题:学习使我快乐', contents)


