import { useState } from "react";
import "./App.css";

function App() {

  const [message, setMessage] = useState("");

  const getMessage = () => {
    setMessage("Frontend CI/CD Application is Working!");
  };

  return (
    <div className="container">

      <h1>
        Final Assessment Project
      </h1>

      <p>
        React Frontend with GitHub Actions CI
      </p>

      <button onClick={getMessage}>
        Check Status
      </button>

      <h3>{message}</h3>

    </div>
  );
}

export default App;