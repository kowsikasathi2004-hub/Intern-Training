import axios from "axios";

const API = "http://127.0.0.1:8000";

export const getTasks = async () => {
  const res = await axios.get(`${API}/tasks`);
  return res.data;
};

export const getTask = async (id) => {
  const res = await axios.get(`${API}/tasks/${id}`);
  return res.data;
};

export const addTask = async (task) => {
  const res = await axios.post(`${API}/tasks`, task);
  return res.data;
};