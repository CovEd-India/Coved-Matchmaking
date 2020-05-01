from apitest import get_data_from_sheet
import classes_model
from classes import Mentor,Student



def get_mentors(sheetname = 'Copy of CovEd Mentor Form New copy'):
	mentors = []

	#variables containing the headings of columns in google forms. 
	name_head = 'Full Name:'
	email_head = 'Email Address'
	grade_head = 'What grades/levels are you comfortable tutoring?'
	foreign_univ_desc_head = "Some students have expressed interest in receiving help with College Applications for foreign universities (like essays and other stuff). Do you have experience in that area and would you be willing to help students with that?"
	maxments_head = "What's the maximum number of mentees you're willing to take at a given point?"
	subjects_head = "What subjects will you be comfortable in helping with?"
	emotional_head = "Will you be willing to provide students with extracurricular support pertaining to moral and emotional (Only proceed forward if your response here is yes):"
	emotype_head = "This is a copy of the question we will be asking students. Check all the boxes that you are comfortable with addressing?"
	feedback_type_head="If you are filling this form for the second time and have already been assigned a student, are you happy with the student assigned to you?"
	feedback_id_head = "Please provide the code ID that you have been assigned(E.g. E-111 or M-34 or X-45 etc.)(Note: If you are filling this form for the first time, write 'None')"
	gender_head = "What is your gender? (Note that we are providing this facility to students only in the case of them requiring emotional support as some issues can be sensitive. For general academic help this option will not be taken into account)"
	assigned_head="Assigned"
	unassigned_head="Unassigned"
	college_head = "What is the college you are or were affiliated with? Please note that we are only accepting responses from students pursuing college level studies (even if not physically going to a college) or have already graduated from college."

	
	#fetch data from sheet
	records,mentor_sheet = get_data_from_sheet(sheetname)
	row_no = 1

	for row in records:
		row_no += 1
		#For some cases, the values do not match what is given in the dictionary. 
		try:
			name = row[name_head]
			email = row[email_head]
			classes = [classes_model.class_ids[y.strip()] for y in row[grade_head].split(",")]	#split- assignmentor assumes list. strip- google forms appends whitespaces which can be difficult to keep in account
			foreignuniv = classes_model.foreign_dict[row[foreign_univ_desc_head] if row[foreign_univ_desc_head]!='' else 'No']	#some entries were blank in forms. 
			subjects = row[subjects_head].split(",")	#split- assignmentor assumes list. strip- google forms appends whitespaces which can be difficult to keep in account
			maxments = row[maxments_head]
			emotional = classes_model.emotional[row[emotional_head]]
			emotype = [classes_model.emotype[y.strip()] for y in row[emotype_head].split(",")]	#split- assignmentor assumes list. strip- google forms appends whitespaces which can be difficult to keep in account
			if 0 not in emotype :
				emotype.append(0)
			feedback_type = classes_model.feedback[row[feedback_type_head]]
			feedback_id = row[feedback_id_head]
			clg = classes_model.college_tiers[row[college_head]]

			if str(row[assigned_head]).replace(' ', '') == '':
				assigned = 0
			else:
				assigned = int(str(row[assigned_head]).replace(' ', ''))

			if str(row[unassigned_head]).replace(' ', '') == '':
				unassigned = 0
			else:
				unassigned = int(str(row[assigned_head]).replace(' ', ''))
			
			try:								#Made like this because some people have not filled gender even after saying Yes to support
				gender = classes_model.gender[row[gender_head]]
			except:
				gender = None

			#Initialise mentor object
			mentor_object = Mentor(name,email,classes,foreignuniv,subjects,maxments,emotional, assigned-unassigned,emotype,feedback_type,feedback_id,gender, row_no, clg)
			## Only the free mentors are returned to reduce time
			if mentor_object.is_free() :
				mentors.append(mentor_object)
			
		except:
			print("Some Error Occured : Mentor")
			print(row[name_head], row[email_head])
			print("\n#############################################\n")
			continue

		
	return mentors,mentor_sheet
	


def get_mentees(sheetname="Copy of CovEd student form (New) copy"):
	mentees = []

	#variables containing the headings of columns in google forms. 
	name_head = 'Full Name:'
	email_head = 'Email Address'
	grade_head ="What is your age group? (Repeaters in any particular stream please select the 11-12 option in the corresponding stream)"
	foreignuniv_head = "Some mentors have experience with College Applications for foreign universities (like essays and other stuff). Do you require some help with that? (Please select yes only if you are really considering applying to a foreign university soon)"
	subjects_head ="What subjects do you specifically need help with?"
	extracurricular_head = "Would you be interested in receiving extra curricular support from your mentor (Answer the next question only if your response to this question is Yes):"
	feedback_head ="If you are filling this form for the second time and have already been assigned a mentor, are you happy with the mentor assigned to you?"
	emotype_head = "Please select all the box pertaining to the area that you need support with with (once again please be considerate and only select something if you genuinely need help with it):"
	gender_head ="What is your gender? (Note that we are providing this facility only in the case of students requiring emotional support as some issues can be sensitive. For general academic help this option will not be taken into account)"
	assigned_mentor_head = "Mentor"

	#fetch data from sheet
	records,mentee_sheet= get_data_from_sheet(sheetname)

	row_no = 1

	for row in records:
		row_no += 1
		#For some cases, the values do not match what is given in the dictionary. 
		try:

			if row[assigned_mentor_head].replace(' ', '') == '':
				assigned_mentor=None
			else:
				assigned_mentor = row[assigned_mentor_head]

			feedback = classes_model.feedback[row[feedback_head]]

			## Appending only the unassigned students to save time
			if assigned_mentor != None and feedback != 2 :
				continue


			name = row[name_head]
			email = row[email_head]
			classes = classes_model.class_ids[row[grade_head]]
			foreignuniv = classes_model.bool_dict[row[foreignuniv_head] if row[foreignuniv_head]!='' else 'No']		#some entries were blank in forms. 
			subjects =  row[subjects_head].split(",")			#Assumed list in assignmentor
			extracurricular = classes_model.bool_dict[row[extracurricular_head]]
			if extracurricular:
				emotype = [classes_model.emotype[y.strip()] for y in row[emotype_head].split(",")]		#split- assignmentor assumes list. strip- google forms appends whitespaces which can be difficult to keep in account
				if 0 not in emotype :
					emotype.append(0)
			else:
				emotype= [0]

			try: 																	#Made like this because some people have not filled gender even after saying Yes to support
				gender = classes_model.gender[row[gender_head]]
			except:
				gender = None


			#Initialise mentee object
			student_object = Student(name,email,classes,foreignuniv,subjects,extracurricular,emotype=emotype,gender=gender,feedback_type=feedback,assigned_mentor=assigned_mentor, row_no = row_no)
			mentees.append(student_object)

		except:
			print("Some Error Occured : Student")
			print(row[name_head], row[email_head])
			print("\n#############################################\n")
			continue
	
	return mentees,mentee_sheet



if __name__=='__main__':
	mentors_list,_ = get_mentors()
	mentees_list,_ = get_mentees()
	print(len(mentors_list))
	print(len(mentees_list))

