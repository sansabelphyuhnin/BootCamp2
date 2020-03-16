import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('names.csv', 'w') as new_file:
		fieldnames = ['first_name',' ','last_name']

		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)

# .DictReader
# .DictWriter
# .writeheader
# .writerow



# Create_name.csv (the original file name)
# save_names.csv (htwt lr mae new file)
# ID shae sone htae py
# excel htae twin header htae py
# sepreate between first_name & last_name
# athit htwt lr mae exel file htae twin first_name last_name ta twl htae pr win ml