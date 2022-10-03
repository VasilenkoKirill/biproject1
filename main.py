name_ = 'name'
surname_ = 'surname'
father_ = 'father'
phone_ = 'phone'
email_ = 'email'


class Contacts:
    def __init__(self, file=str()):
        self.MyContact = []
        self.file = file

    def FILE(self, file):
        text = open(file, 'r', encoding='utf-8')
        for line in text:
            line = line.strip('\n')
            person = {surname_: None, name_: None, father_: None, phone_: None, email_: None}
            person_date = line.split(',')
            person_name = person_date[0].split()
            person_phone = person_date[1]
            person_email = person_date[2]
            if len(person_name) == 3:
                person[surname_] = person_name[0]
                person[name_] = person_name[1]
                person[father_] = person_name[2]
            elif len(person_name) == 2:
                person[surname_] = person_name[0]
                person[name_] = person_name[1]
            else:
                person[surname_] = person_name[0]
            if len(person_phone) != 0:
                person[phone_] = person_phone[1:]
            if len(person_email) != 0:
                person[email_] = person_email[1:]
            self.MyContact.append(person)

    def SearchPhone(self, phone=str()):
        FindPeraon = []
        for i in range(len(self.MyContact)):
            if self.MyContact[i][phone_] == phone:
                FindPeraon.append(i)
        return FindPeraon

    def SearchEmail(self, email=str()):
        FindPeraon = []
        for i in range(len(self.MyContact)):
            if self.MyContact[i][email_] == email:
                FindPeraon.append(i)
        return FindPeraon

    def SearchEmpty(self):
        FindPeraon = []
        for i in range(len(self.MyContact)):
            if self.MyContact[i][email_] is None or self.MyContact[i][phone_] is None:
                FindPeraon.append(i)
        return FindPeraon

    def SearchName(self, name=str()):
        name = name.split()
        FindPeraon = []
        if len(name) == 3:
            surname, name, father = name
            for i in range(len(self.MyContact)):
                if self.MyContact[i][surname_] == surname and self.MyContact[i][name_] == name and self.MyContact[i][
        father_] == father:
                    FindPeraon.append(i)
        if len(name) == 2:
            surname, name = name
            for i in range(len(self.MyContact)):
                if self.MyContact[i][surname_] == surname and self.MyContact[i][name_] == name:
                    FindPeraon.append(i)
        else:
            surname = name[0]
            for i in range(len(self.MyContact)):
                if self.MyContact[i][surname_] == surname:
                    FindPeraon.append(i)
        return FindPeraon

    def EditName(self, name=str(), id=int):
        name = name.split()
        if len(name) == 3:
            surname, name, father = name
            self.MyContact[id][name_] = name
            self.MyContact[id][father_] = father
            self.MyContact[id][surname_] = surname
        elif len(name) == 2:
            surname, name = name
            self.MyContact[id][name_] = name
            self.MyContact[id][father_] = None
            self.MyContact[id][surname_] = surname
        else:
            name = name[0]
            self.MyContact[id][surname_] = name
            self.MyContact[id][father_] = None
            self.MyContact[id][name_] = None

    def EditPhone(self, phone=str(), id=int):
        self.MyContact[id][phone_] = phone

    def EditEmail(self, email=str(), id=int):
        self.MyContact[id][email_] = email

    def Write(self, file=str()):
        text = open(file, 'w', encoding='utf-8')
        id = 0
        for id in range(len(self.MyContact)):
            line = str()
            if self.MyContact[id][surname_] is not None:
                line += self.MyContact[id][surname_]
            if self.MyContact[id][name_] is not None:
                line += ' ' + self.MyContact[id][name_]
            if self.MyContact[id][father_] is not None:
                line += ' ' + self.MyContact[id][father_]
            line += ','
            if self.MyContact[id][phone_] is not None:
                line += ' ' + self.MyContact[id][phone_]
            line += ','
            if self.MyContact[id][email_] is not None:
                line += ' ' + self.MyContact[id][email_]
            if id != len(self.MyContact):
                text.write(line + '\n')
            else:
                text.write(line)
            id += 1
        text.close()


