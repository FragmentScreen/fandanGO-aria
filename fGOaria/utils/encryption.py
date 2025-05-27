from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import json
import logging
from pathlib import Path
import platform

class TokenEncryption:
    def __init__(self):
        self.token_file = Path.home() / '.aria_token'
        self.salt_file = Path.home() / '.aria_salt'
        self._ensure_salt_exists()
        logging.info(f"TokenEncryption initialized on {platform.system()}")
        
    def _ensure_salt_exists(self):
        """Ensure the salt file exists and contains a valid salt."""
        try:
            if not self.salt_file.exists():
                salt = os.urandom(16)
                self.salt_file.write_bytes(salt)
                logging.info(f"Created new salt file at {self.salt_file}")
            else:
                salt = self.salt_file.read_bytes()
                if len(salt) != 16:
                    salt = os.urandom(16)
                    self.salt_file.write_bytes(salt)
                    logging.info("Regenerated invalid salt file")
        except Exception as e:
            logging.error(f"Error managing salt file: {str(e)}")
            raise Exception(f"Failed to manage salt file: {str(e)}")
    
    def _get_key(self, password: str) -> bytes:
        """Derive an encryption key from the password using PBKDF2."""
        try:
            salt = self.salt_file.read_bytes()
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
            return key
        except Exception as e:
            logging.error(f"Error deriving encryption key: {str(e)}")
            raise Exception(f"Failed to derive encryption key: {str(e)}")
    
    def encrypt_token(self, token_data: dict, password: str) -> None:
        """Encrypt and store token data."""
        try:
            key = self._get_key(password)
            f = Fernet(key)
            encrypted_data = f.encrypt(json.dumps(token_data).encode())
            self.token_file.write_bytes(encrypted_data)
            logging.info(f"Successfully encrypted and stored token at {self.token_file}")
        except Exception as e:
            logging.error(f"Error encrypting token: {str(e)}")
            raise Exception(f"Failed to encrypt token: {str(e)}")
    
    def decrypt_token(self, password: str) -> dict:
        """Decrypt and retrieve token data."""
        if not self.token_file.exists():
            logging.info("No token file found")
            return None
            
        try:
            key = self._get_key(password)
            f = Fernet(key)
            encrypted_data = self.token_file.read_bytes()
            decrypted_data = f.decrypt(encrypted_data)
            logging.info("Successfully decrypted token")
            return json.loads(decrypted_data)
        except Exception as e:
            logging.error(f"Error decrypting token: {str(e)}")
            return None
    
    def clear_token(self) -> None:
        """Remove stored token data."""
        try:
            if self.token_file.exists():
                self.token_file.unlink()
                logging.info("Successfully cleared token file")
        except Exception as e:
            logging.error(f"Error clearing token file: {str(e)}")
            raise Exception(f"Failed to clear token file: {str(e)}") 