def triage_system():
    print("********Hospital expert system********")
    name= input("patient name: ")
    age= int(input("enter age: "))
    print("tell the symptoms: ")
    chest_pain= input("Chest_pain? ").lower()=='y'
    stomach_pain= input("stomach_pain? ").lower()=='y'
    short_breath= input("short breath? ").lower()=='y'
    fever= input("fever? ").lower()=='y'
    injury= input("injury? ").lower()=='y'
    bleeding= input("bleeding? ").lower()=='y'
    dizziness= input("dizziness??").lower()=='y'
    
    print("analyzing your report :")
    
    depart=[] 
    advice=[] 
    
    if chest_pain or short_breath:
        depart.append( "cardiology")
        advice.append("consult your doc asap")
    if stomach_pain:
        depart.append("gastroenterology")
        advice.append(" ")
    if bleeding or injury:
        depart.append("emergency room")
        advice.append(" ")
    if dizziness:
        depart.append("neurology")
        advice.append( " ")
    if fever and age<12:
        depart.append("pediatrics")
        advice.append(" ")
    elif fever :
        depart.append("general ward ")
        advice.append(" ")
    if not depart:
        depart.append("OPD")
        advice.append(" ")
        
    print("\n Patient report")
    print(f"name: {name}")
    print(f"age: {age}" )
    print(f" department : {', ' .join(depart)}")
    print(f"advice: {', '.join(advice)}")   
    
if __name__=="__main__":
    triage_system()