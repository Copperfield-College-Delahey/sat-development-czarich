# Cozy Mind Study App 
import customtkinter as ctk

app = ctk.CTk()
app.title("Cozy Mind Study App")
app.geometry("1500x750")
# Configure app window grid 
app.grid_rowconfigure(0, weight=0) #Top frame - fixed height 
app.grid_columnconfigure(0, weight=1) #Main content:expands
# Top Navigation Bar 
topFrame = ctk.CTkFrame(app, height= 100)
topFrame.grid(row=0, column=0, sticky="ew")
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_rowconfigure(0, weight=1)
topFrame.grid_rowconfigure(1, weight=1)
titleLabel= ctk.CTkLabel (topFrame, text="Cozy Mind", font=("Belleza", 30))
titleLabel.grid(row=0, column=0, sticky="w", padx=15, pady=15)
menuButtonFrame=ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=1, column=0, sticky="se")
tasksButton=ctk.CTkButton(menuButtonFrame, text_color="black", text="Tasks List", font=("Belleza", 16), corner_radius=10, height=40, width=110, fg_color= "#6dc6e6", hover_color="#e6b7c9", cursor= "hand2")
tasksButton.grid(row=1, column=1, sticky="w",  padx=5)
tasksButton=ctk.CTkButton(menuButtonFrame, text_color="black", text="Edit Theme", font=("Belleza", 16), corner_radius=10, height=40, width=110, fg_color="#6dc6e6", hover_color="#e6b7c9", cursor= "hand2")
tasksButton.grid(row=1, column=2,sticky="w", padx=5)
tasksButton=ctk.CTkButton(menuButtonFrame, text_color="black", text="Progress Tracker", font=("Belleza", 16), corner_radius=10, height=40, width=110, fg_color="#6dc6e6", hover_color="#e6b7c9", cursor="hand2")
tasksButton.grid(row=1, column=3,sticky="w", padx=5)
tasksButton=ctk.CTkButton(menuButtonFrame, text_color="black",  text="Pomodoro Timer", font=("Belleza", 16), corner_radius=10, height=40, width=110, fg_color="#6dc6e6", hover_color="#e6b7c9", cursor="hand2")
tasksButton.grid(row=1, column=4,sticky="w", padx=5)
tasksButton=ctk.CTkButton(menuButtonFrame, text_color="black", text="⚙️ Settings", font=("Belleza",16), corner_radius=10, height=40, width=110, fg_color="#6dc6e6", hover_color="#e6b7c9", cursor="hand2")
tasksButton.grid(row=1, column=5, sticky="w", padx=5)
# Main Content Area 
mainFrame = ctk.CTkFrame(app)
mainFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
mainFrame.grid_rowconfigure(0, weight=1)
mainFrame.grid_rowconfigure(4, weight=0) #Add this line 
mainFrame.grid_columnconfigure(0, weight=1)
# Configure the timer frame to align left
timerFrame=ctk.CTkFrame(mainFrame, width=350, height=400, fg_color="#d3d3d3")
timerFrame.grid(row=0, column=0, sticky="nw", padx=2, pady=2)
timerFrame.grid_rowconfigure(0, weight=1)
timerFrame.grid_columnconfigure(0, weight=1)
#Create a circular frame for the timer 
circularFrame= ctk.CTkFrame(timerFrame,
                            width=200,
                            height=200,
                            corner_radius=100, #Makes it circular
                            fg_color="#f5e6a3", #Light brown color 
                            border_width=4,
                            border_color="#d4a574") #Darker brown border
circularFrame.grid(row=0, column=0, padx=20, pady=20)
circularFrame.grid_propagate(False) #Maintain the size 
circularFrame.grid_rowconfigure(0, weight=1)
circularFrame.grid_columnconfigure(0, weight=1)

timerLabel = ctk.CTkLabel(circularFrame,
                          text="25:00", 
                          font=("Consolas", 36), 
                          text_color="#5d4e37")
timerLabel.grid(row=0, column=0)

controlsFrame = ctk.CTkFrame(timerFrame)
controlsFrame.grid(row=1, column=0, pady=10)
pauseButton = ctk.CTkButton(controlsFrame, text_color="black", font=("Belleza", 30), text ="⏸️", width=60, height=50, corner_radius=25, fg_color="#87CEEB", hover_color="#7BC4E8", border_width=0)
pauseButton.grid (row=0, column=0, padx=15, pady=10)
heartButton = ctk.CTkButton(controlsFrame, text_color="pink", font=("Belleza", 30), text="🩷", width=60, height=50, fg_color="#fd9ef8", hover_color="#6dc6e6", border_width=0 )
heartButton.grid (row=0, column=1, padx=15, pady=10)
coffeeButton = ctk.CTkButton(controlsFrame, text_color="brown", font=("Belleza", 30), text="☕", width=60, height=50,  fg_color="#dab185", hover_color="#6dc6e6", border_width=0)
coffeeButton.grid(row=0, column=2,padx=15, pady=10)

