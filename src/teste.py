import imaplib
import email
from MailParser import *

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login('marcusdownserver@gmail.com', 'downserver')
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    #print 'Message BEGIN\n%s\nMessage END\n' % data[0][1]
    parser = MailParser(data[0][1])
    
    print 'From Name: ' + parser.fromName
    print 'From Address: ' + parser.fromAddress
    print 'To address: ' + parser.toAddress
    print 'Subject: ' + parser.subject
    print 'Message: ' + parser.messageContent
    
M.close()
M.logout()