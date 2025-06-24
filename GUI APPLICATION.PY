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
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew")
topFrame.grid_columnfigure((0,1,2,3,4), weight=1)