# Progress Tracker Frame 
progressFrame=ctk.CTkFrame(mainFrame, width=300, height=200)
progressFrame.grid(row=0, column=1, sticky="ne", padx=20, pady=20)
progressFrame.grid_rowconfigure((0,1,2,3,4), weight=1)
progressFrame.grid_columnconfigure((0,1), weight=1)
# Progress Tracker Title
progressTitle=ctk.CTkLabel(progressFrame, text="Progress Tracker", font=("Belleza", 18, "bold"), text_color="black")
progressTitle.grid(row=0, column=0, columnspan=2, pady=10)
# Date Label 
dateLabel=ctk.CTkLabel(progressFrame, text="05/06/2025", font=("Monospace", 12), text_color="black")
dateLabel.grid(row=1, column=0, columnspan=2, sticky="w", padx=20)
# Subjects 
psychologyLabel=ctk.CTkLabel(progressFrame, text="✅ Psychology", font=("Monoid", 18),text_color="black")
psychologyLabel.grid(row=2, column=0, sticky="w", padx=20, pady=5)
psychologyStatus= ctk.CTkLabel(progressFrame, text="DONE", font=("Arial", 12, "bold"), text_color="white", fg_color="#ff6b6b", corner_radius=10, width=60, height=20)
psychologyStatus.grid(row=2, column=1, sticky="e", padx=20, pady=5)

englishLabel=ctk.CTkLabel(progressFrame, text="⏳ English", font=("Monoid", 18), text_color="black")
englishLabel.grid(row=3, column=0, sticky="w", padx=20, pady=5)
englishStatus= ctk.CTkLabel(progressFrame, text="IN PROGRESS", font=("Arial", 12, "bold"), text_color="white", fg_color="#ff6b6b", corner_radius=10, width=60, height=20)
englishStatus.grid(row=3, column=1, sticky="e", padx=20, pady=5)

mathLabel=ctk.CTkLabel(progressFrame, text="🔲 Math", font=("Monoid", 18), text_color="black")
mathLabel.grid(row=4, column=0, sticky="w", padx=20, pady=5)
mathStatus= ctk.CTkLabel(progressFrame, text="NOT STARTED/NOT DONE", font=("Arial", 12, "bold"), text_color="white", fg_color="#ff6b6b", corner_radius=10, width=60, height=20)
mathStatus.grid(row=4, column=1, sticky="e", padx=20, pady=5)
#Reminder 
reminderFrame=ctk.CTkFrame(mainFrame, fg_color="#f4eadf", corner_radius=10, width=200, height=180)
reminderFrame.grid(row=1, column=0, sticky="w", padx=20, pady=5)
# Cat emoji and REMEMBER bubble 
headerFrame=ctk.CTkFrame(reminderFrame, fg_color="#f5a6a6", corner_radius=15, width=180, height=35)
headerFrame.grid(row=0, column=0, padx=5, pady=5)
catLabel = ctk.CTkLabel(headerFrame, text="🐱", font=("Arial", 20))
catLabel.grid(row=0, column=0, padx=5, pady=5)
rememberLabel=ctk.CTkLabel(headerFrame, text="REMEMBER", font=("Arial", 20, "bold"), text_color="black")
rememberLabel.grid(row=0, column=1, padx=5, pady=5)
# Reminder text
reminderText=ctk.CTkLabel(reminderFrame, text="📌 Reminder! English Essay (due Tomorrow)", font=("MonaLisa", 15, "bold"), text_color="black")
reminderText.grid(row=1, column=0, padx=10, pady=5)
# Simple Settings Menu
settingsFrame=ctk.CTkFrame(mainFrame, fg_color="#f0d0b0", corner_radius=5, width=150, height=100)
settingsFrame.grid(row=1, column=1, padx=10, pady=10, sticky="w")
# Red/orange left border (using a thin frame)
borderFrame=ctk.CTkFrame(settingsFrame, fg_color="#ff6b6b",width=3, height=90)
borderFrame.grid(row=0, column=0, rowspan=4, padx=(5,0), sticky="nw")
# Settings title 
settingsTitle=ctk.CTkLabel(settingsFrame, text="Settings", font=("MonaLisa", 12, "bold"), text_color="black")
settingsTitle.grid(row=0, column=1, padx=10, pady=(5,2), sticky="w")
# Cozy Themes
cozyLabel=ctk.CTkLabel(settingsFrame, text="● Cozy Themes", font=("MonaLisa", 12), text_color="black")
cozyLabel.grid(row=1, column=1, padx=10, pady=1, sticky="w")
# Pastel Themes
pastelLabel=ctk.CTkLabel(settingsFrame, text="● Pastel Themes", font=("MonaLisa", 12), text_color="black")
pastelLabel.grid(row=2, column=1, padx=10, pady=1, sticky="w")
# Nuetral Themes
neutralLabel=ctk.CTkLabel(settingsFrame, text="● Pastel Themes", font=("MonaLisa", 12), text_color="black")
neutralLabel.grid(row=3, column=1, padx=10, pady=(1,5), sticky="w")
# Create the settings frame 
settingsFrame=ctk.CTkFrame(mainFrame, width=250, height=180, fg_color="#efc5ab", corner_radius=28)
settingsFrame.grid(row=0, column=4, padx=20, pady=20, sticky="n")
settingsIcon=ctk.CTkLabel(settingsFrame, text="⚙️", font=("Arial", 25))
settingsIcon.grid(row=0, column=0, padx=5, pady=10, sticky="w")
# Title Row with Icon 
settingsTitle=ctk.CTkLabel(settingsFrame, text="Settings", font=("MonaLisa", 20, "bold"))
settingsTitle.grid(row=0, column=1, padx=5, pady=10, sticky="w")
# First Switch: Notification
notificationSwitch = ctk.CTkSwitch(settingsFrame,
                                    text="Notification",
                                    onvalue="ON",
                                    offvalue="OFF",
                                    switch_width=50,
                                    switch_height=25,
                                    progress_color="#e08989",
                                    button_color="#fff3eb",
                                    fg_color="#e08989",
                                    font=("MonaLisa", 14))
