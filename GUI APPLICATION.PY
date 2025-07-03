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
mainFrame.grid_columnconfigure((0,1), weight=1)
mainFrame.grid_columnconfigure((0,1,2,3), weight=1)
# Pomodoro Timer (Left) - centered with circle
timerFrame = ctk.CTkFrame(mainFrame, fg_color="#f3f1ec")
timerFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
timerLabel = ctk.CTkLabel(timerFrame, text="25:00", font=("Times New Roman Condensed", 48))
timerLabel.grid(row=0, column=0, pady=30)
# Configure the timer frame to center content 
timerFrame.grid_rowconfigure(0, weight=1)
timerFrame.grid_columnconfigure(0, weight=1)
controlsFrame = ctk.CTkFrame(timerFrame)
controlsFrame.grid(row=1, column=0, pady=10)
pauseButton = ctk.CTkButton(controlsFrame, text_color="black", font=("Belleza", 30), text ="⏸️", width=60, height=50, fg_color="#f9f4f4", hover_color="#6dc6e6", border_width=0)
pauseButton.grid (row=0, column=0, padx=15, pady=10)
heartButton = ctk.CTkButton(controlsFrame, text_color="pink", font=("Belleza", 30), text="🩷", width=60, height=50, fg_color="#fd9ef8", hover_color="#6dc6e6", border_width=0 )
heartButton.grid (row=0, column=1, padx=15, pady=10)
coffeeButton = ctk.CTkButton(controlsFrame, text_color="brown", font=("Belleza", 30), text="☕", width=60, height=50,  fg_color="#dab185", hover_color="#6dc6e6", border_width=0)
coffeeButton.grid(row=0, column=2,padx=15, pady=10)
app.mainloop()