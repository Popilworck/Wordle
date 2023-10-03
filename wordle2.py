from random import randrange as r
import os
fp = os.getcwd()
with open(rf"{fp}\WordList.txt","r") as f:
	a = f.read().splitlines()
b=r(0,len(a))
strword = a[b]
counter=0
print(strword)
word = list(strword)
#print(word) uncomment this to see the word chosen
while counter<6:
	choice = input("\nEnter Guess:\t").lower()
	#print(choice)
	if len(choice)!=5 :
		counter-=1
		print("WRONG NUMBER OF CHARACTERS. SHOULD BE EXACTLY 5. YOU ENTERED",len(choice))
		continue
	elif choice not in a:
		print("WORD NOT IN DICTIONARY")
		counter -=1
		continue
	elif choice == strword:
		print("Congrats. You have won the game")
		#messagebox.showinfo("Congrats", "You Have Correctly Guessed the Word")
		break
	c = list(choice)
	#print(c)
	d1= {i:word.count(i) for i in word}
	d2 = {i:c.count(i) for i in c}
	for i in range (5):
		if c[i] == word[i] :
				print('✅',end='')
		elif c[i] in word:
				if d1[c[i]]>=d2[c[i]]:	
					print('❔',end='')
				else:
					print('❌',end='')
		else:
			print('❌',end="")
	counter+=1
