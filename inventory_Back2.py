import sqlite3

def MusicData():
    con=sqlite3.connect("Music.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Music(id INTEGER PRIMARY KEY,MusicID INTEGER,MusicEquip text, CompanyMus text,MusicNum INTEGER)") 
    con.commit()
    con.close()
def addMusicInfo(MusicID,MusicEquip, CompanyMus,MusicNum):
    con=sqlite3.connect("Music.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Music (id,MusicID,MusicEquip, CompanyMus,MusicNum) VALUES(NULL,?,?,?,?)",(MusicID,MusicEquip, CompanyMus,MusicNum))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("Music.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Music")
    rows=cur.fetchall()
    con.close()
    return rows
def deleteRec(id):
    con=sqlite3.connect("Music.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Music WHERE id=?",(id,))
    con.commit()
    con.close()
def searchdata(MusicID="",MusicEquip="", CompanyMus="",MusicNum=""):
    con=sqlite3.connect("Music.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Music WHERE MusicID=? OR MusicEquip=? OR CompanyMus=? OR MusicNum=?",(MusicID,MusicEquip, CompanyMus,MusicNum))
    rows=cur.fetchall()
    con.close()
    return rows
def dataUpdate(id,MusicID="",MusicEquip="", CompanyMus="",MusicNum=""):
    con=sqlite3.connect("Music.db")
    cur=con.cursor()
    cur.execute("UPDATE Music SET MusicID=? ,MusicEquip=?,CompanyMus=?,MusicNum=?,WHERE id=?",(MusicID,MusicEquip, CompanyMus,MusicNum,id))
    con.commit()
    con.close()


MusicData()
