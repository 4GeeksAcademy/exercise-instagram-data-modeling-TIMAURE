import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firtsname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email= Column(String(250), nullable=False, unique=True)


class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, nullable=False)
    user_from_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    Follower = relationship(User)


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post= relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100), nullable=False)
    author_id = Column(Integer, nullable=False)
    post_id = Column(Integer, nullable=False)
    User_id = Column(Integer, ForeignKey('user.id'))
    User = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post= relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False)
    url = Column(String(1000), nullable=False)
    post_id = Column(Integer, nullable=False)
    Media_id = Column(Integer, ForeignKey('post.id'))
    post= relationship(Post)
 
#class Address(Base):
    # __tablename__ = 'address'
    # # Here we define columns for the table address.
    # # Notice that each column is also a normal Python instance attribute.
    # id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

#     def to_dict(self):
#         return {}

#  Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
