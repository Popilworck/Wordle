with open("WordList.txt","r") as f:
	a = f.read().splitlines()
def main(strword,choice):
    word = list(strword)
        #print(choice)
    if len(choice)!=5 :
        #print("WRONG NUMBER OF CHARACTERS. SHOULD BE EXACTLY 5. YOU ENTERED",len(choice))
        return(0)
    elif choice not in a:
        #print("WORD NOT IN DICTIONARY")
        return(1)
    elif choice == strword:
        #print("Congrats. You have won the game")
        #messagebox.showinfo("Congrats", "You Have Correctly Guessed the Word")
        return(2)
    c = list(choice)
    d1= {i:word.count(i) for i in word}
    d2 = {i:c.count(i) for i in c}
    ching=[]
    for i in range (5):
        if c[i] == word[i] :
                ching.append(1)
        elif c[i] in word:
                if d1[c[i]]>=d2[c[i]]:	
                    ching.append(0)
                else:
                    ching.append(2)
        else:
            ching.append(2)
    return(ching)
if __name__ == '__main__':
     print(main('books','ploin'))
        