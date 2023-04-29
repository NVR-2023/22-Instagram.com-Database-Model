import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class NewUser(Base):
    __tablename__ = "new_user"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    posts = relationship("Post")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("new_user.id"))
    likes_count = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    is_published = Column(Boolean, default=False)
    media = relationship("Media")
    comments = relationship("Comment")



class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(Enum('photo', 'video', 'reel', 'igtv'), nullable=False)   
    url = Column(String(2048), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(2200))
    author_id = Column(Integer, ForeignKey("new_user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("new_user.id"))
    user_to_id = Column(Integer, ForeignKey("new_user.id"))
    user_from = relationship("NewUser")
    user_to = relationship("NewUser")

    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
