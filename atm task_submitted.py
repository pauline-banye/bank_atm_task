import locale
locale.setlocale(locale.LC_ALL, 'yo_NG')    

print ('')
name = input ("What is your name?  ")
allowedUsers = ['Pauline','Uche','Banye']
allowedPassword = ['passPa','passUc','passBa']

if(name in allowedUsers):
    password = input ("Your password?  ")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        import datetime
        dt = datetime.datetime.now()
        dt_string = dt.strftime("Date: %d/%m/%Y Time: %H:%M")
        print ('')
        print ('Welcome %s!' % name, end='\n\n')
        print ("Account accessed at") 
        print (dt_string, end='\n\n')
        
        print ('These are the available options:', end='\n\n')
        print ('1. Withdrawal')
        print ('2. Cash Deposit')
        print ('3. Complaint', end='\n\n')

        selectedOption = int(input('Please select an option:  '))                                 
        if (selectedOption == 1):
            #assumption1: mimimum and maximum withdrawal amount are ₦1000 and ₦50000 respectively
            print ('')
            withdrawal = int(input('How much would you like to withdraw?  '))
            print ('')
            if (withdrawal >= 1000) and (withdrawal <=50000):
                print ('Take your cash', end='\n\n')

            elif (withdrawal <= 1000):
                print ('Minimum withdrawal amount is 1000. Please try again. ', end='\n\n')    
            
            else:
                print ('Maximum withdrawal limit exceeded. Please try again. ', end='\n\n')    

        elif (selectedOption == 2):
            #assumtion2: Account balance is 9500000
            accountbal = 9500000
            print ('')
            depositamt = int(input('How much would you like to deposit?  '))
            accountbal += depositamt          
            print ('') 
            print ('Your current balance is', (locale.currency(accountbal, grouping=True)), end='\n\n')

        elif (selectedOption == 3):
            print ('')
            complaint = input('What issue will you like to report?  \n\n')
            print ('')
            print ('Thank you for contacting us.', end='\n\n')
            
        else:
            print('Invalid option selected! Please try again', end='\n\n')                                   
                               
    else:
        print('Password incorrect! Please try again', end='\n\n')

else:
    print ('Name not found! Please try again', end='\n\n')