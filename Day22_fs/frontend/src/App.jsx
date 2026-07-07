import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [counter, setCounter] = useState("Waiting for server...");

  useEffect(() => {
    const socket = new WebSocket(import.meta.env.VITE_WS_URL);

    socket.onopen = () => {
      console.log("✅ Connected to WebSocket");
    };

    socket.onmessage = (event) => {
      setCounter(event.data);
    };

    socket.onerror = (error) => {
      console.error("WebSocket Error:", error);
    };

    socket.onclose = () => {
      console.log("❌ WebSocket Closed");
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div className="container">
      <h1>🚀 React + FastAPI</h1>
      <h2>Live Counter</h2>
      <h3>{counter}</h3>
    </div>
  );
}

export default App;