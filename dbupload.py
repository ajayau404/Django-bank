#!/usr/bin/env python
import sys, os, json

# import MySQLdb
import re

import mysql.connector


# mycursor.execute("CREATE DATABASE mydatabase")
def filterData(text):
	# return ''.join([i if ord(i) < 128 else ' ' for i in text])
	reqStr = re.sub(r'[^\x00-\x7F]+',' ', text)
	reqStr = reqStr.replace('\xe2\x94\xac\xc3\xa1', '')
	return reqStr
def main():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="toor"
	)

	mycursor = mydb.cursor()
	# mycursor.execute("CREATE DATABASE mydatabase")
	# print("mycursor:", mycursor)

	with open("/home/kadmin/Documents/Ajay/fyle_src/indian_banks-master/bank_branches.csv", 'r') as fp:
		lineNo = 0
		errorCount = 0
		for eachLine in fp:
			lineNo += 1
			if lineNo == 1:
				continue
			# print eachLine
			try:
				splitQuote = eachLine.split('"')
				if len(splitQuote) < 2:
					continue
				splitQuote[1] = splitQuote[1].replace(',', ".")
				normanlLine = "".join(splitQuote)
				# print normanlLine
				normanlLine = normanlLine.split(',')
				# ifsc,bank_id,branch,address,city,district,state,bank_name
				INSERT_Q_DB= """INSERT INTO test.`branches` (ifsc,bank_id,branch,address,city,district,state) VALUES ("%s", %s, "%s", "%s" ,"%s", "%s", "%s");"""%(filterData(normanlLine[0]),
									filterData(normanlLine[1]),
									filterData(normanlLine[2]),
									filterData(normanlLine[3]),
									filterData(normanlLine[4]),
									filterData(normanlLine[5]),
									filterData(normanlLine[6]),
									# normanlLine[7],
									)
				# print "INSERT_Q_DB:", INSERT_Q_DB
				mycursor.execute(INSERT_Q_DB)
			except Exception as e:
				errorCount += 1
				# print e
				# print splitQuote, normanlLine
				# exc_type, exc_obj, exc_tb = sys.exc_info()
				# fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
				# print(exc_type, fname, exc_tb.tb_lineno)
				# print INSERT_Q_DB
				# sys.exit()
			# sys.exit()
		print "errorCount:",errorCount
		print "success count:", lineNo
		mydb.commit()

if __name__ == "__main__":
	main()