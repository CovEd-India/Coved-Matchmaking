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
	data,_ = get_data_from_sheet()
	print(data)
