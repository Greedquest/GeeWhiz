def sendEmail(msg):
    import smtplib
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("geewhiz833@gmail.com" , "1234AbCd")
    
    # Import the email modules we'll need


    server.send_message(msg)
    server.quit()
    
    
def dispatchFaultMessage(faultObject, to):
    from email.message import EmailMessage
    faultObject.value = "SANJAN DAS"
    
    msg = EmailMessage()
    
    msg.set_content(f"Dear Sir/Madam,\n\nDarling this value ({faultObject.value}) is not the situation we were after for {faultObject.meaning}\n\nThe factory is gone...")
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f"Error in {faultObject.meaning}"
    msg['From'] = "geewhiz833@gmail.com"
    msg['To'] = to
    
    
    sendEmail(msg)
    
if __name__ == "__main__":
    from DataCollation.SemanticOutputMap import _randomSemanticClass as semantic
    
    dispatchFaultMessage(semantic(), "gh454@cam.ac.uk")
    