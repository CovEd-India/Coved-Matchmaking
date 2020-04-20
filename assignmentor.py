import get_data
from apitest import get_data_from_sheet
# insert code to read mentor spreadsheet and populate mentors list (initially set mentees = 0)
# insert code to read student spreadsheet and populate students list
#periodically read the student spreadsheet 
mentors,mentor_sheet = get_data.get_mentors()     # list of Mentor objects
students,mentee_sheet=get_data.get_mentees()     # list of student objects           


# def create_student_instance(self, name, email, feedbacktype, feedback_code=None, college_num, class_list, foreignuniv,subjects, hours, maxments,emotional,gender=None,emotype):
#     '''Creates a student entry in student dict'''
#     name=Student(name, email, feedbacktype, feedback_code=None, college_num, class_list, foreignuniv,subjects, hours, maxments,emotional,gender=None,emotype)
#     students.append(name)
    
    
def student_assign_mentor(student):
    '''Takes in a student instance as an input'''
    assignable_mentors=[]
    for mentor in mentors:
        if mentor.is_free():
            possible=True
            if student.assigned_mentor!=None and student.feedback_type==2:
                if student.assigned_mentor==mentor:
                    possible=False
            
            if not student.class_id in mentor.class_list:
                # print("2")
                possible=False
                continue

            for sub in student.subjects:
                if not (sub in mentor.subjects):
                    # print("3")
                    possible=False
                    continue

            if student.foreignuniv:
                if not mentor.foreignuniv:
                    # print("4")
                    possible=False
                    continue

            if student.extracurricular:
                if not mentor.emotional:
                    # print("5")
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
    assignable_mentors[0].assigned_students.append(student)
    mentor_sheet.update_cell(mentor_rowno,21,assignable_mentors[0].numberassigned)

    #Update mentee parameters
    student.assigned_mentor = assignable_mentors[0].name
    student_rowno = mentee_sheet.find(student.name).row
    mentee_sheet.update_cell(student_rowno,18,student.assigned_mentor)

    return assignable_mentors[0]


def student_feedback():
    for student in students:
        if student.feedback_type !=None:
        
            if student.feedback_type==1:
                pass
        #For both of these we'll haveto make an entry into some database regarding the changes
            elif student.feedback_type==2:
                del student.assigned_mentor.assigned_students[student.id]
                student.assigned_mentor=student_assign_mentor(student)
            elif student.feedback_type==3:
                student.assigned_mentor=student_assign_mentor(student)
                student.assigned_mentor.assigned_students[student.id]=student
        if student.assigned_mentor==None:
            student.assigned_mentor=student_assign_mentor(student)
            student.assigned_mentor.assigned_students[student.id]=student
                
        student.feedback_type=None
            
def mentor_feedback():
    for mentor in mentors:
        if mentor_feedback_type != None:
            
            if mentor.feedback_type==1:
                pass

            elif mentor.feedback_type==2:
                copydict=mentor.assigned_students.copy()
                for student_id in copydict:
                    if mentor.feedback_id==student_id:  
                        mentor.assigned_students[student_id].assigned_mentor=None
                        del mentor.assigned_students[student_id]
        mentor.feedback_type=None
        mentor.feedback_id=None


if __name__=='__main__':
    i=0
    for student in students:
        try:
            print(student_assign_mentor(student).name,student.name,i)
            i+=1
        except:
            print("no mentor found")


