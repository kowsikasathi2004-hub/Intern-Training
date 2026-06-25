from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/data_db"
)
print("Database Connection Successful")

#CREATE UESER MODEL
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    posts = relationship("Post", back_populates="user")

# CREATE POST MODEL
class Post(Base):
    __tablename__="posts"
    post_id = Column(Integer, primary_key=True)
    title = Column(String(200),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User", back_populates= "posts")
Base.metadata.create_all(engine)

#CREATE SESSION
Session = sessionmaker(bind=engine)
session = Session()

#CREATE USER
existing_user = session.query(User).filter_by(
    email="divya@gmail.com"
).first()

if not existing_user:
    new_user = User(
        name="Divya",
        email="divya@gmail.com"
    )

    session.add(new_user)
    session.commit()

#CREATE POST
post1 = Post(
    title="SQL Basics",
    user_id=1
)

post2 = Post(
    title="Python Basics",
    user_id=1
)

session.add(post1)
session.add(post2)
session.commit()

# READ USER
users = session.query(User).all()

for user in users:
    print(user.id, user.name, user.email)

# READ POST
posts = session.query(Post).all()

for post in posts:
    print(post.post_id, post.title, post.user_id)

#FILTER QUERY
user = session.query(User).filter_by(name="Divya").first()
print(user.name)
#UPDATE USER
user = session.query(User).filter_by(id=1).first()
user.name = "Devika"
user.email = "devika12@gmail.com"
session.commit()
#DELETE
post = session.query(Post).filter_by(post_id=2).first()
session.delete(post)
session.commit()
#RELATIONSHIP QUERY
user = session.query(User).filter_by(id=1).first()
print(user.name)
for post in user.posts:
    print(post.title)