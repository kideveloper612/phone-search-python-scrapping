import csv

file = open(file='US0205.txt', encoding='utf-8')
source = file.readlines()
file.close()


f = open(file='US0205/pass_phones.csv', encoding='utf-8')
pass_phones = f.readlines()
f.close()


done_phones = []
for i in pass_phones:
    done_phones.append(i.strip())


def write_phones(lines, file_name):
    with open(file_name, 'a', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(lines)
    csv_file.close()


total = []
for phone in source:
    striped_phone = phone.strip()
    if striped_phone not in done_phones:
        total.append([striped_phone])
        print(len(total))

print('========================')
print('Pass: ', len(pass_phones))
print('Source: ', len(source))
print('Yet: ', len(total))
write_phones(lines=total, file_name='sort.csv')