import models


class BaseService:
    def __init__(self, db: models.Db):
        self.db = db

    def get_all(self):
        pass

    def add(self, entity):
        self.db.add(entity)
        self.commit()

    def commit(self):
        self.db.commit()

    def delete(self, _id: int):
        pass
