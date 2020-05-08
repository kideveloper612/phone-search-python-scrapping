import csv

file = open(file='filtered_US_06_05_todelivery2.txt', encoding='utf-8')
source = file.readlines()
file.close()


def write_phones(lines, file_name):
    with open(file_name, 'a', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(lines)
    csv_file.close()


total = []
for phone in source:
    striped_phone = phone.strip()
    if striped_phone not in total:
        total.append([striped_phone])
        print(len(total))

print('========================')
print('Source: ', len(source))
print('Not DUP: ', len(total))
write_phones(lines=total, file_name='dup_remove.csv')