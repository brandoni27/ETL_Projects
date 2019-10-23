import csv

with open('/Users/Brando/Library/Preferences/PyCharm2018.3/scratches/attachment.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    emails = []

    for row in readCSV:
        email = row[0]
        emails.append(email)

new_emails = [ x + ',' for x in emails]
i = 1
while i < 210:
    print(new_emails[i], end='')
    i+=1