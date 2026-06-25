from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/data_db"
)

Base = declarative_base()

print("Database Connection Successful")


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    posts = relationship("Post", back_populates="user", cascade="all, delete")

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)

    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("User", back_populates="posts")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

users_data = [
    ("John", "john@gmail.com"),
    ("Alice", "alice@gmail.com"),
    ("Bob", "bob@gmail.com"),
    ("David", "david@gmail.com")
]

for name, email in users_data:
    existing = session.query(User).filter_by(email=email).first()
    if not existing:
        user = User(name=name, email=email)
        session.add(user)

session.commit()

john = session.query(User).filter_by(email="john@gmail.com").first()
alice = session.query(User).filter_by(email="alice@gmail.com").first()
bob = session.query(User).filter_by(email="bob@gmail.com").first()

# =========================
# CREATE POSTS (SAFE RELATIONSHIP WAY)
# =========================
if john:
    session.add_all([
        Post(title="SQL Basics", user=john),
        Post(title="Database Design", user=john)
    ])

if alice:
    session.add_all([
        Post(title="Python Guide", user=alice),
        Post(title="FastAPI Tutorial", user=alice)
    ])

if bob:
    session.add(
        Post(title="PostgreSQL Joins", user=bob)
    )

session.commit()

print("\nUSERS:")
for u in session.query(User).all():
    print(u.user_id, u.name, u.email)

print("\nPOSTS:")
for p in session.query(Post).all():
    print(p.post_id, p.title, p.user_id)

print("\nRELATIONSHIP OUTPUT:")
user = session.query(User).filter_by(name="John").first()

if user:
    print("User:", user.name)
    for post in user.posts:
        print("-", post.title)