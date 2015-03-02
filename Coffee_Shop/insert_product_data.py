import sqlite3

def insert_data(values):
	with sqlite3.connect("coffee_shop.db") as db:
		cursor = db.cursor()
		sql = "insert into Product (Name, Price) values (?,?)"
		cursor.execute(sql,values)
		db.commit()

if __name__ == "__main__":
	product = ("Expresso",1.5)
	products = [("Late",1.35),("Mocha",2.40),("Gree Tea",1.20),("Black Tea",1.00),("Americano",1.50)]
	for p in products:
		insert_data(p)