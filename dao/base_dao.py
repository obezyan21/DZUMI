from sqlalchemy.orm import Session 


class BaseDAO:
    def __init__(self, session: Session, model):
        self.session = session
        self.model = model

    def create(self, *, instance=None, **kwargs):
        if instance is not None:
            obj = instance
        else:
            obj = self.model(**kwargs)

        self.session.add(obj)
        self.session.commit()
        
        return obj
    
    def get_all(self):



