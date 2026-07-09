export default function Card({ title, description }) {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "10px",
        marginBottom: "10px",
        borderRadius: "8px",
      }}
    >
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}