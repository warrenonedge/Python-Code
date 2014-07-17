class DBUpdater():
    def __init__(self, database):
		self.database = database

    def add(self, ID, firstName, lastName, address, city, state, zipCode, DOB):
        if ID in self.database:
            if (input("Do you want to update ID: {0}\nPress 'y' or 'n'".format(ID)) == 'y'):
                self.update(ID, firstName, lastName, address, city, state, zipCode, DOB)
            else:
                print("No Update Created")
        else:
            self.database[ID] = [firstName, lastName, address, city, state, zipCode, DOB]

    def update(self, ID, firstName, lastName, address, city, state, zipCode, DOB):
        self.database[ID] = [firstName, lastName, address, city, state, zipCode, DOB]

    def get(self, key):
        try:
            return self.database[key]
        except:
            print("ID does not exist")

    def items(self):
        return self.database.items()

    def keys(self):
        return self.database.keys()

    def values(self):
        return self.database.values()

    def pop(self,key):
        self.database.pop(key)

    def __len__(self):
        return len(self.database)
