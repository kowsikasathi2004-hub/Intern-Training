import { useState } from "react";
import "./App.css";

interface Employee {
  id: number;
  name: string;
  department: string;
  present: boolean;
}

function getAttendanceStatus(employee: Employee): string {
  return employee.present ? "Present" : "Absent";
}

function App() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [department, setDepartment] = useState("");
  const [present, setPresent] = useState(true);

  const addEmployee = () => {
    if (!id || !name || !department) {
      alert("Please fill all fields");
      return;
    }

    const newEmployee: Employee = {
      id: Number(id),
      name,
      department,
      present,
    };

    setEmployees([...employees, newEmployee]);

    // Clear the form
    setId("");
    setName("");
    setDepartment("");
    setPresent(true);
  };

  return (
    <div className="container">
      <h1>Employee Attendance System</h1>

      <input
        type="number"
        placeholder="Employee ID"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />

      <input
        type="text"
        placeholder="Employee Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      {/* Department Dropdown */}
      <select
        value={department}
        onChange={(e) => setDepartment(e.target.value)}
      >
        <option value="">Select Department</option>
        <option value="HR">HR</option>
        <option value="Manager">Manager</option>
        <option value="Asst. Manager">Asst. Manager</option>
        <option value="Senior Manager">Senior Manager</option>
      </select>

      <label style={{ marginLeft: "15px" }}>
        <input
          type="checkbox"
          checked={present}
          onChange={(e) => setPresent(e.target.checked)}
        />
        Present
      </label>

      <br />
      <br />

      <button onClick={addEmployee}>Add Employee</button>

      <hr />

      {employees.map((employee) => (
        <div className="card" key={employee.id}>
          <h2>{employee.name}</h2>

          <p>
            <strong>Employee ID:</strong> {employee.id}
          </p>

          <p>
            <strong>Department:</strong> {employee.department}
          </p>

          <p>
            <strong>Status:</strong>{" "}
            <span
              style={{
                color: employee.present ? "green" : "red",
                fontWeight: "bold",
              }}
            >
              {getAttendanceStatus(employee)}
            </span>
          </p>
        </div>
      ))}
    </div>
  );
}

export default App;