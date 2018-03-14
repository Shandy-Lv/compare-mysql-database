import getbaseinfo


db1 = getbaseinfo.get_database_connection_from_excel("db1.xlsx")
db2 = getbaseinfo.get_database_connection_from_excel("db2.xlsx")
cursor1 = db1.cursor()
cursor2 = db2.cursor()
db1_name = getbaseinfo.get_database_info_from_excel("db1.xlsx")['database']
db2_name = getbaseinfo.get_database_info_from_excel("db2.xlsx")['database']
file = open('Result.txt', 'w')
file.truncate()

cursor1.execute('SHOW TABLES')
cursor2.execute('SHOW TABLES')
tables1 = cursor1.fetchall()
tables2 = cursor2.fetchall()
list1 = [table for table in tables1 if table not in tables2]
if len(list1) != 0:
        print("Tables only in db1")
        file.write("Tables only in db1\n")
        for list in list1:
                print(list)
                file.write(str(list)+'\n')
list2 = [table for table in tables2 if table not in tables1]
if len(list2) != 0:
        print("Tables only in db2")
        file.write("Tables only in db2\n")
        for list in list2:
                print(list)
                file.write(str(list)+'\n')
file.write('\n')
print("differences between tables")
file.write("differences between tables"+'\n')
for table in tables1:
        if table not in list2 and table not in list1:
                cursor1.execute('DESC ' + table[0])
                cols1 = cursor1.fetchall()
                cursor2.execute('DESC ' + table[0])
                cols2 = cursor2.fetchall()
                wrote_table_name = True
                for col1 in cols1:
                        if col1 not in cols2:
                                if wrote_table_name:
                                        file.write('\n')
                                        file.write('Table Name：' + table[0] + '\n')
                                        file.write('\n')
                                        wrote_table_name = False
                                file.write('Field Name：'+col1[0] + '\n')
                                file.write('structure in db1:' + str(col1)+'\n')
                                for col2 in cols2:
                                        if col2[0] == col1[0]:
                                                file.write('structure in db2:' + str(col2)+'\n')
                                file.write('\n')
file.close()


