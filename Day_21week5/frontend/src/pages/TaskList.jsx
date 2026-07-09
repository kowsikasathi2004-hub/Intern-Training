import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import axios from "axios";
import { Link } from "@tanstack/react-router";

const API = "http://localhost:8000/tasks";

const fetchTasks = async () => {
  const res = await axios.get(API);
  return res.data;
};

const createTask = async (newTask) => {
  const res = await axios.post(API, newTask);
  return res.data;
};

export default function TaskList() {
  const queryClient = useQueryClient();

  const { data, isLoading, isError } = useQuery({
    queryKey: ["tasks"],
    queryFn: fetchTasks,
  });

  const mutation = useMutation({
    mutationFn: createTask,
    onSuccess: () => {
      queryClient.invalidateQueries(["tasks"]);
    },
  });

  if (isLoading) return <p>Loading tasks...</p>;
  if (isError) return <p>Error loading tasks!</p>;

  return (
    <div>
      <h1>Tasks</h1>
      <ul>
        {data.map((task) => (
          <li key={task.id}>
            <Link to={`/task/${task.id}`}>{task.title}</Link>
          </li>
        ))}
      </ul>

      <button
        onClick={() =>
          mutation.mutate({ id: data.length + 1, title: "New Task", description: "Demo task" })
        }
      >
        Add Task
      </button>
    </div>
  );
}
