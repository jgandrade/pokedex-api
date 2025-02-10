from pokemon_project.core.persistence.mapper import Mapper


class UserMapper(Mapper):
    def toDomain(self):
        return "test"

    def toPersistence(self):
        return "test"
