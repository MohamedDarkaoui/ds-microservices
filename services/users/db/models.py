# from sqlalchemy import create_engine, Column, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'user'
#     username = Column('username', String, primary_key=True)
#     password = Column('password', String)

# engine = create_engine('sqlite:///:users.db', echo=True)
# Base.metadata.create_all(bind=engine)


