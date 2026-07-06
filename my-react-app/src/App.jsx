import Counter from "./components/Counter";
import Card from "./components/Card";
import List from "./components/List";

export default function App() {
  const cardData = [
    { title: "React Basics", description: "Learn components and JSX" },
    { title: "Props", description: "Pass data between components" },
    { title: "State", description: "Manage dynamic data with useState" },
  ];

  const items = [1, 2, 3, 4, 5, 6, 7, 8];

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Day 19 - React Fundamentals</h1>

      <section>
        <h2>Counter</h2>
        <Counter />
      </section>

      <hr />

      <section>
        <h2>Cards (Props Example)</h2>
        {cardData.map((item, index) => (
          <Card
            key={index}
            title={item.title}
            description={item.description}
          />
        ))}
      </section>

      <hr />

      <section>
        <h2>List Rendering + Conditional Styling</h2>
        <List items={items} />
      </section>
    </div>
  );
}
