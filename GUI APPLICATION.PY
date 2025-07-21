# Cozy Mind Study App 
import customtkinter as ctk

app = ctk.CTk()
app.title("Cozy Mind Study App")
app.geometry("1000x650")
# Configure app window grid 
app.grid_rowconfigure((0,1,2),weight=1) #Top frame - fixed height 
app.grid_columnconfigure(0, weight=1)
# Top Navigation Bar 
topFrame = ctk.CTkFrame(app, height= 80)
topFrame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
topFrame.grid_columnconfigure(0, weight=1)
titleLabel= ctk.CTkLabel (topFrame, text="Cozy Mind", font=("Belleza", 30))
titleLabel.grid(row=0, column=0, sticky="w", padx=15, pady=15)
menuButtonFrame=ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=1, column=0, sticky="se", padx=15, pady=15)
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
mainFrame.grid_columnconfigure(0, weight=1)
# Configure the timer frame to align left
timerFrame=ctk.CTkFrame(mainFrame)
timerFrame.grid(row=0, column=0, sticky="nw", padx=20, pady=20)
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
psychologyLabel=ctk.CTkLabel(progressFrame, text="✅ Psychology", font=("Monoid", 14),text_color="black")
psychologyLabel.grid(row=2, column=0, sticky="w", padx=20, pady=5)
psychologyStatus= ctk.CTkLabel(progressFrame, text="DONE", font=("Arial", 12, "bold"), text_color="white", fg_color="#ff6b6b", corner_radius=10, width=60, height=20)
psychologyStatus.grid(row=2, column=1, sticky="e", padx=20, pady=5)

englishLabel=ctk.CTkLabel(progressFrame, text="⏳ English", font=("Monoid", 14), text_color="black")
englishLabel.grid(row=3, column=0, sticky="w", padx=20, pady=5)
englishStatus= ctk.CTkLabel(progressFrame, text="IN PROGRESS", font=("Arial", 12, "bold"), text_color="white", fg_color="#ff6b6b", corner_radius=10, width=60, height=20)
englishStatus.grid(row=3, column=2, sticky="e", padx=20, pady=5)

mathLabel=ctk.CTkLabel(progressFrame, text="🔲 Math", font=("Monoid", 14), text_color="black")
mathLabel.grid(row=4, column=0, sticky="w", padx=20, pady=5)
mathStatus= ctk.CTkLabel(progressFrame, text="NOT STARTED/ NOT DONE", font=("Arial", 12, "bold"), text_color="white", fg_color="#ff6b6b", corner_radius=10, width=60, height=20)
mathStatus.grid(row=4, column=4, sticky="e", padx=20, pady=5)
app.mainloop()