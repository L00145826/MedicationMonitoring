#imports
import pyrebase
from tkinter import *

##variables

firebaseConfig = {
  "apiKey": "AIzaSyBpgjeUFiTnkw7bXeZt2d9eeqnL0nuEN-g",
  "authDomain": "medicationmonitoring-39ad3.firebaseapp.com",
  "databaseURL": "https://medicationmonitoring-39ad3-default-rtdb.firebaseio.com",
  "projectId": "medicationmonitoring-39ad3",
  "storageBucket": "medicationmonitoring-39ad3.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
 
};



firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()
db = firebase_storage.database()




morningHour = db.child("times").child("times needed").child("morningHour").get()
morningMinute = db.child("times").child("times needed").child("morningMinute").get()

afternoonHour = db.child("times").child("times needed").child("afternoonHour").get()
afternoonMinute = db.child("times").child("times needed").child("afternoonMinute").get()

nighttimeHour = db.child("times").child("times needed").child("nighttimeHour").get()
nighttimeMinute = db.child("times").child("times needed").child("nighttimeMinute").get()
#times = db.child("MzLSdzDkaGHNR0R81jc").get()

print(morningHour.val())
print(morningMinute.val())
print(afternoonHour.val())
print(afternoonMinute.val())
print(nighttimeHour.val())
print(nighttimeMinute.val())

#nighttimeMinute.val() = 49

#time =  {"morningHour": morningHour.val(),"morningMinute": morningMinute.val(),
#"afternoonHour": afternoonHour.val(),"afternoonMinute": afternoonMinute.val(),
#"nighttimeHour": nighttimeHour.val()),"nighttimeMinute": nighttimeMinute.val() } 


#upload
##storage.child("image.jpg").put("image.jpg")
#storage.child("nightimeHour)".put("nightimeHour")

#time =  {"morningHour": 9,"morningMinute": 30,
#"afternoonHour": 14,"afternoonMinute": 30,
#"nighttimeHour": 19,"nighttimeMinute": 30 } 

#
#db.child("times").child("times needed").set(time)
#db.push(time)

#storage.push(time)


mornval = morningHour.val()
mornmin = morningMinute.val()
afval =afternoonHour.val()
afminval = afternoonMinute.val()
nval = nighttimeHour.val()
nmin = nighttimeMinute.val()



# Create object
root = Tk()

# Adjust size
root.geometry("400x800")

morningHour = ""
morningMinute = ""
afternoonHour = ""
afternoonMinute = ""
nightimeHour = ""
nightimeMinute = ""
m=0

# decide if checkbox is needed or not
a = IntVar()
m = IntVar()
n = IntVar()



def show():
    morningHour = clicked.get()
    morningMinute = minuteclicked.get()
    label.config(text=morningHour)
    label.config(text=morningMinute)


# Dropdown menu options
options = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24"

]

minuteOptions = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"

]
# datatype of menu text
clicked = StringVar()
minuteclicked = StringVar()

# initial menu text

#print(morningHour.val())

clicked.set(mornval)
minuteclicked.set(mornmin)


# Create Dropdown menu

mo = Label(root, text="Morning Time: ")
mo.pack()
  
hourLabel = Label(root, text="Hour Time: ")
hourLabel.pack()
drop = OptionMenu(root, clicked, *options)
drop.pack()

minuteLabel = Label(root, text="Minute Time: ")
minuteLabel.pack()
minuteDrop = OptionMenu(root, minuteclicked, *minuteOptions)
#minuteDrop.config(height=20)
minuteDrop.pack()

def unshowmorningtime():
  
    drop.configure(state="disabled")
    minuteDrop.configure(state="disabled")
    # Create button, it will change label text
    #button = Button(root, text="Save Time for Morning Medication", command=show).pack()

def showmorningtime():
    if mornval == -1:
      clicked.set(0)
      minuteclicked.set(0)
    drop.configure(state="active")
    minuteDrop.configure(state="active")

def morningChange():

    if m.get() == 1:
        showmorningtime()
    if m.get() == 0:
        unshowmorningtime()
        infolabel=Label(root, text="No Morning Medication ")
        infolabel.pack()


if mornval ==-1:
  drop.configure(state="disabled")
  minuteDrop.configure(state="disabled")
  m.set(0);
else:
  m.set(1);

c = Checkbutton(root, text="Morning Medication", variable=m, command=morningChange)
c.pack()


def afternoonsSave():
    afternoonHour = afternoonclicked.get()
    afternoonMinute = afternoonminuteclicked.get()
    label.config(text=afternoonHour)
    label.config(text=afternoonMinute)


# Dropdown menu options
options = [
    "00",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24"

]

minuteOptions = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"

]
# datatype of menu text
afternoonclicked = StringVar()
afternoonminuteclicked = StringVar()

# initial menu text
afternoonclicked.set(afval)
afternoonminuteclicked.set(afminval)


# Create Dropdown menu

