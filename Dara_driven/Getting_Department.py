import requests
import pandas as pd

file_path ="//Users//mukund//Desktop//Temp_person_report.xlsx"

df = pd.read_excel(file_path)

for index,row in df.iterrows():
  mis_id =int(row["PersonId"])
  url = f"https://api.uat.bapsapps.org/myseva/api/v1/Person/FamilyMembersProfileMask?personId={mis_id}&includeAddressInfo=true"
  payload = {}
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ik5vbmUiLCJyZXF1ZXN0b3JpZCI6Ik5vbmUiLCJyZXNvdXJjZXVyaSI6IiIsImFkZGl0aW9uYWxpbmZvIjoiTm9uZSIsIm5vbmNlIjoiTm9uZSIsInVpZCI6ImVkNjhhODUwLWFiNTUtNGI5OS05MTIzLWIzOWRiOWJkYjEwNCIsInNpZCI6IjAyMzkxMDU1LTE1ZWEtNGEzMi1hMmViLTQ0MmY1ODlmMWNkMSIsImFpZCI6ImM4YTFlYmY3LTVlNGMtNDQ5Yi1hODA0LWEzMGJhZjQ0MjA1MCIsImNpZCI6IjA3NENFRjg0LTBEQjktNEEwNi1BQkY2LTZBRUQ2NDU0MjE5MSIsImF1dGgiOiJ2ZXJpZmllZCIsImZuIjoiSGl0ZXNoIiwibG4iOiJQYXRlbCIsInBpZCI6IjM3OTQiLCJjdCI6ImF0Iiwicm9sZSI6IlVuZGVmaW5lZCIsIm5iZiI6MTcyOTA5MDYzMSwiZXhwIjoxNzI5MDk3ODMxLCJpYXQiOjE3MjkwOTA2MzEsImlzcyI6Imh0dHBzOi8vYmFwcy5vcmciLCJhdWQiOiJNZW1iZXJzIn0.IDQj67syaoSeR6Sj10kkxesb4Yu90TIJ4nCuLE99GJQ',
    'x-baps-auth-app-id': '1',
    'x-baps-auth-user-id': '3794',
    'x-baps-auth-position-id': '55392',
    'x-baps-auth-role-id': '1',
    'CultureInfo': 'EN',
    'Origin': 'https://uat.baps.dev',
    'Connection': 'keep-alive',
    'Referer': 'https://uat.baps.dev/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  familyId = response.json()["data"][0]["familyId"]
  print(familyId)
  df.at[index,"Family_ID"]=familyId

df.to_excel(file_path,index=False)