class Command:
    def __init__(self, contact=Contacts()):
        self.contact = contact
        self.id = []

    def command(self, operation=int):
        self.id = []
        if operation == 1:
            operation = int(input('Enter number of search characteristic: 1) name, 2) phone, 3) email, 4) empty: '))
            if operation == 2:
                self.id = self.contact.SearchPhone(input('enter phone: '))
            elif operation == 3:
                self.id = self.contact.SearchEmail(input('enter email: '))
            elif operation == 4:
                self.id = self.contact.SearchEmpty()
            else:
                self.id = self.contact.SearchName(input('enter name: '))
            if len(self.id) == 0:
                print('no find person')
            else:
                for id in self.id:
                    if self.contact.MyContact[id][surname_] is not None:
                        print(self.contact.MyContact[id][surname_], end=" ")
                    if self.contact.MyContact[id][name_] is not None:
                        print(self.contact.MyContact[id][name_], end=" ")
                    if self.contact.MyContact[id][father_] is not None:
                        print(self.contact.MyContact[id][father_], end=" ")
                    if self.contact.MyContact[id][phone_] is not None:
                        print(self.contact.MyContact[id][phone_], end=" ")
                    if self.contact.MyContact[id][email_] is not None:
                        print(self.contact.MyContact[id][email_], end=" ")
                    print()
        elif operation == 2:
            id_ = -1
            operation = int(input('Enter number of search characteristic: 1) name, 2) phone, 3) email: '))
            if operation == 2:
                self.id = self.contact.SearchPhone(input('enter phone: '))
            elif operation == 3:
                self.id = self.contact.SearchEmail(input('enter email: '))
            else:
                self.id = self.contact.SearchName(input('enter name: '))
            if len(self.id) == 0:
                print('no find person')
            else:
                if len(self.id) > 1:
                    count = 1
                    for id in self.id:
                        print(str(count) + ') ', end="")
                        if self.contact.MyContact[id][surname_] is not None:
                            print(self.contact.MyContact[id][surname_], end=" ")
                        if self.contact.MyContact[id][name_] is not None:
                            print(self.contact.MyContact[id][name_], end=" ")
                        if self.contact.MyContact[id][father_] is not None:
                            print(self.contact.MyContact[id][father_], end=" ")
                        if self.contact.MyContact[id][phone_] is not None:
                            print(self.contact.MyContact[id][phone_], end=" ")
                        if self.contact.MyContact[id][email_] is not None:
                            print(self.contact.MyContact[id][email_], end=" ")
                        print()
                        count += 1
                    id = int(input('number of contact: '))
                    id_ = self.id[id - 1]
                else:
                    id_ = self.id[0]
                    if self.contact.MyContact[id_][surname_] is not None:
                        print(self.contact.MyContact[id_][surname_], end=" ")
                    if self.contact.MyContact[id_][name_] is not None:
                        print(self.contact.MyContact[id_][name_], end=" ")
                    if self.contact.MyContact[id_][father_] is not None:
                        print(self.contact.MyContact[id_][father_], end=" ")
                    if self.contact.MyContact[id_][phone_] is not None:
                        print(self.contact.MyContact[id_][phone_], end=" ")
                    if self.contact.MyContact[id_][email_] is not None:
                        print(self.contact.MyContact[id_][email_], end=" ")
                    print()
                operation = int(input('edit 1)name, 2)phone, 3)email'))
                if operation == 1:
                    self.contact.EditName(input('enter name: '), id_)
                elif operation == 2:
                    self.contact.EditPhone(input('enter phone: '), id_)
                else:
                    self.contact.EditEmail(input('enter email: '), id_)
                self.contact.Write(self.contact.file)


file = input('enter name of file: ')
my_contacts = Contacts(file)
my_contacts.FILE(file)
operation = int
while operation != 0:
    operation = int(input('1) search, 2) edit, 0) exit: '))
    command = Command(my_contacts)
    command.command(operation)
