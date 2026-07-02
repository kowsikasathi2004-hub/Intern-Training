export default function List({ items }) {
  return (
    <ul>
      {items.map((item) => (
        <li
          key={item}
          style={{
            padding: "5px",
            margin: "5px 0",
            backgroundColor: item % 2 === 0 ? "#d1ffd6" : "#ffd6d6",
          }}
        >
          Item {item} {item % 2 === 0 ? "(Even - Highlighted)" : "(Odd)"}
        </li>
      ))}
    </ul>
  );
}