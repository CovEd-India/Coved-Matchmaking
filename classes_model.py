class_ids = {'6th to 10th' : 1, '11th and 12th (engineering)' : 2, '11th and 12th (medical)' : 3, '11th and 12th (arts)' : 4, \
             '11th and 12th (commerce)':5}
gender = {'Male': 0 , 'Female' : 1 , 'Prefer not to say' : 2}
feedback={"Yes, I am satisfied with my assignment and don't want to change it":1, "No, I want to be entered for reassignment (Please tell us a reason in the feedback form)":2, \
"Not applicable as I am applying for the first time or haven't been assigned yet":3}
emotype= {'Support regarding managing examination anxiety and stress':1,'Support regarding situations created by the corona virus pandemic':2,\
'General mental health related issues independent of the Covid-19 crisis':3}
sub_dict={'Mathematics':1,'Physics':2,'Chemistry':3,'Biology':4,'Science':5,'Language':6,'SST':7,'Commerce':8,'Arts':9}
college_tiers={'Any named college':1,'Any other government college':2, 'Any other private college':3}
foreign_dict= {"Yes":1,"No":0}
emotional = {"Yes":1,"No":0}
bool_dict ={"Yes":1,"No":0}


id1=1
id2=1

class Mentor(object):
    def _init_(self, name, email,college_num, class_list,foreignuniv,subjects, hours, maxments, emotional, emotype,feedbacktype=None,feedback_id=None,gender=None) :
        self.name = name #string
        self.id=id1
        id1=id1+1
        self.email = email #string
        self.feedbacktype=feedbacktype # int feedback[1,2,or 3]
        self.feedback_id=feedback_id
        self.college_num=college_num  #college is an integer , all college categories will be assigned an id.
        self.class_list = class_list # class_list is a list of integers. All classes have been assigned a unique id
        self.foreignuniv=foreignuniv  #boolean var
        self.hours = hours #int
        self.maxments=maxments #integer
        self.subjects=subjects #list of subjects numbers the mentor is interested in teaching
        self.emotional=emotional    #boolean var
        self.gender=gender      # int 0,1 or 2 use gender dict
        self.emotype=emotype  # list of emotypes they are comfortable in addressing, all ints
        self.assigned_students={} #dict of student_id:student_instance
    
    def _repr_(self):
        return self.name
    
    def _lt_ (self,other):
        if self.college_num != other.college_num:
            return self.college_num < other.college_num
        return self.mentees-1.5 *self.hours<other.mentees-1.5 * other.hours
    
    # def is_free (self):
    #     return len(self.assigned_students)<=int(self.maxments)
    
#    def assign_student (self,student):
#        ''' input is an instance of the student class'''
#        #create a random id using the python random module
#        match_id='Random generated id'
#        self.assigned_students[match_id]=student

    
                
class Student (object):
    def _init_(self, name, email, class_id,\
                 foreignuniv,subjects,extracurricular,emotype, gender=None, feedback_type=None) :
        self.name = name
        self.email = email
        self.id=id2
        id2=id2+1
        self.feedback_type=feedback_type  #(feedback[1,2,or 3])
        self.prevmatch_code=prevmatch_code #string code regarding the previous match
        self.class_id =class_id          # class_id is an int
        self.foreignuniv=foreignuniv    # bool var
        self.subjects= subjects      #list of subjects the student wants mentoring in, all ints
        self.mentorgender=gender    # int male=0 female =1 any=2
        self.emotype=emotype        # int using the emotype dictionary
        self.extracurr=extracurr         # bool var
        self.assigned_mentor=None
        
    def _repr_(self):
        return self.name