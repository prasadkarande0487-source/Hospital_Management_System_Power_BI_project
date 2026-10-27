import mysql.connector
import pandas as pd 

data=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Radha@123",
    database="hospital_management_system"
)

if data.is_connected():
    print("Connected")
    
    
df=pd.read_sql("select * from patient",data)

df.to_excel(
    r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\patient.xlsx",
    index=False
)


df=pd.read_sql("select * from hospital",data)
df=pd.read_sql("select * from doctor",data)
df=pd.read_sql("select * from admission",data)
df=pd.read_sql("select * from appointment ",data)
df=pd.read_sql("select * from staffs",data)
df=pd.read_sql("select * from room",data)
df=pd.read_sql("select * from prescription",data)
df=pd.read_sql("select * from department",data)
df=pd.read_sql("select * from bill",data)
df=pd.read_sql("select * from lab_test",data)
df=pd.read_sql("select * from medicine",data)


df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\hospital.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\doctor.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\admission.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\appointment.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\staffs.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\room.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\prescription.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\bill.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\lab_test.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\medicine.xlsx",index=False)
df.to_excel(r"C:\Users\prasa\OneDrive\Desktop\Data_Analytics_Project\department.xlsx",index=False)

