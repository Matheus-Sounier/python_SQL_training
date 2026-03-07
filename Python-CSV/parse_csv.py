import csv
try:
    with open('Python-CS/names.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open('Python-CSV/new_names.csv', 'w') as new_file:
            header = ['email', 'last_name', 'first_name']
            
            csv_file = csv.DictWriter(new_file, fieldnames=header, delimiter='\t')
            
            csv_file.writeheader()

            # next(csv_reader)

            for lines in csv_reader:
                del lines['email']
                csv_file.writerow(lines)
except FileNotFoundError:
    print('File was not found')
except PermissionError:
    print('Permission denied')

        # fieldnames = ['first_name', 'last_name']

        # csv_file = csv.DictReader(new_file, fieldnames=fieldnames, delimiter='\t')

        # csv_file.writeheader()

        # for line in csv_reader:
        #     csv_file.writerow(line)

    # with open('Python-CSV/new_names.csv', 'w') as new_file:
    #     new_thing = csv.writer(new_file, delimiter='\t' )

    #     for line in csv_reader:
    #         new_thing.writerow(line)
