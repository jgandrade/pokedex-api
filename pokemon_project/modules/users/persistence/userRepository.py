from pokemon_project.core.persistence.repository import Repository


class UserRepository(Repository):
    def save(self):
        return "test"

    def findById(self):
        return "test"
