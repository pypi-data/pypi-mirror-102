from sqlalchemy import create_engine, Table, Column, Integer, String, Text, MetaData, DateTime
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator
from datetime import datetime


class ClientDB:
    """
    База данных клиента.
    """
    class KnownUsers:
        def __init__(self, user):
            self.id = None
            self.username = user

    class MessageHistory:
        def __init__(self, from_user, to_user, message):
            self.id = None
            self.from_user = from_user
            self.to_user = to_user
            self.message = message
            self.date = datetime.now()

    class Contacts:
        def __init__(self, contact):
            self.id = None
            self.name = contact

    def __init__(self, name):
        self.database_engine = create_engine(f'sqlite:///client/cln_{name}.db3', echo=False, pool_recycle=7200,
                                             connect_args={'check_same_thread': False})
        self.metadata = MetaData()

        users = Table('known_users', self.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('username', String)
                      )

        history = Table('message_history', self.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('from_user', String),
                        Column('to_user', String),
                        Column('message', Text),
                        Column('date', DateTime)
                        )

        contacts = Table('contacts', self.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('name', String, unique=True)
                         )

        self.metadata.create_all(self.database_engine)

        mapper(self.KnownUsers, users)
        mapper(self.MessageHistory, history)
        mapper(self.Contacts, contacts)

        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        # --------очистка списка активных контактов-------------------
        self.session.query(self.Contacts).delete()
        self.session.commit()

    def upd_contact(self, contact, action):
        query = self.session.query(self.Contacts).filter_by(name=contact)
        if action == 'add':
            if not query.first():
                self.session.add(self.Contacts(contact))
        elif action == 'del':
            query.delete()
        self.session.commit()

    def add_users(self, users_list):
        self.session.query(self.KnownUsers).delete()
        for user in users_list:
            user_row = self.KnownUsers(user)
            self.session.add(user_row)
        self.session.commit()

    def save_message(self, from_user, to_user, message):
        message_row = self.MessageHistory(from_user, to_user, message)
        self.session.add(message_row)
        self.session.commit()

    def get_contacts(self):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        #print('cont')
        #return session1.query(self.Contacts.name).all()
        return [contact[0] for contact in session1.query(self.Contacts.name).all()]

    def get_users(self):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        return [contact[0] for contact in session1.query(self.KnownUsers.username).all()]


    '''
    def check_user(self, user):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        if session1.query(self.KnownUsers).filter_by(username=user).count():
            return True
        else:
            return False

    def check_contact(self, contact):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        if session1.query(self.Contacts).filter_by(name=contact).count():
            return True
        else:
            return False
    '''

    def get_hist(self, user_from=None, user_to=None):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        query = session1.query(self.MessageHistory)
        if user_from:
            query = query.filter_by(from_user=user_from)
        if user_to:
            query = query.filter_by(to_user=user_to)
        return [(history_row.from_user, history_row.to_user, history_row.message, history_row.date)
                for history_row in query.all()]


if __name__ == '__main__':
    test_db = ClientDB('user1')
    #for i in ['user2', 'user3', 'user4']:
    #    test_db.upd_contact(i, action='add')
    #test_db.upd_contact('user4', action='add')
    #test_db.add_users(['user1', 'user2', 'user3', 'user4'])
    #test_db.save_message('user1', 'user2', f'test message1 {datetime.now()}!')
    #test_db.save_message('user2', 'user1', f'test message2 {datetime.now()}!')
    #print(test_db.get_contacts())
    #print(test_db.get_users())
    #print(test_db.check_user('user1'))
    #print(test_db.check_user('user66'))
    print(test_db.get_hist(user_to='user33'))
    #print(test_db.get_hist(to_who='user2'))
    #print(test_db.get_hist('user3'))
    #test_db.upd_contact('user4', action='del')
    #print(test_db.get_contacts())
