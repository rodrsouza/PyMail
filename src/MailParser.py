'''
Created on 12/04/2015

@author: Rodrigo
'''
import email
from optparse import isbasestring

class MailParser:
    
    fromName = ""
    fromAddress = ""
    toAddress = ""
    subject = ""
    messageContent = ""

    def __init__(self, params = None):
        if not params:
            return
        elif isbasestring(params):
            self.__parse_string(params)
            return
            
            
    @classmethod
    def __parse_string(self, text):
        msg = email.message_from_string(text)
        self.fromName = self.__parse_mail_name(msg['From'])
        self.fromAddress = self.__parse_mail(msg['From'])
        self.toAddress = self.__parse_mail(msg['To'])
        self.subject = msg['Subject']
        
        if msg.is_multipart():
            i = 0
            msg_took = False
            for pl_part in msg.get_payload():
                if pl_part.get_content_type() == 'text/plain' and not msg_took:
                    self.messageContent = str(pl_part.get_payload())
                    i = i+1
                    msg_took = True            
            if (i > 1) or (i == 0): 
                self.messageContent = ""
        
        else:
            self.messageContent = str(msg.get_payload())

    @classmethod
    def __parse_mail(self, text):
        if isbasestring(text):
            if ("<" in text) and (">" in text) :
                s=text
                return s[s.find('<')+1:s.find('>')]
            else:
                return text
        else:
            return ""
    
    @classmethod
    def __parse_mail_name(self, text):
        if isbasestring(text):
            if ("<" in text) and (">" in text) :
                s=text
                return s[0:s.find('<')-1]
            else:
                return ""
        else:
            return ""    