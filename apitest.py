import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("covedresourcesapicreds.json", scope)
client = gspread.authorize(creds)
	
def get_data_from_sheet(sheetname="sheet1"):
	sheet = client.open(sheetname).sheet1
	data = sheet.get_all_records()
	return data,sheet

if __name__=='__main__':
	# resources = get_data_from_sheet()
	# print(len(resources),type(resources),type(resources[0]))
	# resources_math = resources_science = resources_chemistry_m =  resources_chemistry_nm = resources_physics_m = resources_physics_nm = []
	# resources_kidsmath = resources_general =resources_biology = resources_commerce = resources_arts = resources_cs =[]
	# for item in resources:
	# 	subjects = item.subject.split(",")
	# 	if 'm' in subjects:
	# 		resources_math.append(item)

	# for item in resources_math:
	# 	print (item.name)
	cell = get_data_from_sheet()
	print(cell.col)
