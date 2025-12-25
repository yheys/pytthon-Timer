from tkinter import *
# -------CONSTANT-------#

PINK = "#FFC0CB"
RED = "#FF0000"
GREEN = "#00FF00"
YELLOW = "#FFFF00"
FONT_NAME="Courier"
WORK_MIN=1
SHORT_BREAK_TIME=5
LONG_BREAK_TIME=25
rep=0
time=None

                            #----------TIMER RESET-----------#
def reset( ):
    if time is not None:
        window.after_cancel(time)

    canvas.itemconfig(timer,text="00:00")
    lebel.config(text="Timer")
    check.config(text=" ")


                            #-------TIMER MECHANISM-----#

def star():
    global rep
    rep+=1
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_TIME*60
    long_sec=LONG_BREAK_TIME*60

    if rep%8==0:
        count_down(long_sec)
        lebel = Label(text="Long Break Time", fg=PINK, font=(FONT_NAME, 30), bg="#ffffff")

        lebel.config(padx=20, pady=20)
        lebel.grid(column=2, row=1)




    elif rep%2==0:
        count_down(short_sec)
        lebel = Label(text="Short Break Time", fg=RED, font=(FONT_NAME, 30), bg="#ffffff")

        lebel.config(padx=20, pady=20)
        lebel.grid(column=2, row=1)



    else:
        count_down(work_sec)

        lebel = Label(text="Working Time", fg=GREEN, font=(FONT_NAME, 30), bg="#ffffff")
        lebel.config(padx=20, pady=20)
        lebel.grid(column=2, row=1)





                            #--------COUNTDOWN MECHANISM-------------#
def count_down(count):
    count_min=count//60
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    if int(count_sec)<10 and int(count_sec)>0:
        count_sec=f"0{count_sec}"



    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global time
        time=window.after(1000,count_down,count-1)
    else :
        star()
        marks=" "
        for i in range(rep//2):
            marks+="✓"
        check.config(text=marks)




                            #--------------------UI SETUP--------------#


window=Tk()
window.title("Pomadoro")
window.config(padx=150,pady=150,bg="#ffffff")




canvas=Canvas(width=219,height=230, highlightthickness=0)
tomato_img=PhotoImage(file="download.png")
canvas.create_image(109.5,115,image=tomato_img)
timer=canvas.create_text(109,130, text="00:00",font=(FONT_NAME,20),fill="yellow")
canvas.grid(column=2,row=2)

lebel = Label(text="Timer", fg="yellow", font=(FONT_NAME, 30), bg="#ffffff")
lebel.config(padx=20, pady=20)
lebel.grid(column=2, row=1)




sb=Button(text="Start",font=(FONT_NAME,10),fg="black",bg="#ffffff", command=star)
sb.grid(column=1,row=3)

rb=Button(text="Reset",font=(FONT_NAME,10),fg="black",bg="#ffffff",command=reset)
rb.grid(column=3,row=3)

check = Label(text=" ", bg="#ffffff", font=(FONT_NAME, 20), fg=GREEN)
check.grid(column=2, row=6)


window.mainloop()