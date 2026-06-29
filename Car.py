class Car:
    def __init__(self, brand, car_name, year):
        self.brand = brand
        self.car_name = car_name
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Car Name:", self.car_name)<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Profile</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>

    <header>
        <h1>My Personal Profile</h1>
        <p>Welcome to my profile page</p>
    </header>

    <main>

        <section class="profile">

            <div class="profile-image">
                <img src="profile.jpg" alt="Profile Image">
            </div>

            <div class="profile-content">
                <h2>About Me</h2>

                <p>
                    Hello! My name is Kowsika.
                    I am learning HTML, CSS, Python,
                    SQL and FastAPI. I enjoy building
                    web applications and continuously
                    improving my programming skills.
                </p>

                <h3>Skills</h3>

                <ul>
                    <li>HTML</li>
                    <li>CSS</li>
                    <li>Python</li>
                    <li>SQL</li>
                    <li>FastAPI</li>
                </ul>

            </div>

        </section>

        <section class="contact">

            <h2>Contact Me</h2>

            <form>

                <label for="name">Name</label>

                <input
                    type="text"
                    id="name"
                    placeholder="Enter your name"
                    required
                >

                <label for="email">Email</label>

                <input
                    type="email"
                    id="email"
                    placeholder="Enter your email"
                    required
                >

                <label for="message">Message</label>

                <textarea
                    id="message"
                    rows="5"
                    placeholder="Write your message"
                    required
                ></textarea>

                <button type="submit">
                    Send Message
                </button>

            </form>

        </section>

    </main>

    <footer>
        <p>© 2026 Kowsika | All Rights Reserved</p>
    </footer>

</body>
</html>
        print("Year:", self.year)
brand = input("Enter the brand of the car: ")
car_name = input("Enter the name of the car: ")
year = int(input("Enter the year of the car: "))
car1 = Car(brand, car_name, year)
car1.display()