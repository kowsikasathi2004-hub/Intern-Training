import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/users")
      .then((res) => setUsers(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <h1>Docker Full Stack App</h1>

      {users.map((user) => (
        <div key={user.id}>
          <h3>{user.name}</h3>
        </div>
      ))}
    </>
  );
}

export default App;