notificationSwitch.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")
# Second Switch: Receive Notifications 
reminderSwitch=ctk.CTkSwitch(settingsFrame,
                            text="Receive Notifications",
                            onvalue="ON",
                            offvalue="OFF",
                            switch_width=50,
                            switch_height=25,
                            progress_color="#e08989",
                            button_color="#fff3eb",
                            fg_color="#e08989",
                            font=("MonaLisa", 14))
reminderSwitch.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="w")
# Task Lists Section 
taskListFrame=ctk.CTkFrame(mainFrame, fg_color="#f6e5cb", corner_radius=10, width=700, height=160)
taskListFrame.grid(row=1, column=4, padx=10, pady=10, sticky="nsew") # Use nsew to expand
taskListFrame.grid_columnconfigure(0, weight=1)
# Title 
taskTitle=ctk.CTkLabel(taskListFrame, text="Task List |", font=("MonaLisa", 16, "bold"), text_color="black")
taskTitle.grid(row=0, column=0, columnspan=2, padx=15, pady=(15, 10), sticky="w")
# Psychology section 
psychologyFrame=ctk.CTkFrame(taskListFrame, fg_color="#e6c7bd", corner_radius=8, width=250, height=35)
psychologyFrame.grid(row=1, column=0, padx=15, pady=(0, 5), sticky="ew")
psychologyIcon=ctk.CTkLabel(psychologyFrame, text="✅", font=("MonaLisa", 12, "bold"))
psychologyIcon.grid(row=0, column=0, padx=5, pady=5)
psychologyLabel=ctk.CTkLabel(psychologyFrame, text="●PSYCHOLOGY", font=("MonaLisa", 12, "bold"), text_color="black")
psychologyLabel.grid(row=0, column=1, padx=5, pady=5, sticky="w")
psychologyTask=ctk.CTkLabel(taskListFrame, text="● answer section question", font=("MonaLisa", 12), text_color="black")
psychologyTask.grid(row=2, column=0, padx=15, pady=2, sticky="w")
# English section
englishFrame=ctk.CTkFrame(taskListFrame, fg_color="#e6c7bd", corner_radius=8, width=250, height=35)
englishFrame.grid(row=3, column=0, padx=15, pady=(0, 5), sticky="ew")
englishIcon=ctk.CTkLabel(englishFrame, text="⏳", font=("MonaLisa", 12, "bold"))
englishIcon.grid(row=0, column=0, padx=5, pady=5)
englishLabel=ctk.CTkLabel(englishFrame, text="●ENGLISH", font=("MonaLisa", 12, "bold"), text_color="black")
englishLabel.grid(row=0, column=1, padx=5, pady=5, sticky="w")
englishTask=ctk.CTkLabel(taskListFrame, text="● write essay", font=("MonaLisa", 12), text_color="black")
englishTask.grid(row=4, column=0, padx=15, pady=2, sticky="w")
# Math section
mathFrame=ctk.CTkFrame(taskListFrame, fg_color="#e6c7bd", corner_radius=8, width=250, height=35)
mathFrame.grid(row=5, column=0, padx=15, pady=(0, 5), sticky="ew")
mathIcon=ctk.CTkLabel(mathFrame, text="🔲", font=("MonaLisa", 12, "bold"))
mathIcon.grid(row=0, column=0, padx=5, pady=5)
mathLabel=ctk.CTkLabel(mathFrame, text="●MATH", font=("MonaLisa", 12, "bold"), text_color="black")
mathLabel.grid(row=0, column=1, padx=5, pady=5, sticky="w")
mathTask=ctk.CTkLabel(taskListFrame, text="● answer 1A questions", font=("MonaLisa", 12), text_color="black")
mathTask.grid(row=6, column=0, columnspan=2, padx=15, pady=2, sticky="w")
# Add new task button 
addTaskButton=ctk.CTkButton(
    taskListFrame,
    text="➕ Add New Task",
    font=("MonaLisa", 12, "bold"),
    text_color="black",
    fg_color="gray",
    hover_color="#e6d7f0",
    width=120,
    height=25
)
addTaskButton.grid(row=7, column=0, columnspan=2, padx=15, pady=(10, 15), sticky="e")
app.mainloop()