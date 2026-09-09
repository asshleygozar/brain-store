import bcrypt

class HashManager:
    @staticmethod
    def hash_value(value: str) -> str:
        """Hash a value using bcrypt."""
        salt = bcrypt.gensalt()
        hashed_value = bcrypt.hashpw(value.encode('utf-8'), salt)
        return hashed_value.decode('utf-8')

    @staticmethod
    def verify_hash(value: str, hashed_value: str) -> bool:
        """Verify a value against a hashed value."""
        return bcrypt.checkpw(value.encode('utf-8'), hashed_value.encode('utf-8'))