
from tkinter import *
names = []

class Quiz:
    def __init__(self, parent):
 
        background_color="pale green"

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Python Quiz", font=("Tw Cen MT","20","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 
        self.var1=IntVar() 
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="enter name below", font=("Tw Cen MT","10"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="Whitesmoke", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)        
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner
      
           

if __name__ == "__main__":
    root = Tk()
    root.title("Python Quiz") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 
