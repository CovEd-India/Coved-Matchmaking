import get_data

# insert code to read mentor spreadsheet and populate mentors list (initially set mentees = 0)
# insert code to read student spreadsheet and populate students list
#periodically read the student spreadsheet 
mentors = get_data.get_mentors()     # list of Mentor objects
students=get_data.get_mentees()     # list of student objects           



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
                    if student.emotype not in mentor.emotype:
                        possible=False
                        continue
            if possible:
                assignable_mentors.append(mentor)
    # assignable_mentors=sorted(assignable_mentors)
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
    for student in students:
        try:    
            print(student_assign_mentor(student).name,student.name)
        except:
            continue


