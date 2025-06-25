# Cozy Mind Study App 
import customtkinter as ctk

app = ctk.CTk()
app.title("Cozy Mind Study App")
app.geometry("1000x650")
# Configure app window grid 
app.grid_rowconfigure((0,1,2),weight=1)
app.grid_rowconfigure((0,1),weight=1)
# Top Navigation Bar 
topFrame = ctk.CTkFrame(app, height= 60)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
topFrame.grid_columnconfigure((0,1,2,3,4), weight=1)
titleLabel= ctk.CTkLabel (topFrame, text="Cozy Mind Study App", font=("Belleza", 30))
titleLabel.grid(row=0, column=0, sticky="n", padx=15, pady=15)
titleLabel=ctk.CTkLabel(topFrame, text="Task List", font=("Belleza", 30))
titleLabel.grid(row=0, column=0, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Progress Tracker", font=("Belleza", 30))
titleLabel.grid(row=0, column=1, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Edit Theme", font=("Belleza", 30))
titleLabel.grid(row=0, column=2, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Pomodoro Timer", font=("Belleza",30))
titleLabel.grid(row=0, column=3, sticky="n", padx=10, pady=10)
titleLabel=ctk.CTkLabel(topFrame, text="Settings", font=("Belleza, 30"))
titleLabel.grid(row=0, column=4, sticky="n", padx=10, pady=10)
menuButtonFrame=ctk.CTkFrame(topFrame)
menuButtonFrame.grid(row=0, column=1, sticky="e", padx=15, pady=15)
searchPageButton=ctk.CTkButton(menuButtonFrame, text)
