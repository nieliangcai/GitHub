import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from socket import gaierror,error
from utils.log import logger

class Email(object):
    def __init__(self,sender,receiver,password,title,server,message=None,path=None):
        '''基础信息设置'''
        self.server = server
        self.title = title
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('related')

    def _attach_file(self,att_file):
        '''添加附件'''
        att = MIMEText(open('%s'%att_file,'rb').read(),'plain','utf-8')
        att['Content-Type'] = 'application/octet-stream'        #二进制文本信息
        file_name = re.split(r'[\\|/]',att_file)   #把文件路径拆分,得到最后一个为文件名称
        #print(file_name)
        att['Content-Disposition'] = 'attachment;filename="%s"' %file_name[-1]  #Content-Disposition 影响传送附件名称和格式
        self.msg.attach(att)
        logger.info('attach file{}'.format(att_file))

    def send(self):
        '''发送邮件'''
        self.msg['Subject'] = Header(self.title,'utf-8')
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        if self.message:
            self.msg.attach(MIMEText(self.message))

        if self.files:
            if isinstance(self.files,list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files,str):
                self._attach_file(self.files)
        try:
            smtp_server = smtplib.SMTP(self.server)
        except (gaierror or error) as e:
            logger.exception("发送邮件失败!无法连接到SMTP服务器,请检查网络以及服务器.%s",e)
        else:
            try:
                smtp_server.ehlo()  #使用ehlo指令向ESMTP确认身份信息
                smtp_server.starttls()  #加密
                smtp_server.login(self.sender,self.password)
            except smtplib.SMTPAuthenticationError as e:
                logger.exception("用户名密码验证失败！%s",e)
            else:
                smtp_server.sendmail(self.sender,self.receiver.split(';'),self.msg.as_string())
                #print(self.msg.as_string())
            finally:
                smtp_server.quit()
                logger.info('邮件发送"{0}"成功！收件人:{1}。如果没有受到邮件'
                            '请检查垃圾箱，同时查看邮件地址是否正确'.format(self.title,self.receiver))