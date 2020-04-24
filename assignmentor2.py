import get_data
from apitest import get_data_from_sheet
# insert code to read mentor spreadsheet and populate mentors list (initially set mentees = 0)
# insert code to read student spreadsheet and populate students list
#periodically read the student spreadsheet 
mentors,mentor_sheet = get_data.get_mentors()    # list of Mentor objects
students,mentee_sheet=get_data.get_mentees()     # list of student objects       


# def create_student_instance(self, name, email, feedbacktype, feedback_code=None, college_num, class_list, foreignuniv,subjects, hours, maxments,emotional,gender=None,emotype):
#    '''Creates a student entry in student dict'''
#    name=Student(name, email, feedbacktype, feedback_code=None, college_num, class_list, foreignuniv,subjects, hours, maxments,emotional,gender=None,emotype)
#    students.append(name)
    
    
def student_assign_mentor(student):
    '''Takes in a student instance as an input'''

    if student.assigned_mentor != None and student.feedback_type != 2 :
        return None

    assignable_mentors=[]
    for mentor in mentors:
        if mentor.is_free():
            score = 100 * (int(mentor.maxments) - int(mentor.numberassigned))     # high score means this mentor is a good match for student

            if student.assigned_mentor!=None and student.feedback_type==2:
                if student.assigned_mentor==mentor:
                    continue
            
            if not student.class_id in mentor.class_list:
                continue

            for sub in student.subjects:
                if not (sub in mentor.subjects):
                    continue

            if student.foreignuniv:
                if not mentor.foreignuniv:
                    score -= 600             # decide this value
            else :
                if mentor.foreignuniv :
                    score -= 600

            if student.extracurricular:
                if not mentor.emotional:
                    continue             # decide this value
                else:
                    if student.emotype not in mentor.emotype:
                        continue         # decide this value

            assignable_mentors.append([mentor, score])

        else :
            mentors.remove(mentor)
        # assignable_mentors=sorted(assignable_mentors)
    #update mentor parameters
    mentor_return = None
    max_score = -1000

    for ment in assignable_mentors :
        if (ment[1] > max_score) :
            max_score = ment[1]
            mentor_return = ment[0]

    if mentor_return is not None :

        #mentor_rowno = mentor_sheet.find(mentor_return.email).row
        mentor_return.numberassigned+=1
        mentor_return.assigned_students.append(student)
        mentor_sheet.update_cell(mentor_return.row_no,21,mentor_return.numberassigned)

        #Update mentee parameters
        student.assigned_mentor = mentor_return.name
        #student_rowno = mentee_sheet.find(student.name).row
        mentee_sheet.update_cell(student.row_no,22,student.assigned_mentor)
        mentee_sheet.update_cell(student.row_no,23,mentor_return.email)

        ## There is a limit of 100 requests per 100 seconds on free account. So use update_cell only when necessary
        # mentee_sheet.update_cell(student.row_no,19,mentor_return.email)
        # mentee_sheet.update_cell(student.row_no,20,"No")

    return mentor_return


# def student_feedback():
#     for student in students:
#         if student.feedback_type !=None:
        
#             if student.feedback_type==1:
#                 pass
#         #For both of these we'll haveto make an entry into some database regarding the changes
#             elif student.feedback_type==2:
#                 del student.assigned_mentor.assigned_students[student.id]
#                 student.assigned_mentor=student_assign_mentor(student)
#             elif student.feedback_type==3:
#                 student.assigned_mentor=student_assign_mentor(student)
#                 student.assigned_mentor.assigned_students[student.id]=student
#         if student.assigned_mentor==None:
#             student.assigned_mentor=student_assign_mentor(student)
#             student.assigned_mentor.assigned_students[student.id]=student
                
#         student.feedback_type=None
            
# def mentor_feedback():
#     for mentor in mentors:
#         if mentor_feedback_type != None:
            
#             if mentor.feedback_type==1:
#                 pass

#             elif mentor.feedback_type==2:
#                 copydict=mentor.assigned_students.copy()
#                 for student_id in copydict:
#                     if mentor.feedback_id==student_id:  
#                         mentor.assigned_students[student_id].assigned_mentor=None
#                         del mentor.assigned_students[student_id]
#         mentor.feedback_type=None
#         mentor.feedback_id=None


if __name__=='__main__':
    i=0
    for student in students:
        try:
            men = student_assign_mentor(student)
            if men is not None :
                print(men.name,student.name,i)
                i += 1
            else :
                print("No mentor found")
        except:
            print("Request limit exceeded (100 requests per 100 seconds). Try again after some time.")
            break


