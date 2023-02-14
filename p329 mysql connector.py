import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="chinmaypatel@8383")
mycur = mydb.cursor()
mycur.execute("use student1")

n = int(input("Enter the limit: "))
for i in range(n):
    id = str(input("Enter the id: "))
    name = str(input("Enter the name: "))
    gender = str(input("Enter the gender(M/F): "))
    colum_table = "insert into student1 values ('"+id+"', '"+name+"', '"+gender+"')"
    mycur.execute(colum_table)
    mydb.commit()

mycur.execute("select * from student1")
result = mycur.fetchall()
for x in result:
    print(*x)
print("")
