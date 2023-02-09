import random

hello=["hi","Hi","there","hello","Hello","HELLO","Hey","hey"]
bye=["bye","take care","Goodbye"]
howru=["How are you","how are you"]

print('\n')
print("*******************Welcome to My Club-Ilyas-***********************")
while True:
    
    a=input('Guest:-')
    
    if a.lower() in hello:
        botans=["Hi,Can i help you?","Hi,Welcome","Hey"]
        print('Ilyas:-'+random.choice(botans)+'\n')
        
    elif a.lower() in bye:
        botans=["Bye","Take Care","Good Bye!","Have a Good Day!"]
        print('Ilyas:-'+random.choice(botans)+'\n')
        
    elif a.lower() in howru:
        botans=["i am fine! Hope you are feeling good as well?","I am feeling good! Hope you are feeling good as well"]
        print('Ilyas:-'+random.choice(botans)+'\n')
    else:
        print("SORRY!, I cant Understand")