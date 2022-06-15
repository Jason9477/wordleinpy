import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import enchant
import os
import datetime
import time
import challenge
def GetAnswer():
    url = "https://www.stockq.org/life/wordle-answers.php"
    r = requests.request("GET", url)                #網頁請求
    soup=BeautifulSoup(r.text,"html.parser")        #利用bs4解析
    result=soup.find(id="today").find_next_siblings()   #尋找答案
    ans=result[2].text[-6:]
    return ans

ans=GetAnswer()
record = [[0 for i in range(5)] for j in range(6)]
dict={}
guesses =[ "" for i in range(6)]
d = enchant.Dict("en_US")
win=False
print("~WORDLE~    Attempts left:"+str(6)+"\n")
for i in range(6):
    if win==True:
        break
    check=True
    print("The letters you haven't guessed")
    for k in range(ord('A'), ord('Z') + 1):
        if chr(k) not in dict:
            print(chr(k), end=" ")
    print()
    while check:
        guess=input("Guess a word:") #得到使用者輸入
        if len(guess)==5:           #檢查是否為五字母
            if d.check(guess):       #檢查是否為一合法字
                check=False
            else:
                print(guess+" is not a word")
        else:
            print("Please enter a 5 letter word")
    os.system("clear")
    print("~WORDLE~    Attempts left:"+str(5-i)+"\n")
    guess=guess.upper()
    guesses[i]=guess
    for w in range(5):
        if guess[w] in ans:
            if guess[w] == ans[w]:
                record[i][w]=2  #字母正確且位置正確
            else:
                record[i][w]=1  #字母正確但位置不正確
            dict[guess[w]]=1
        else:
            record[i][w]=0      #字母錯誤
            dict[guess[w]]=0
    
    for j in range(i+1):
        print('-----------')
        print('|',end='')
        ss=''.join(str(_) for _ in record[j])
        if(ss)=="22222":
            for c in range(5):
                print(Back.GREEN+Fore.WHITE+guesses[j][c],end=Style.RESET_ALL+'|')
            win=True
        else:
            for c in range(5):
                if record[j][c]==0:
                    print(guesses[j][c],end='|')
                elif record[j][c]==1:
                    print(Back.YELLOW+guesses[j][c],end=Style.RESET_ALL+'|')
                else :
                    print(Back.GREEN+guesses[j][c],end=Style.RESET_ALL+'|')
        print()
    print("-----------")
    
print(Fore.GREEN+"You win!!") if win==True else print(Fore.RED+"You lose")
print(Style.RESET_ALL+"The answer is ",ans) 
challenge.MonthlyChallenge(win)