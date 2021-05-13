# 정보시스템 분석 및 설계 팀 프로젝트
# Tkinter를 이용하여 랜덤 좌석 배치 프로그램 만들기

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog 
from tkinter.filedialog import *
import pandas as pd
from pandas import Series, DataFrame
import sqlite3
from IPython.display import display
from PIL import ImageGrab
import random
import numpy as np
df=pd.read_csv('final_data.csv')
con=sqlite3.connect("final.db")
df.to_sql('Class',con,if_exists='append',index=False)
con.commit()
cur=con.cursor()
cur.fetchall()


def apply():
    global s1,s3
    s1=s3
            
def saveFile(): 
    filename=filedialog.asksaveasfilename(initialdir="/",title="Select file",
                                         filetypes=(("pptx files","*.pptx"),("all files","*.*")))

def saveimage():
    box = (int(window.winfo_x()), int(window.winfo_y()), int(window.winfo_x())+1920, int(window.winfo_y())+1080)
    img=ImageGrab.grab(box) #창의 크기만큼만 이미지저장
    saveas='capture.png'
    img.save(saveas) # 이미지를 파일로 저장

def changepassword():
    change = Toplevel(window)
    global s5,s6,s7,s8,s9
    s5=StringVar()
    s6=StringVar()
    s7=StringVar()
    s8=StringVar()
    s9=StringVar()
    Label(change,text = "ID", width=10).grid(row=3, column=2)
    Label(change,text = "인증번호", width=20).grid(row=4, column=2)
    Label(change,text = "새로운 비밀번호", width=20).grid(row=5, column=2)
    Label(change,text = "새로운 비밀번호 확인", width=20).grid(row=6, column=2)
    Button(change,text="인증번호발송",width=10,command=email).grid(row=3,column=4)
    Button(change,text="변경 사항 저장",width=18, command=abcd).grid(row=7,column=3)
    Entry(change, width=10,textvariable = s5).grid(row=3, column=3)
    Entry(change, width=10,textvariable = s6).grid(row=4, column=3)
    Entry(change, width=10,textvariable = s7).grid(row=5, column=3)
    Entry(change, width=10,textvariable = s8).grid(row=6, column=3)

    
