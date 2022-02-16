import sqlite3

DBNAME="chatbot"
T1="info"
T2="qa"


if __name__ == '__main__': 
	conn = sqlite3.connect(DBNAME) 
	c = conn.cursor() 
	c.execute(f"CREATE TABLE {T1} (i INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, info TEXT)") 
	c.execute(f"CREATE TABLE {T2} (i INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, question TEXT, answer TEXT)") 
	c.execute(f"CREATE INDEX id_comapny ON {T1} (id);")
	c.execute(f"CREATE INDEX id_qa ON {T2} (id);")
	conn.commit() 
	conn.close()
	
