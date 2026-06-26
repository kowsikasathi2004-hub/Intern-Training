from database import session
from models import User, Post

def insert_data():
    # Create users
    user1 = User(
        name="Kowsika",
        email="kowsika@gmail.com"
    )

    user2 = User(
        name="Priya",
        email="priya@gmail.com"
    )

    # Create posts
    post1 = Post(
        title="SQLAlchemy Intro",
        content="Learning ORM basics",
        user=user1
    )

    post2 = Post(
        title="Relationships",
        content="One-to-Many relationship",
        user=user1
    )

    post3 = Post(
        title="PostgreSQL Guide",
        content="Database concepts",
        user=user2
    )

    # Add records
    session.add_all([
        user1,
        user2,
        post1,
        post2,
        post3
    ])

    # Save to database
    session.commit()

    print("Data inserted successfully!")

insert_data()