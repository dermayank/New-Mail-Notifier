import smtplib
import time
import imaplib
import email
import os

email_id = "mayankrocking80@gmail.com"
password = '';
server = "imap.gmail.com";
port = 993;

def users_log():
    if not os.path.exists("users_data"):
        os.makedirs("users_data")

    split_id = email_id.split('@');
    filename = split_id[0]+".log"
    #user_list = open("users_data/"+filename,"w+");
    #user_list.close()
    return filename

def check(e_from,subject,filename):
    val = False;
    subject = subject.replace('\n', ' ').replace('\r', '').replace("'",'')
    user_list = open("users_data/"+filename,"a+")
    var = user_list.readlines();
    for lines in var:
        if lines.find(subject)!= -1:
            val=True;
            break;
    if not val:
        user_list.writelines("%s:-->%s\n" %(e_from,subject));
    return val;
    


def read_email_from_gmail():
    #check("email_from","email_subject")
    try:
        filename = users_log();
        
        mail = imaplib.IMAP4_SSL(server)
        mail.login(email_id,password)

	folderStatus, UnseenInfo = mail.status('INBOX', "(UNSEEN)")

	print folderStatus

	NotReadCounter = int(UnseenInfo[0].split()[2].strip(').,]'))
	print NotReadCounter
        mail.select('inbox')

        type, data = mail.search(None, 'All')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )
            email_from = "";
            email_subject = "";
     
            for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print 'From : ' + email_from + '\n'
                        print 'Subject : ' + email_subject + '\n\n'
                        
            if check(email_from,email_subject,filename):
                    print "\n\nNO MORE MAILS"
                    break;

    except Exception, e:
        print str(e)

read_email_from_gmail();
