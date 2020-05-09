import csv

class Customer():

    def __init__(self, ID, name, gender, birthday, email, active):
        self.id = ID
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.email = email
        self.active = active

        with open('customers.csv') as csv_reader:
            reader = csv.reader(csv_reader)
            header = next(reader)

            csv_customer = []
            for lines in reader:
                ID, name, gender, birthday, email, active = lines[0].split(';')
                customer = Customer(ID, name, gender, birthday, email, active)
                csv_customer.append(customer)

    Return_Attributes = lambda x: "{}, {}, {}, {}, {}, {}\n".format(x.id, x.name, x.gender, x.birthday, x.email, x.active)

    def Ativos(x):
        return True if x.active == 'True' else False

    csv_customer = []

    Active = list(filter(Ativos, csv_customer))

    Act = sorted(Active, key = lambda x: x.id)

    with open('actives.csv') as csv_reader:
        csv_reader.write('id, name, gender, birthday, email, active\n')
        csv_reader.writelines(list(map(Return_Attributes, Act)))


