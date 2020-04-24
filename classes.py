class Mentor:
    def __init__(self, name, email, class_list,foreignuniv,subjects, maxments, emotional, assigned=0,emotype=None,feedback_type=None,feedback_id=None,gender=None, row_no = 0, college = 3) :
        self.name = name #string
        self.email = email #string
        self.feedback_type=feedback_type # int feedback[1,2,or 3]
        self.feedback_id=feedback_id
        self.class_list = class_list # class_list is a list of integers. All classes have been assigned a unique id
        self.foreignuniv=foreignuniv  #boolean var
        self.maxments=maxments #integer
        self.subjects=subjects #list of subjects numbers the mentor is interested in teaching
        self.emotional=emotional    #boolean var
        self.gender=gender      # int 0,1 or 2 use gender dict
        self.emotype=emotype  # list of emotypes they are comfortable in addressing, all ints
        self.assigned_students=[] #dict of student_id:student_instance
        self.numberassigned = assigned
        self.row_no = row_no
        self.college = college
    def is_free (self):
    	try:
            return int(self.numberassigned) < int(self.maxments)
    	except:
            print("----------------------Error ocuured in is_free function------------------")
            print(self.name, self.email)
            print("-------------------------------------------------------------------------")
    		return False


class Student:
    def __init__(self, name, email, class_id,\
                 foreignuniv,subjects,extracurricular,emotype=None, gender=None, feedback_type=None,assigned_mentor=None, row_no = 0) :
        self.name = name
        self.email = email
        self.feedback_type=feedback_type  #(feedback[1,2,or 3])
        # self.prevmatch_code=prevmatch_code #string code regarding the previous match
        self.class_id =class_id          # class_id is an int
        self.foreignuniv=foreignuniv    # bool var
        self.subjects= subjects      #list of subjects the student wants mentoring in, all ints
        self.mentorgender=gender    # int male=0 female =1 any=2
        self.emotype=emotype        # int using the emotype dictionary
        self.extracurricular=extracurricular         # bool var
        self.assigned_mentor= assigned_mentor   #Name of assigned Mentor
        self.row_no = row_no
        
    def repr(self):
        return self.name