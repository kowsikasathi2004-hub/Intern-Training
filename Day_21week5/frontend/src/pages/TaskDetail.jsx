import { useParams } from "@tanstack/react-router";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const API = "http://localhost:8000/tasks";

const fetchTask = async (id) => {
  const res = await axios.get(`${API}/${id}`);
  return res.data;
};

export default function TaskDetail() {
  const { id } = useParams();

  const { data, isLoading, isError } = useQuery({
    queryKey: ["task", id],
    queryFn: () => fetchTask(id),
  });

  if (isLoading) return <p>Loading task...</p>;
  if (isError) return <p>Error loading task!</p>;

  return (
    <div>
      <h2>{data.title}</h2>
      <p>{data.description}</p>
    </div>
  );
}