def click():
    global result, resultwin, b
    resultwin = Toplevel(window) # 새로운 창 띄우기
    entered_id = s1.get()
    entered_pw = s2.get()
    result = db_check(entered_id, entered_pw)
    print(result)
    if result == 0:
        Button(resultwin, text="패스워드가 틀렸습니다.", command = after_unlogin).pack()
    elif result==2:
        Button(resultwin, text="아이디가 틀렸습니다.", command = after_unlogin).pack()
    else:
        resultwin.protocol("WM_DELETE_WINDOW", ask_quit)

        def clickrandom():
            if var.get() == "데이터마이닝":
                data=pd.read_sql('SELECT name FROM Class WHERE subject="데이터마이닝" ', con)
                name=list(np.array(data).flatten())
                name = list(set(name))
                num_list = []
                for i in range(7,17):
                    for k in range(10):
                        globals()["entry{}_{}".format(i, k)].delete(0, END)
                        x = random.randint(0, len(name)-1)
                        if x not in num_list:
                            num_list.append(x)
                            globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))

            elif var.get() == "데이터 애널리틱스":
                data=pd.read_sql('SELECT name FROM Class WHERE subject="데이터애널리틱스" ', con)
                name=list(np.array(data).flatten())
                name = list(set(name))
                num_list = []
                for i in range(7,17):
                    for k in range(10):
                        globals()["entry{}_{}".format(i, k)].delete(0, END)
                        x = random.randint(0, len(name)-1)
                        if x not in num_list:
                            num_list.append(x)
                            globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))

            else:
                data=pd.read_sql('SELECT name FROM Class WHERE subject="정보시스템분석및설계" ', con)
                name=list(np.array(data).flatten())
                name = list(set(name))
                num_list = []
                for i in range(7,17):
                    for k in range(10):
                        globals()["entry{}_{}".format(i, k)].delete(0, END)
                        x = random.randint(0, len(name)-1)
                        if x not in num_list:
                            num_list.append(x)
                            globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
            
            messagebox.showinfo('좌석 배치 완료', "랜덤으로 배치되었습니다!")
                            
        # 시험기간 버튼 클릭 커맨드(체크박스 조건에 따라 달라지게 만듬)                
        def testrandom():
            if cVar1.get() == 1:
                if cVar2.get() == 0:
                    message = "1강의실 좌석을 배치합니다!"
                    if var.get() == "데이터마이닝":
                        data=pd.read_sql('SELECT name FROM Class WHERE subject="데이터마이닝" AND testroom =="1 강의실" ', con)
                        name=list(np.array(data).flatten())
                        name = list(set(name))
                        num_list = []
                        for i in range(7,17):
                            for k in range(10):
                                globals()["entry{}_{}".format(i, k)].delete(0, END)
                                x = random.randint(0, len(name)-1)
                                if x not in num_list:
                                    num_list.append(x)
                                    if k%2 == 0:
                                        globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
                                    else:
                                        pass
                                    
                    if var.get() == "데이터 애널리틱스":
                        data=pd.read_sql('SELECT name FROM Class WHERE subject="데이터애널리틱스" AND testroom =="1 강의실" ', con)
                        name=list(np.array(data).flatten())
                        name = list(set(name))
                        num_list = []
                        for i in range(7,17):
                            for k in range(10):
                                globals()["entry{}_{}".format(i, k)].delete(0, END)
                                x = random.randint(0, len(name)-1)
                                if x not in num_list:
                                    num_list.append(x)
                                    if k%2 == 0:
                                        globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
                                    else:
                                        pass
                    if var.get() == "정보시스템 분석 및 설계":
                        data=pd.read_sql('SELECT name FROM Class WHERE subject="정보시스템분석및설계" AND testroom =="1 강의실" ', con)
                        name=list(np.array(data).flatten())
                        name = list(set(name))
                        num_list = []
                        for i in range(7,17):
                            for k in range(10):
                                globals()["entry{}_{}".format(i, k)].delete(0, END)
                                x = random.randint(0, len(name)-1)
                                if x not in num_list:
                                    num_list.append(x)
                                    if k%2 == 0:
                                        globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
                                    else:
                                        pass
            if cVar1.get() == 0:
                if cVar2.get() == 1:
                    message = "2강의실 좌석을 배치합니다!"
                    if var.get() == "데이터마이닝":
                        data=pd.read_sql('SELECT name FROM Class WHERE subject="데이터마이닝" AND testroom =="2 강의실" ', con)
                        name=list(np.array(data).flatten())
                        name = list(set(name))
                        num_list = []
                        for i in range(7,17):
                            for k in range(10):
                                globals()["entry{}_{}".format(i, k)].delete(0, END)
                                x = random.randint(0, len(name)-1)
                                if x not in num_list:
                                    num_list.append(x)
                                    if k%2 == 0:
                                        globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
                                    else:
                                        pass
                    if var.get() == "데이터 애널리틱스":
                        data=pd.read_sql('SELECT name FROM Class WHERE subject="데이터애널리틱스" AND testroom =="2 강의실" ', con)
                        name=list(np.array(data).flatten())
                        name = list(set(name))
                        num_list = []
                        for i in range(7,17):
                            for k in range(10):
                                globals()["entry{}_{}".format(i, k)].delete(0, END)
                                x = random.randint(0, len(name)-1)
                                if x not in num_list:
                                    num_list.append(x)
                                    if k%2 == 0:
                                        globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
                                    else:
                                        pass
                    if var.get() == "정보시스템 분석 및 설계":
                        data=pd.read_sql('SELECT name FROM Class WHERE subject="정보시스템분석및설계" AND testroom =="2 강의실" ', con)
                        name=list(np.array(data).flatten())
                        name = list(set(name))
                        num_list = []
                        for i in range(7,17):
                            for k in range(10):
                                globals()["entry{}_{}".format(i, k)].delete(0, END)
                                x = random.randint(0, len(name)-1)
                                if x not in num_list:
                                    num_list.append(x)
                                    if k%2 == 0:
                                        globals()["entry{}_{}".format(i, k)].insert(END, str(name[x]))
                                    else:
                                        pass             
            if cVar1.get() == 0:
                if cVar2.get() == 0:
                    message = "체크가 되어있지 않습니다!"
            if cVar1.get() == 1:
                if cVar2.get() == 1:
                    message = "중복 체크입니다!"       
            messagebox.showinfo("Check Box", message)
      
        # 메뉴바 동작 함수
        def donothing():
            pass

        def openFile():
            global fname
            fname = askopenfilename(filetypes = (("CSV" , "*.csv"),("All Files","*.*")))
            messagebox.showinfo('Open File:', fname)
            loadData()

        def loadData(): 
            df_csv = pd.read_csv(fname, engine = "python") 
            display(df_csv)


        # 메뉴바 생성    
        menubar = Menu(resultwin)    
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=saveFile)
        filemenu.add_command(label="Capture",command=saveimage)
        filemenu.add_command(label="Close", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.quit)
        resultwin.config(menu=menubar)

        editmenu = Menu(menubar, tearoff=1)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Undo", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        helpmenu = Menu(menubar, tearoff=1)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="Help Index", command=help_index)
        helpmenu.add_command(label="About...", command=donothing)

        # 강의 선택 메뉴바 
        OptionList =[
            "데이터마이닝",
            "데이터 애널리틱스",
            "정보시스템 분석 및 설계"
        ]

        var = StringVar(resultwin)
        var.set(OptionList[0])

        opt = OptionMenu(resultwin, var, *OptionList)
        opt.grid(row = 1, column = 0, sticky = W)

        # 레이블
        Label(resultwin, text = "강의실 좌석 배치", font = (20)).grid(row = 2, column = 0)
        # 레이블
        Label(resultwin, text = "칠판").grid(row = 5, column = 0)

        
        seat = Frame(resultwin)
        seat.grid(row=6,column=0,sticky=W)
       
        # 좌석  테이블 
        for i in range(7,17):
            for k in range(10):
                globals()["entry{}_{}".format(i, k)] = Entry(seat, text = "")
                globals()["entry{}_{}".format(i, k)].grid(row = i, column = k, pady = 5, ipady = 8, ipadx = 6)


        # 랜덤 버튼

        btn = Button(resultwin, text = "랜덤 배치", command = clickrandom)
        btn.grid(sticky = W)

        cVar1 = IntVar()
        c1 = Checkbutton(resultwin, text="1 강의실", variable = cVar1)
        c1.grid(column=0, row=2, sticky = W)
        cVar2 = IntVar()
        c1 = Checkbutton(resultwin, text="2 강의실", variable = cVar2)
        c1.grid(column=0, row=3, sticky = W)

        action=Button(resultwin, text="시험기간 좌석 배치", command=testrandom)
        action.grid(column=0, row=4, sticky = W)
        
