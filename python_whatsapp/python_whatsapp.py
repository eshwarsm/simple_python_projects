import pywhatkit
phone = input('Enter phone number: ')
message = input('Enter your Message: ')
hour = input('Enter hour: ')
minute = input('Enter minute: ')
pywhatkit.sendwhatmsg(phone,message,int(hour),int(minute))
