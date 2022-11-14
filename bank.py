#write a python program that computes the net amount of a bank account based on transaction log from console input
# format: W 200 D500
# W - withdrawl
# Deposit
log = []
balance = 1500

def Balance(): 
    global balance
    print("\nCurrent Balance is: %d" %(balance))

def Withdrawl(amount): 
    global balance
    balance -= amount
    print("\nWithdrew: %d" %amount)
    Balance()

def Deposit(amount): 
    global balance 
    balance += amount
    print("\nDeposited: %d" %amount)
    Balance()

def Transactions(): 
        for i in log:
            if( log[0] == "W"): 
                Withdrawl(log[1])
            elif(log[0] == "D"): 
                Deposit(log[1]) 

def Read():
        global balance 
        
        while True:
            data = input("\nEnter transaction details:") 
            if data == 'Exit' or data == 'exit': 
                Transactions()
                break
            log.append(data.split())
        

def main(): 
    print("\nWelcome")
    
    Balance()
    
    Read()

main()

    

