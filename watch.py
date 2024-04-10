from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    lab_hour.config(text=hr)
    lab_minute.config(text=mi)
    lab_second.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hour.after(200,date_time)


clock = Tk()
clock.title('***Digital Clock***')
clock.geometry('1000x500')
clock.config(bg='grey')

# Hour, Minute, Second, and AM/PM Labels
lab_hour = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_hour.grid(row=0, column=0, padx=10, pady=10)

lab_minute = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_minute.grid(row=0, column=1, padx=10, pady=10)

lab_second = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_second.grid(row=0, column=2, padx=10, pady=10)

lab_am = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_am.grid(row=0, column=3, padx=10, pady=10)

# Date, Month, Year, and Day Labels
lab_date = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_date.grid(row=1, column=0, padx=10, pady=10)

lab_month = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_month.grid(row=1, column=1, padx=10, pady=10)

lab_year = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_year.grid(row=1, column=2, padx=10, pady=10)

lab_day = Label(clock, text="00", font=('Times New Roman', 60, "bold"), bg='black', fg="white")
lab_day.grid(row=1, column=3, padx=10, pady=10)

date_time()
clock.mainloop()
