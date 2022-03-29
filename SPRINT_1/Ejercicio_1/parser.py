import csv
import sys


emails = []
users = []
errors = []
file = "random2.csv"

def parser_func(f):
	with open(file, 'r') as infile:
		reader = csv.reader(infile, delimiter=",")
		header = next(reader)
		row_num = 1 # teniendo en cuenta el header
		for row in reader:
			row_num += 1
			current = row_num
			try:
				email = row[0]
				name = row[1]
				user = row[2]
				if row[0] not in emails:
					users.append(user)
					emails.append(email)
				else:
					errors.append(f"duplicated mail, {row[0]} in line: {current}")
					print(errors, file=sys.stderr)
					return 0
			except:
				errors.append(f"Invalid data in line: {current}")
				print(errors, file=sys.stderr)
				return 0

		print(f"Se han procesado {row_num} lineas correctamente")
		return users


parser_func(file)