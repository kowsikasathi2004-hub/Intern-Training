import { useState, useEffect } from "react";

function App() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [course, setCourse] = useState("");
  const [search, setSearch] = useState("");
  const [time, setTime] = useState("");

  useEffect(() => {
    console.log("Student Management System Loaded");

    setStudents([
      { id: 1, name: "Kowsika", course: "React" },
      { id: 2, name: "Rahul", course: "Python" },
    ]);

    const timer = setInterval(() => {
      setTime(new Date().toLocaleString());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const addStudent = (e) => {
    e.preventDefault();

    if (name.trim() === "" || course === "") {
      alert("Please fill all the fields");
      return;
    }

    const newStudent = {
      id: students.length + 1,
      name,
      course,
    };

    setStudents([...students, newStudent]);

    setName("");
    setCourse("");
  };

  const clearForm = () => {
    setName("");
    setCourse("");
  };

  const filteredStudents = students.filter((student) =>
    student.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-gradient-to-r from-indigo-700 via-purple-600 to-pink-500 flex justify-center items-center p-6">

      <div className="bg-white/90 backdrop-blur-md w-[800px] rounded-2xl shadow-2xl p-8 border border-white">

        <h1 className="text-4xl font-bold text-center text-indigo-700">
          🎓 Student Management System
        </h1>

        <p className="text-center text-gray-600 mt-2">
          {time}
        </p>

        <p className="text-center text-green-600 font-semibold mt-2">
          Total Students : {students.length}
        </p>

        {/* Search */}

        <input
          type="text"
          placeholder="🔍 Search Student..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full mt-6 border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        />

        {/* Form */}

        <form onSubmit={addStudent} className="space-y-4 mt-6">

          <input
            type="text"
            placeholder="Enter Student Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />

          <select
            value={course}
            onChange={(e) => setCourse(e.target.value)}
            className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
            <option value="">Select Course</option>
            <option>React</option>
            <option>Python</option>
            <option>Java</option>
            <option>JavaScript</option>
            <option>TypeScript</option>
            <option>SQL</option>
          </select>

          <div className="flex gap-4">

            <button
              type="submit"
              className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg"
            >
              Add Student
            </button>

            <button
              type="button"
              onClick={clearForm}
              className="bg-gray-500 hover:bg-gray-600 text-white px-6 py-3 rounded-lg"
            >
              Clear
            </button>

          </div>

        </form>

        {/* Student Table */}

        <table className="w-full mt-8 border border-gray-300">

          <thead className="bg-indigo-600 text-white">

            <tr>
              <th className="p-3">ID</th>
              <th>Name</th>
              <th>Course</th>
            </tr>

          </thead>

          <tbody>

            {filteredStudents.length > 0 ? (
              filteredStudents.map((student) => (
                <tr
                  key={student.id}
                  className="text-center border hover:bg-indigo-50"
                >
                  <td className="p-3">{student.id}</td>
                  <td>{student.name}</td>
                  <td>{student.course}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3" className="text-center text-red-500 p-5">
                  No Student Found
                </td>
              </tr>
            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default App;