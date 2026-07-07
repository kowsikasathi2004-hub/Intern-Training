import { useState } from "react";
import axios from "axios";
import {
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";

const API = "http://127.0.0.1:8000/tasks";

export default function App() {
  const [title, setTitle] = useState("");

  const queryClient = useQueryClient();

  const { data, isLoading, error } = useQuery({
    queryKey: ["tasks"],
    queryFn: async () => {
      const res = await axios.get(API);
      return res.data;
    },
  });

  const mutation = useMutation({
    mutationFn: async (newTask) => {
      return axios.post(API, newTask);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["tasks"],
      });
      setTitle("");
    },
  });

  if (isLoading) return <h2>Loading...</h2>;

  if (error) return <h2>Error loading tasks.</h2>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Task Manager</h1>

      <input
        type="text"
        placeholder="Enter Task"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <button
        onClick={() => mutation.mutate({ title })}
      >
        Add Task
      </button>

      <hr />

      {data.map((task) => (
        <p key={task.id}>
          {task.id}. {task.title}
        </p>
      ))}
    </div>
  );
}