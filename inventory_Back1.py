import sqlite3

def PEData():
    con=sqlite3.connect("Pe.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS PE(id INTEGER PRIMARY KEY,SportID INTEGER,SportEquip text, CompanySpo text,SportNum INTEGER)") 
    con.commit()
    con.close()
def addPEInfo(SportID,SportEquip, CompanySpo,SportNum):
    con=sqlite3.connect("Pe.db")
    cur=con.cursor()
    cur.execute("INSERT INTO PE (id,SportID,SportEquip, CompanySpo,SportNum) VALUES(NULL,?,?,?,?)",(SportID,SportEquip, CompanySpo,SportNum))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Pe.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM PE")
    rows=cur.fetchall()
    con.close()
    return rows
def deleteRec(id):
    con=sqlite3.connect("Pe.db")
    cur=con.cursor()
    cur.execute("DELETE FROM PE WHERE id=?",(id,))
    con.commit()
    con.close()
def searchdata(SportID="",SportEquip="", CompanySpo="",SportNum=""):
    con=sqlite3.connect("Pe.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM PE WHERE SportID=? OR SportEquip=? OR CompanySpo=? OR SportNum=?",(SportID,SportEquip, CompanySpo,SportNum))
    rows=cur.fetchall()
    con.close()
    return rows
def dataUpdate(id,SportID="",SportEquip="", CompanySpo="",SportNum=""):
    con=sqlite3.connect("Pe.db")
    cur=con.cursor()
    cur.execute("UPDATE PE SET SportID=? ,SportEquip=?,CompanySpo=?,SportNum=?,WHERE id=?",(SportID,SportEquip, CompanySpo,SportNum,id))
    con.commit()
    con.close()


PEData()
