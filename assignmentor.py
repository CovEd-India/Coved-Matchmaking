import get_data
from apitest import get_data_from_sheet
# insert code to read mentor spreadsheet and populate mentors list (initially set mentees = 0)
# insert code to read student spreadsheet and populate students list
#periodically read the student spreadsheet 
mentors,mentor_sheet = get_data.get_mentors()     # list of Mentor objects
students,mentee_sheet=get_data.get_mentees()     # list of student objects           

 
def student_assign_mentor(student):
    '''Takes in a student instance as an input'''
    assignable_mentors=[]
    for mentor in mentors:
        if mentor.is_free():
            possible=True
            if student.assigned_mentor!=None:
                print("Mentor already assigned")
                return

            if not student.class_id in mentor.class_list:
                possible=False
                continue

            for sub in student.subjects:
                if not (sub in mentor.subjects):
                    possible=False
                    continue

            if student.foreignuniv:
                if not mentor.foreignuniv:
                    possible=False
                    continue

            if student.extracurricular:
                if not mentor.emotional:
                    possible=False
                    continue
                else:
                    for emotype in student.emotype:
                        if emotype not in mentor.emotype:
                            possible=False
                            continue
            if possible:
                assignable_mentors.append(mentor)
    
    # assignable_mentors=sorted(assignable_mentors)     
    
    #update mentor parameters
    mentor_rowno = mentor_sheet.find(assignable_mentors[0].email).row
    assignable_mentors[0].numberassigned+=1
    assignable_mentors[0].assigned_students.append(student.name)        #Not in use at the moment though
    mentor_sheet.update_cell(mentor_rowno,21,assignable_mentors[0].numberassigned)

    #Update mentee parameters
    student.assigned_mentor = assignable_mentors[0].name
    student_rowno = mentee_sheet.find(student.name).row
    mentee_sheet.update_cell(student_rowno,18,student.assigned_mentor)
    mentee_sheet.update_cell(student_rowno,19,assignable_mentors[0].email)

    return assignable_mentors[0]


if __name__=='__main__':
    i=0
    for student in students:
        try:
            print(student_assign_mentor(student).name,student.name,i)
            i+=1
        except:
            print("no mentor found")


