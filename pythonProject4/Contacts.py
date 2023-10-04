from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_contacts_list = []


def fio():
    for column in contacts_list[1:]:
        pattern_FIO = r'([А-Я])'
        sub_FIO = r' \1'
        line = column[0] + column[1] + column[2]
        if len((re.sub(pattern_FIO, sub_FIO, line).split())) == 3:
            for i in range(3):
                column[i] = re.sub(pattern_FIO, sub_FIO, line).split()[i]
        elif len((re.sub(pattern_FIO, sub_FIO, line).split())) == 2:
            column[0] = re.sub(pattern_FIO, sub_FIO, line).split()[0]
            column[1] = re.sub(pattern_FIO, sub_FIO, line).split()[1]
            column[2] = ''
        elif len((re.sub(pattern_FIO, sub_FIO, line).split())) == 1:
            column[0] = re.sub(pattern_FIO, sub_FIO, line).split()[0]
            column[1] = ''
            column[2] = ''


def phones():
    pattern_phone = (r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})(\d{2}|[s-]*)(\d{2})(\d{2}|[s-]*)(\d{2})(\s*)?(\(?(доб.)?\s?(\d+)\)?)?')
    sub_phone = r"+7(\2)\3-\5-\7\8\10\11"
    for column in contacts_list:
        column[5] = re.sub(pattern_phone, sub_phone, column[5], re.MULTILINE)


def duplicate():
    contacts_list_1 = contacts_list
    for column in contacts_list[1:]:
        for column_1 in contacts_list_1[1:]:
            if column[0] == column_1[0]:
                for i, col in zip(range(7), column):
                    if col == '':
                        column[i] = column_1[i]
    for contact in contacts_list:
        if contact not in new_contacts_list:
            new_contacts_list.append(contact)
    pprint(new_contacts_list)


if __name__ == '__main__':
    fio()
    phones()
    duplicate()

    with open("phonebook_2.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
