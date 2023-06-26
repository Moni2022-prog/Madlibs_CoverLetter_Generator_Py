from tkinter import ttk
from tkinter import *

window = Tk()
window.title("MadLibs Generator for Cover Letter")
window.geometry('580x520')
window.resizable(False, False)


def madlib_coverLetter(win):
    def finish_madlib(tl:Toplevel,company_name,field_of_study,university, relevant_skills,
                       department,courses,your_name):
        
        let_text = f'''Dear Hiring Manager,

I am writing to express my strong interest in the internship position at {company_name}. As a highly motivated and ambitious {field_of_study} student, I am eager to apply my skills and contribute to the growth and success of your organization.
Throughout my academic journey at {university}, I have gained a solid foundation in {relevant_skills}. I have successfully completed coursework in {courses}, which has equipped me with a strong understanding of the concepts to utilise on field. I am confident that my 
theoretical knowledge, combined with my enthusiasm and dedication, make me a suitable candidate for this internship opportunity.What sets me apart is my strong passion for {department} field. 
I have actively engaged in attending industry conferences,participating in science and engineering clubs. 

Thank you for considering my application. I have attached my resume for your review, and I would welcome the opportunity to further discuss how my skills and experiences align with the internship position 
at {company_name}. I look forward to the possibility of contributing to the success of your organization. 
Sincerely,
{your_name}'''

        tl.geometry(newGeometry ='560x860')
        Label(tl, text='Your Cover Letter!!', font=("Times New Roman", 12, 'bold'), background='Gold',
              wraplength=tl.winfo_width()).place(x=0, y=240)
        Label(tl, text=let_text, font=("Times New Roman", 11, 'bold'), background='Gold',
              wraplength=tl.winfo_width()).place(x=0, y=260)
    
    madlib_tl = Toplevel(win, bg='Gold')
    madlib_tl.title("Cover Letter for You!")
    madlib_tl.geometry('560x860')
    madlib_tl.resizable(True,True)
    madlib_tl.maxsize(600,1000)

    Label(madlib_tl, text="Company Name",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=10)
    Label(madlib_tl, text="Undergrad/Grad Student",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=40)
    Label(madlib_tl, text="University",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=70)
    Label(madlib_tl, text="Relevant Skills",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=100)
    Label(madlib_tl, text="Courses",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=130)
    Label(madlib_tl, text="Department",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=160)
    Label(madlib_tl, text="Your Name",font=("Roboto",12,'bold'), bg='Gold').place(x=0, y=190)
    


    company_entry = Entry(madlib_tl, width=30)
    company_entry.place(x=280, y=10)
    university_entry = Entry(madlib_tl, width=30)
    university_entry.place(x=280, y=70)
    relevant_skills_entry= Entry(madlib_tl, width=30)
    relevant_skills_entry.place(x=280, y=100)
    your_name_entry = Entry(madlib_tl, width=30)
    your_name_entry.place(x=280, y=190)

    

    department = ['Software','Business Analytics', 'Data Science','Business Analyst','Data Analyst', 'HR', 
              'Business Development']
    courses = ['Software Engineering','Cybersecurity','Software Verification and Testing','Business Analytics',
           'Machine Learning','Operations Management', 'Business Analytics' ]
    field_of_study = ['Undergraduate', 'Graduate', 'Post-Graduate']


    field_of_study_opt = StringVar(madlib_tl)
    field_of_study_opt.set(field_of_study[0])
    OptionMenu(madlib_tl, field_of_study_opt, *field_of_study).place(x=280, y=40)

    courses_opt = StringVar(madlib_tl)
    courses_opt.set(courses[0])
    OptionMenu(madlib_tl, courses_opt, *courses).place(x=280, y=130)

    department_applying_opt = StringVar(madlib_tl)
    department_applying_opt.set(department[0])
    OptionMenu(madlib_tl, department_applying_opt, *department).place(x=280, y=160)

    submit_btn = Button(madlib_tl, text="Submit", background="SteelBlue", font=('Helvetica',12), 
                        command=lambda:finish_madlib(madlib_tl,company_entry.get(),field_of_study_opt.get(),
                                                    university_entry.get(), relevant_skills_entry.get(),
                                                    department_applying_opt.get(),courses_opt.get(), your_name_entry.get()))
    submit_btn.place(x=230, y=220)    
    
#Frame
window_frame = ttk.Frame(window, borderwidth=5, relief="raised", width=560, height=500)
window_frame.grid(column=0, row=0, columnspan=3)

#Label

Label(window, font=("Forte",20), text="Mad😉Libs Generator for Cover Letter").place(x=80, y=0)
Label(window, font=("Forte",16), text="Have Fun!").place(x=220, y=35)
Label(window, font=("Helvetica", 16), text="Push Me").place(x=230,y=280)

#mad-lib Button
ml_button = Button(window, text="Cover Letter", font=('Kalinga',22),bg= 'LightSkyBlue',
                   command=lambda:madlib_coverLetter(window))
ml_button.place(x=190, y=200)



    
window.mainloop()