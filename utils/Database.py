import sqlite3

class Database():
	def __init__(self, dbname) -> None: 
		self.dbname = dbname

	def createTable(self, table_name):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor() 
		c.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, info TEXT, TEXT, characteristics TEXT)")
		conn.commit()
		conn.close()
	
	def insertInfo(self, table_name, id, text):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (None, id, text)) 
		conn.commit()
		conn.close()

	def updateInfo(self, table_name, id, text):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"Update {table_name} set info=? where id=?",(text, id))
		conn.commit()
		conn.close()

	def insertQA(self, table_name, id, question, answer):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", (None, id, question, answer)) 
		conn.commit()
		conn.close()

	def updateQA(self, table_name, id, question, answer):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"Update {table_name} set  = {question} where id = {id}")
		conn.commit()
		conn.close()

	def read(self, table_name):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name}")
		l = [list(row) for row in r]
		conn.close()
		return l
		
	def readColumn(self, table_name, column_name):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT {column_name} FROM {table_name}")
		l = [row[0] for row in r if row[0]!=None ]
		conn.close()
		return l
	def getRowById(self, table_name, id):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name} where id = ?", (id,))
		l = [row for row in r if row[0]!=None ]
		conn.close()
		return l
	
	def cleanData(self, table_name, id):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"DELETE FROM {table_name} WHERE id=?", (id,))
		conn.close()
		return l
	def getNumRows(self, table_name):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f'SELECT COUNT(*) from {table_name}') 
		result = c.fetchone() 
		return result[0]
	
	def getColumnsNames(self, table_name):
		columns = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		data = c.execute(f"SELECT * FROM {table_name}")
		for col in data.description:
			columns.append(col[0])
		return columns
		