af = Label(root, text="Afternoon Time: ")
af.pack()
hourLabel = Label(root, text="Hour Time: ")
hourLabel.pack()
afternoondrop = OptionMenu(root, afternoonclicked, *options)
afternoondrop.pack()
minuteLabel = Label(root, text="Minute Time: ")
minuteLabel.pack()
afternoonminuteDrop = OptionMenu(root, afternoonminuteclicked, *minuteOptions)
afternoonminuteDrop.pack()

def unshowAfternoon():
    afternoondrop.configure(state="disabled")
    afternoonminuteDrop.configure(state="disabled")
    
def showAfternoon():
  if afval == -1:
    afternoonclicked.set(0)
    afternoonminuteclicked.set(0)
  afternoondrop.configure(state="active")
  afternoonminuteDrop.configure(state="active")
    # Create button, it will change label text
   # button = Button(root, text="Save Time for Afternoon Medication", command=afternoonsSave).pack()
  #drop.configure(state="disabled")
    #minuteDrop.configure(state="disable

#if a == 1:
 #   showAfternoon()

def afternoonChange():
    if a.get() == 1:
        showAfternoon()
    if a.get() ==0:
        unshowAfternoon()
        infoAfternoonlabel = Label(root, text="No Afternoon Medication ")
        infoAfternoonlabel.pack()

if afval ==-1:
  afternoondrop.configure(state="disabled")
  afternoonminuteDrop.configure(state="disabled")
  a.set(0);
else:
  a.set(1);

d = Checkbutton(root, text="Afternoon Medication", variable=a, command=afternoonChange)
d.pack()

def nighttimeSave():
    nightimeHour = nightimeclicked.get()
    nightimeMinute = nightimeminuteclicked.get()
    label.config(text=nightimeHour)
    label.config(text=nightimeMinute)


# Dropdown menu options
options = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24"

]

minuteOptions = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"

]
# datatype of menu text
nightimeclicked = StringVar()
nightimeminuteclicked = StringVar()

# initial menu text
nightimeclicked.set(nval)
#nightimeminuteclicked.set("0")
nightimeminuteclicked.set(nmin)



#save times to database
def saveTime():
    #c = str(clicked)
    ##get times from the checkboxes
    mornHr = int(clicked.get())
    mornmin = int(minuteclicked.get())
    aHr = int(afternoonclicked.get())
    aMin = int(afternoonminuteclicked.get())
    nHr = int(nightimeclicked.get())
    nMin = int(nightimeminuteclicked.get())
    #morning sets the morning values as -1 so they wont be used in the main program if the box is unchecked
    #it will ignore the value in the dropdown and upload -1 instead
    if a.get() == 0:
        aHr =-1
        aMin =-1
        
          #afternoon sets the afternoon values as -1 so they wont be used in the main program if the box is unchecked
    #it will ignore the value in the dropdown and upload -1 instead
    if n.get() == 0:
        nHr =-1
        nMin =-1
        
          #nighttime sets the nighttime values as -1 so they wont be used in the main program if the box is unchecked
    #it will ignore the value in the dropdown and upload -1 instead
    if m.get() == 0:
        mornHr =-1
        mornmin =-1
      
    db.child("times").child("times needed").update({"morningHour": mornHr,"morningMinute": mornmin,
    "afternoonHour": aHr,"afternoonMinute": aMin ,
    "nighttimeHour": nHr,"nighttimeMinute": nMin })
    
# Create Dropdown menu

ni = Label(root, text="Nighttime Time: ")
ni.pack()
    
hourLabel = Label(root, text="Hour Time: ")
hourLabel.pack()
nighttimeDrop = OptionMenu(root, nightimeclicked, *options)
nighttimeDrop.pack()

minuteLabel = Label(root, text="Minute Time: ")
minuteLabel.pack()
nighttimeminuteDrop = OptionMenu(root, nightimeminuteclicked, *minuteOptions)
nighttimeminuteDrop.pack()



def shownighttime():
    if nval == -1:
      nightimeclicked.set(0)
      nightimeminuteclicked.set(0)
    nighttimeDrop.configure(state="active")
    nighttimeminuteDrop.configure(state="active")
    
def unshownighttime():
    nighttimeDrop.configure(state="disabled")
    nighttimeminuteDrop.configure(state="disabled")
    #afternoonminuteDrop.configure(state="active")

# Create button, it will change label text



#if n == 1:
  #  shownighttime()


def nighttimeClick():
    if n.get() == 1:
        shownighttime()
    if n.get() == 0:
        unshownighttime()
        infoNighttimelabel = Label(root, text="No Nighttime Medication ")
        infoNighttimelabel.pack()

if nval ==-1:
  nighttimeDrop.configure(state="disabled")
  nighttimeminuteDrop.configure(state="disabled")
  n.set(0);
else:
  n.set(1);
e = Checkbutton(root, text="Nighttime Medication", variable=n, command=nighttimeClick)
e.pack()

button = Button(root, text="Save Time for Medication", command=saveTime).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()



