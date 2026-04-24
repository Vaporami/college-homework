class Recipe:
    def __init__(self, id, user_id, name, desc):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.desc = desc

    def get_array(self):
        return [self.id, self.user_id, self.name, self.desc]

class Ingredient:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get(self, as_array = True):
        if as_array:
            return [self.id, self.name]
        else:
            return {"id": self.id, "name": self.name}

class User:
    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password

    def get(self, as_array = True):
        if as_array:
            return [self.id, self.login, self.password]
        else:
            return {"id": self.id, "login": self.login, "password": self.password}
