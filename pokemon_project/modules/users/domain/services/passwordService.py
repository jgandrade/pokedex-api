import bcrypt


class PasswordService:
    def __init__(
        self, bcrypt_hash=bcrypt.hashpw, bcrypt_check=bcrypt.checkpw, password_rounds=10
    ):
        self.bcrypt_hash = bcrypt_hash
        self.bcrypt_check = bcrypt_check
        self.password_rounds = password_rounds

    def encrypt_password(self, password: str) -> dict:
        salt = bcrypt.gensalt(rounds=self.password_rounds)
        hashed_password = self.bcrypt_hash(password.encode(), salt).decode()
        return hashed_password

    def validate_password(self, from_password: str, to_password: str) -> bool:
        return self.bcrypt_check(from_password.encode(), to_password.encode())