def db_check(entered_id, entered_pw):
    con = sqlite3.connect('student.db')
    cur = con.cursor()
    
    ID = entered_id
    password = entered_pw

    sql = "SELECT * FROM StudentInfo WHERE ID = %s" %(ID)

    try:
        cur.execute(sql)
        data = cur.fetchone()
        if data[2]==password:
            result = 1
        else:
            result = 0
    except:
        result=2
    
    return result

def after_unlogin():
    resultwin.destroy()
    ### 로그인 되지 않았을 때의 후작업
    
def ask_quit():
    if messagebox.askokcancel("Quit","종료하시겠습니까?"):
        resultwin.quit()
        resultwin.destroy()
        window.quit()
        window.destroy()



#헬프 인덱스
def help_index():        
    filewin = Toplevel(window)

    r=0
    c=0
    for help_text in help_msg_list: #help index
        help_table = Entry(filewin, text="", width="50")
        help_table.grid(row=r,column=c)
        help_table.insert(END,help_text)
        help_table.config(state='disabled')
        r=r+1

#어바웃 함수 선언  
def about():        
    filewin = Toplevel(window)

    r=0
    c=0
    for about_text in about_list: #about index
        about_msg = Entry(filewin, text="", width="30")
        about_msg.grid(row=r,column=c)
        about_msg.insert(END,about_text)
        about_msg.config(state='disabled')
        r=r+1    
    
window=Tk()
window.title("자리 랜덤 배치 시스템")
    
# Menu 생성하기
menubar = Menu(window)

menu_2=Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_radiobutton(label="Help Index",command=help_index)
menu_2.add_radiobutton(label="About ...",command=about)
menubar.add_cascade(label="Help", menu=menu_2)


window.config(menu=menubar)

help_msg_list=['Log-in',
    ' > 학번과 비밀번호를 입력하고 로그인 버튼을 클릭한다.',
    ' > 비밀번호를 모를 경우 비밀번호 찾기를 누른다',
               '자리 랜덤 배치',
    ' > 자리 배치를 원하는 과목을 클릭한 후 랜덤배치 버튼을 누른다',
            '강의실 별 시험기간 좌석 배치  ',
    ' > 시험기간 좌석 배치를 눌러 자리를 배치한다',
]

about_list=[
    '정보시스템 분석 및 설계 팀 프로젝트',
    '<자리 랜덤 배치 시스템>  홍윤표, 안윤정, 이승현, 이해철, 정재빈']



s1 = StringVar()
s2 = StringVar()
s4 = StringVar()
Label(window, text="학번").grid(row=0, column=1, sticky=W)
entry_id = Entry(window, textvariable = s1).grid(row=0, column=2, columnspan=2, sticky=W)
Label(window, text="패스워드").grid(row=1, column=1, sticky=W)
entry_pw = Entry(window, textvariable = s2, show='*').grid(row=1, column=2, columnspan=2, sticky=W)
Label(window,text="").grid(row=2,column=0)
Button(window, text="로그인", width=5, command=click).grid(row=3, column=2, sticky=W)
Button(window, text="PW찾기", width=5, command=changepassword).grid(row=3,column=2,sticky=E)
i=PhotoImage(file="pic.png")
label=Label(window, image=i).grid(row=4,column=0)

window.mainloop()
