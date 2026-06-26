
from models import User, Post
from database import session
def relationship_check():
    user = session.query(User).filter_by(name="Kowsika").first()

    print("\nRELATIONSHIP: User → Posts")
    for post in user.posts:
        print("-", post.title)