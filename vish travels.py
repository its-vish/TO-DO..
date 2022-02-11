
print("****🚖🚖WELCOME TO TRAVEL vish OLA🚖🚖****")
list1=["flora","khopi","shirwal","katraj","junction","airport","railway station"]
list2=["pune","hadapsar","swarget","manapa","gadital","fc foad","airport","dagduseth",'sarasbag',"shaniwarwada","bharti vidhyapith","khopi","junction","shivajinagar","katraj"]
current_location=input("PLEASE ENTER YOUR CUREENT LOCATION : ")
destination=input("PLEASE ENTER THE DESTINATION LOCATION : ")
nearby_riders=[["yash","CAB",".......he is ready to to go for rupees=100","📟pocket FM is avaliable"] , ["suyash","CAB",".....he is ready to to go for rupees=120","🎶songs avaliable"] , ["aditya","AUTO",".....he is ready to to go for rupees=150","🩺firstaid avaliable"] , ["karam","CAB","......he is ready to to go for rupees=200","🧯💊🩺extra sefty element avaliable"] , ["yogesh","AUTO","......he is ready to to go for rupees=130","🚭smoking prohibited"]]
riders_details=[["📞mobile no.=..987272488.." ,"🚖no.=.MH.4280YZ" , "v.color=...yellow..." , "🚖model = SUV"],["📞mobile no.=..8289247890" , "🚖no=GU.2982XBC" , "v.color=Grey" , "🚖model no.=Wagonar"],["📞mobile no.=..7428827892" , "🚖no=6789 RJ.MNO" , "v.color=pinkYellow" , "🚖model = AUTO"],["📞mobile no.=..6289637480" , "🚖no=pj.42902 LMN" , "v.color=Black" , "🚖model = Verna"],["📞mobile no.=..7249093734" , "🚖no=MH.23451PQR" , "v.color=darkPink" , "🚖model = AUTO"]]
for i in range(len(nearby_riders)):
    print(nearby_riders[i])
if  current_location in list1: 
    print("yash,suyash aditya yogesh karam is avaliable")
# if destination=="pune"or destination=="hadapsar" or destination=="sangvi" or destination=="fc road" or destination=="airport" or destination=="junction" or destination=="shivajinagar" or destination=="swarget" or destination=="katraj" or destination=="tulsibag":
if destination in list2:
    print("you can call any of them")
else:
    print("🚫no one is available for this ride")

riders=input("ENTER ANY DRIVER NAME")

rider1="yash"
rider2="suyash"
rider3="aditya"
rider4="karam"
rider5="yogesh"

if riders==rider1:
   print((riders_details[0][::]))
   print("CAB will be coming in 10 mins")
elif riders==rider2:
   print((riders_details[1][::])),
   print("CAB will be coming in 20 mins")
elif riders==rider3:
   print((riders_details[2][::])),
   print("AUTO will be coming in 12 mins")
elif riders==rider4:
   print ((riders_details[3][::])) ,
   print("CAB will be coming in 10 mins")
elif riders==rider5:
   print((riders_details[4][::])),  
   print("AUTO will be coming in 15 mins")
else:
    print("🚫NO SERVICES AVAILABLE TO YOUR DESTINATION LOCATION")

# OTP
print("****please ...⏳wait for the OTP verification****")
mobile_number=int(input("enter the mobile number"))
if mobile_number<=10:
    print("🆗correct")
    print("check the OTP")
else:
    print("incorrect number ")
print("check your input📩 message")
otp=int(input("enter the OTP number"))
if otp==1107:
    print("1107 is your OTP for the ola verification of phone number ")
else:
    print("🚫invaid")


# PAYMENT
payment=input("which way you want to pay")
if payment=="cash":
    print("u have to pay in 💷cash amount")
if payment=="UPI":
    print("you have to swipe the 💳card")
if payment=="googlpay":
    print("scan the QR code")


# FEEDBACK
feedback=input("how many 🌟 you have to give this ride")
if feedback=="*****":
    print("👍👍👍excellent!")
if feedback=="****":
    print("👍👍very good")
if feedback=="***":
    print("👍good")
if feedback=="**":
    print("👎bad")
if feedback=="*":
    print("😑ugly")
elif feedback=="complaint":
    print("i want to apologize for your mismanagement")
responce=input("enter your feedback")
print(responce)

print("*************thanks for visit**********")
# print("*************have a good day**********")/

