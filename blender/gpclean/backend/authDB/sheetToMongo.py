import os
from pprint import pprint

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from db import reservation_collection


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credential_path = os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"]
spreadsheet_name = os.getenv("GOOGLE_SPREADSHEET_NAME", "PRFS reservation")
worksheet_name = os.getenv("GOOGLE_WORKSHEET_NAME")

creds = ServiceAccountCredentials.from_json_keyfile_name(credential_path, scope)
client = gspread.authorize(creds)

spreadsheet = client.open(spreadsheet_name)
sheet = spreadsheet.worksheet(worksheet_name) if worksheet_name else spreadsheet.sheet1

values = sheet.get_all_values()
pprint(values)
records = []

for row in values[2:]:
    time_slot = row[0]
    for i, student in enumerate(row[1:], start=1):
        day = values[1][i]
        student = student.strip()
        if student:
            found = False
            for rec in records:
                if student in rec:
                    rec[student].append(f"{day}_{time_slot}")
                    found = True
                    break
            if not found:
                records.append({student: [f"{day}_{time_slot}"]})

for record in records:
    for student_id, day_list in record.items():
        filter = {"student_id": student_id}
        if reservation_collection.find_one(filter):
            update = {"$push": {"days": {"$each": day_list}}}
            print("Existing reservation updated")
        else:
            doc = {"student_id": student_id, "days": day_list}
            update = {"$set": doc}
            print("New reservation registered")
        reservation_collection.update_one(filter, update, upsert=True)

print("MongoDB reservation sync complete")
