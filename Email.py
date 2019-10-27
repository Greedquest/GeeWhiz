#from DataCollation import Semantic_Class as Sem

def sendEmail(msg):
    import smtplib
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("geewhiz833@gmail.com" , "1234AbCd")
    
    # Import the email modules we'll need


    server.send_message(msg)
    server.quit()
    
    
#def dispatchFaultMessage(faultObject, to):
#    from email.message import EmailMessage
#    faultObject.value = "SANJAN DAS"
#    
#    msg = EmailMessage()
#    
#    msg.set_content(f"Commander,\n\nFault conditions have been violated on your control panel!({faultObject.value}){faultObject.meaning}\n\nThe factory is in peril! \n\nBest wishes, \nGeeWhizWare")
#    
#    # me == the sender's email address
#    # you == the recipient's email address
#    msg['Subject'] = f"Error in {faultObject.meaning}"
#    msg['From'] = "geewhiz833@gmail.com"
#    msg['To'] = to
#    
#    
#    sendEmail(msg)
    
def dispatchFaultMessage(conditions_map, semantic_map, to):
    from email.message import EmailMessage
    
    faultlist = []
    for i in conditions_map:
        if type(conditions_map[i])==str:
            faultlist.append(semantic_map[i].meaning + " is in the state: " + semantic_map[i].value)
        else:
            faultlist.append(semantic_map[i].meaning + " has value "+str(semantic_map[i].value)+" and so has deviated from the range: " + str(conditions_map[i]))
            
    error_message = "CONDITIONS BREACHED:"
    for j in faultlist:
        error_message += "\n\t"
        error_message += j
    
    msg = EmailMessage()
    
    msg.set_content("Commander,\n\nFault conditions have been violated on your control panel!\n\n{}\n\nThe factory is in peril! \n\nBest wishes, \nGeeWhizWare".format(error_message))
    
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = f"Error on your control panel"
    msg['From'] = "geewhiz833@gmail.com"
    msg['To'] = to
    
    
    sendEmail(msg)
    
#if __name__ == "__main__":
#    #from DataCollation.SemanticOutputMap import _randomSemanticClass as randSemantic
#    
#    test = Sem.Discrete("Fan Oven Status")
#    test.value = True
##    print(test.meaning, test.value)
##    print(test._valueMap)
#    
#    Switchvalue = Sem.Discrete("Oven Power", {0:"left",1:"middle",2:"right"})
#    Switchvalue.value = 1
#    #print(Switchvalue.meaning, Switchvalue.value)
#    
#    Needle_test = Sem.ContinuousDial("Voltage", 20,-20,40,0)
#    Needle_test.value = 10
#    #print(Needle_test.meaning, Needle_test.value)
#    
#    Example_semanticmap   = {"ID1":Needle_test,"ID2":test,"ID3":Switchvalue}
#    Example_conditionsmap = {"ID1":[5,25],"ID2":"On","ID3":"middle"}
#    dispatchFaultMessage(Example_conditionsmap,Example_semanticmap, "sm2232@cam.ac.uk")
    