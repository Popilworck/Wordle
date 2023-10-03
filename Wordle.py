import random
with open("WordList.txt","r") as f:
    a=f.read().splitlines()
    b = random.randrange(0,len(a))
    word = a[b]
    print(word)
    counter=0
    while counter < 6:
        choice = input("\nEnter Guess:\t").lower()
        if len(choice)!=5 :
            counter-=1
            print("WRONG NUMBER OF CHARACTERS. SHOULD BE EXACTLY 5. YOU ENTERED",len(choice))
            continue
        elif choice not in a:
            print("WORD NOT IN DICTIONARY")
            counter -=1
            continue
        elif choice == word:
           print("Congrats. You have won the game")
           break
        
        for i in range(5):
            c = list(choice)
            word1 = list(word)
            d1= {i:word1.count(i) for i in word1}
            d2 = {i:c.count(i) for i in c}
            #print(d1,d2)
            for i in range (5):
                if c[i] == word1[i] :
                        print('/',end='')                    
                elif c[i] in word1:
                        if d1[c[i]]>d2[c[i]]:	
                            print('?',end='')
                        else:
                            print('x',end='')
                else:
                    print('x',end="")
        counter+=1