import { useState, useEffect } from "react";
import api from "../api";
import MoodEntryForm from "./MoodEntryForm";

function Navbar({ userId, handleAddMood }) {
  const [username, setUsername] = useState("");
  useEffect(() => {
    console.log("userId:", userId);

    if (userId) {
      api
        .get(`/api/users/${userId}/`)
        .then((res) => {
          console.log("API Response:", res.data);
          setUsername(res.data.username);
        })
        .catch((err) => {
          console.error("API Error:", err);
        });
    } else {
      console.warn("No userId available");
    }
  }, [userId]);

  return (
    <div className="navbar bg-base-100">
      <div className="flex-1">
        <a className="btn btn-ghost text-xl">Mood Tracker</a>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          <li>
            <MoodEntryForm userId={userId} handleAddMood={handleAddMood}/>
          </li>
          <li>
            <a>{username}</a>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default Navbar;
