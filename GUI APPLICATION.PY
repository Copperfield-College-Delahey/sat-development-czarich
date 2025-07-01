# Cozy Mind Study App 
import customtkinter as ctk

app = ctk.CTk()
app.title("Cozy Mind Study App")
app.geometry("1000x650")
# Configure app window grid 
app.grid_rowconfigure((0,1,2),weight=1) #Top frame - fixed height 
app.grid_rowconfigure((0,1),weight=1) # Main content area- expandable 
app.grid_columnconfigure(0, weight=1)
# Top Navigation Bar 
topFrame = ctk.CTkFrame(app, height= 80)
topFrame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
topFrame.grid_columnconfigure(0, weight=1)
titleLabel= ctk.CTkLabel (topFrame, text="Cozy Mind Study App", font=("Belleza", 30))
titleLabel.grid(row=0, column=0, sticky="n", padx=15, pady=15)
titleLabel=ctk.CTkLabel(topFrame, text="Task List", font=("Belleza", 30))
titleLabel.grid(row=0, column=0, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Progress Tracker", font=("Belleza", 30))
titleLabel.grid(row=0, column=1, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Edit Theme", font=("Belleza", 30))
titleLabel.grid(row=0, column=2, sticky="ne", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Pomodoro Timer", font=("Belleza",30))
titleLabel.grid(row=0, column=3, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Settings", font=("Belleza", 30))
titleLabel.grid(row=0, column=4, sticky="n", padx=10, pady=10)

menuButtonFrame=ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=0, column=1, sticky="e", padx=15, pady=15)
tasksButton=ctk.CTkButton(menuButtonFrame, text="Tasks List", font=("Belleza", 16), height=40, width=110, fg_color= "#e6c7bd", hover_color="#f6e5cb", cursor= "hand2")
tasksButton.grid(row=0, column=0, padx=5)
tasksButton=ctk.CTkButton(menuButtonFrame, text="Progress Tracker", font=("Belleza", 16), height=40, width=140, fg_color="#e6c7bd", hover_color="#f6e5cb", cursor="hand2")
tasksButton.grid(row=0, column=1, padx=5)
app.mainloop()