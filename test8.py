import sqlite3


conn = sqlite3. connect('test10.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assingment( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT)")
    conn.commit()

conn.close()

    fileList = ('information.docx', 'hello.txt', 'myimage.png', \
                'mymovie.mpg','world.txt','data.pdf','myphoto.jpg')


conn = sqlite3.connect('test10.db')


with conn:

    cur = conn.cursor()
    for each file in fileList:
        if file.endswith(".txt"):
            execute statement to insert file into the table
    
conn.close()



conn = sqlite3.connect('test10.db')



with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_assingment")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "text file; {}\ntext file2: {}".format(item[0],item[1])
    print(msg)
