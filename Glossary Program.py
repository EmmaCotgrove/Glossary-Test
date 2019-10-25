import subprocess as sp
import time
words=[]
definitions=[]

def savedetails(name,score):
    studentrecord=open("studentrecords.txt","a")#a means append, r is read, w is write
    studentrecord.write(name+'\t')#adds the name and then a tab
    studentrecord.write(str(score))#converts the score to a string to append
    studentrecord.write('\n')#adds a new line
    studentrecord.close()#closes the file

def readfile():#allows us to just read in what is in the file
    studentrecord=open("studentrecords.txt","r")

    for arec in studentrecord:#for every record in the student record text file
        values = arec.split()#each value is saved into an array by being split up
        print("Name: ",values[0],"\t\tScore:",values[1])#shows the name and the score with tabs inbetween
    
    studentrecord.close()#closes the file

def searchfile():#allows us to search for a particular student
    print("Enter name")
    searchname=input()#gets the name from the user
    
    studentrecord=open("studentrecords.txt","r")#opens the file in read mode
    for arec in studentrecord:
        values = arec.split()
        if searchname==values[0]:#only if the record matches the search name will it display the results
            print("Name: ",values[0],"\nScore:",values[1])
    
    studentrecord.close()
    
def enterWords(): #allows the teacher to enter the words
    teacherWords=open("teacherWords.txt","w")
    for i in range(0,10):
        print("Enter word")
        w=input()
        w=w.lower()
        teacherWords.write(w)
        teacherWords.write('\t')#makes the words lower case and writes to file
        
        print("Enter definition")
        d=input()
        d=d.lower()
        teacherWords.write(d)
        teacherWords.write('\n')#makes the definitions lower case and writes to file
    
    teacherWords.close()

    
def showWords(): #shows the contents of the teacher words file to view the words and definitions
    teacherWords=open("teacherWords.txt","r")
    for aline in teacherWords:
        print (aline,end="") #shows the words and definitions in the file- each line
    teacherWords.close()
    input("\n\n Press any key to continue...")

def taketest():
    teacherWords=open("teacherWords.txt","r")
    score=0
    for arec in teacherWords:#for each record in the teacherwords file
        value = arec.split()#splits up the line i.e. record into words
        for i in range (1,len(value)):
            print(value[i], "",end="")#stops the next value from being written on the next line
        
        print("\nEnter spelling")
        guess=input()
        guess=guess.lower()#forces lowercase
        count=0

        if len(value[0])==len(guess):
            for j in range(0,len(value[0])):
                if guess[j]==value[0][j]:
                    count+=1
            
            if count==len(value[0]):#if correct then give 2 
                score+=2 
            elif count+1==len(value[0]):#if almost correct then give 1 
                score+=1   
            else:
                score+=0#if not correct then get 0
        sp.call('cls',shell=True)
    teacherWords.close()
    print(name,"Your Final Score is ",score)
    return(score)


def showmenu():#shows the menu on the screen
    print("""

            +++++++++++++++++++++++++++++++
                    SPELLING BEE
            +++++++++++++++++++++++++++++++

            1.  To enter words press 1
            2.  To take the test press 2
            3.  To read the student file press 3
            4.  To search the student file press 4
            5.  To show the words to learn press 5
            6.  To analyse data press 6
            0.  Press anything else to exit
    """)

def password():#teacher password
    print("Enter Password to Continue")
    passguess=input()
    if passguess=="teacherPass":
        return True

def studentpassword():#student password
    print("Enter password")
    password=input()

    if password=="student"+name:
        return True

def analyse():
    if password()==True:#teacher enters their password before continuing
        print("Enter name")
        searchname=input()
        temp=[]#sets a temporary array to empty
       
        studentrecord=open("studentrecords.txt","r")
        for arec in studentrecord:#searches for each entry for a student
            values = arec.split()
            if searchname==values[0]:
                temp.append(values[1])  #copies the results to the temp array
        studentrecord.close()

        if len(temp)==1:
            print("Not enough entries for comparison")
            time.sleep(3)
        else:
            progress=int(temp[-1])-int(temp[-2])#looks at the latest two entries in the array
            print(searchname,"has made",progress,"points of progress since last time")#identifies the precise amount of progress
            print("The latest score was:",temp[-1],"out of 20")#states the latest score for clarification
            time.sleep(3)
    
Finish=False
score=0

while Finish==False:#MAIN PROCEDURE
    sp.call('cls',shell=True)#clears the screen
    showmenu()
    answer=int(input())
    if answer==1:
        if password()==True:
            enterWords()
    elif answer==2:
        print("Enter your name")
        name=input()
        if studentpassword()==True:
            score=taketest()
            time.sleep(1)
            savedetails(name,score)
        input("\n\n Press any key to continue...")
    elif answer==3:
        readfile()
        input("\n\n Press any key to continue...")
    elif answer==4:
        searchfile()
        input("\n\n Press any key to continue...")
    elif answer==5:
        showWords()
    elif answer==6:
        analyse()
        input("\n\n Press any key to continue...")
    else:
        Finish=True


