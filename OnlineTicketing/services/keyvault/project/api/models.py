from sqlalchemy.sql import func

from project import db


class Keyvault(db.Model):
    __tablename__ = 'keyvault'
    encrypted = db.Column(db.String(128), nullable=False)
    decrypted = db.Column(db.String(128), nullable=False)

    def __init__(self, encrypted, decrypted):
        self.encrypted = encrypted
        self.decrypted = decrypted

    def to_json(self):
        return {
            'encrypted': self.encrypted,
            'decrypted': self.decrypted
        }
