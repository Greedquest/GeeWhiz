import csv

semantic_object_list = [red_light, green_light, etc.]

# want to create dictionary {'time_stamp' : time, 'red_light'}

with open('as_csv_test_file.csv', mode='w') as test_file:
    fieldnames = ['time_stamp']
    for each_so in semantic_object_list:
        fieldnames.append(each_so.meaning)

    my_writer = csv.DictWriter(test_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

    test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    test_writer.writerow(['John Smith', 'Accounting', 'November'])
    test_writer.writerow(['Erica Meyers', 'IT', 'March'])

import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['time_stamp']
    for each_so in semantic_object_list:
        fieldnames.append(each_so.meaning)


    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})