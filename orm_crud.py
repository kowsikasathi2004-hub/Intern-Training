from database import engine, SessionLocal
from models import Base, User, Post

# Create tables
Base.metadata.create_all(bind=engine)

session = SessionLocal()

# -------------------
# CREATE
# -------------------

user1 = User(
    name="Balachandar",
    email="balachandar@gmail.com"
)

session.add(user1)
session.commit()

post1 = Post(
    title="My First Post",
    content="Learning SQLAlchemy ORM",
    user_id=user1.id
)

session.add(post1)
session.commit()

print("Data inserted successfully!")

# -------------------
# READ
# -------------------

users = session.query(User).all()

print("\nAll Users:")
for user in users:
    print(user)

# Filter User

user = session.query(User).filter(
    User.name == "Balachandar"
).first()

print("\nFiltered User:")
print(user)

# -------------------
# UPDATE
# -------------------

user.name = "Bala"

session.commit()

print("\nUser Updated Successfully!")

# -------------------
# RELATIONSHIP QUERY
# -------------------

user = session.query(User).first()

print("\nPosts of User:")

for post in user.posts:
    print(post.title)

# -------------------
# DELETE
# -------------------

post_to_delete = session.query(Post).first()

session.delete(post_to_delete)

session.commit()

print("\nPost Deleted Successfully!")

session.close()