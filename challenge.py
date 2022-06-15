from copyreg import pickle
import datetime,calendar,time
import pickle
year=datetime.datetime.now().year
month=datetime.datetime.now().month
day=datetime.datetime.now().day
first=calendar.monthrange(year,month)
print(day)
def MonthlyChallenge(win):
    count=0
    l=[]
    with open ('outfile', 'rb') as fp:  #讀取二進位制檔案
        l = pickle.load(fp)             #利用pickle模組讀取
    if day==1:
        l.clear()
    for i in range(len(l),day-1):
        l.append(0)
    if(len(l)==day):
        l[-1]=(win+1)
    else:
        l.append(win+1)

    print('~Monthly Challenge~')
    print("su mo tu we th fr sa")
    for i in range(6):
        for j in range(7):
            if(count<=first[0]):
                print("  ",end=' ')
            else:
                try:
                    if l[count-first[0]-1]==2:      #勝利
                        print("🟩",end=' ') 
                    elif l[count-first[0]-1]==1:     #失敗
                        print("🟥",end=' ')
                    else:
                        print("⬛",end=' ')          #沒有資料
                except:
                    print('   ',end='')
            count+=1
        print('')
    
    with open('outfile', 'wb') as fp:
        pickle.dump(l, fp)                  #利用pickle寫入