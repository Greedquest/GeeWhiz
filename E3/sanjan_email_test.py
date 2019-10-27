import smtplib
import time
import imaplib
import email
import pprint
import os

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python

#
# ------------------------------------------------

def download_attachments(msg, download_folder=''):
    # downloading attachments
    print('starting download script')
    for part in msg.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join(download_folder, fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                subject = str(msg).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
                print('Downloaded "{file}" from email titled "{subject}".'.format(file=fileName, subject=subject))
    

def read_email_from_gmail(FROM_EMAIL, FROM_PWD, subject_keyword, how_many=1, download_folder='',SMTP_SERVER="imap.gmail.com"):
    try:
        
        #--------------------------THIS BIT WORKS, DON't EDIT -----------------------------
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        # Get email ids based on the subject keyphrase passed
        type, data = mail.search(None, '(SUBJECT %s)'% subject_keyword)
        #print(data)
        mail_ids = data[0]
        mail_ids = mail_ids.decode('utf-8')
        

        id_list = mail_ids.split()   
        #first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        #---------------------------------------------------------------------------------
    
        for i in range(latest_email_id, latest_email_id - how_many, -1):
            #print('==============================================================')
            typ, data = mail.fetch(str(i), '(RFC822)' )

            for response_part in data:
                #print('**********')
    
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    #print(msg)
                    #print(msg.get_payload())
                    
                    email_subject = msg['subject']
                    email_from = msg['from']
                    
                    #print('---------')
                    body = msg.get_payload()[0].get_payload()
                    #print(body)
                    #print(msg.get_payload(decode=False))
                    """
                    if msg.is_multipart():
                        for payload in msg.get_payload():
                            # if payload.is_multipart(): ...
                            print(payload.get_payload())
                    else:
                        print(msg.get_payload())
                    """
                        
                        
                    #print('From : ' + email_from + '\n')
                    #print('Subject : ' + email_subject + '\n')
                    #print('Body : ')
                    #print(body)
                    #print('----------')
                    
                    # downloading attachments
                    download_attachments(msg, download_folder)
                    
        return body
    except Exception as e:
        return None
        
        
if __name__ == "__main__":
    ORG_EMAIL   = "@gmail.com"
    FROM_EMAIL  = "geewhiz833" + ORG_EMAIL
    FROM_PWD    = "1234AbCd"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT   = 993
    body = read_email_from_gmail(FROM_EMAIL, FROM_PWD, 'attachment?')
    print(body)