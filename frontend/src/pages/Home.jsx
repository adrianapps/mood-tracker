import { useState, useEffect } from "react";
import api, { getUserIdFromToken } from "../api";
import MoodEntry from "../components/MoodEntry";
import Navbar from "../components/Navbar";

function Home() {
  const userId = getUserIdFromToken();
  const [moodEntries, setMoodEntries] = useState([]);

  useEffect(() => {
    if (userId) {
      api
        .get(`/api/users/${userId}/moods/`)
        .then((res) => {
          setMoodEntries(res.data);
        })
        .catch((err) => {
          console.error("API Error:", err);
        });
    }
  }, [userId]);

  const handleAddMood = (newMood) => {
    setMoodEntries((prevEntries) => [...prevEntries, newMood]);
  };

  const handleRemoveMood = (moodId) => {
    setMoodEntries((prevEntries) =>
      prevEntries.filter((mood) => mood.id !== moodId)
    );
  };

  return (
    <div>
      <Navbar userId={userId} handleAddMood={handleAddMood} />
      <div className="flex flex-col items-center justify-center min-h-screen">
        <MoodEntry
          userId={userId}
          moodEntries={moodEntries}
          handleRemoveMood={handleRemoveMood}
        />
      </div>
    </div>
  );
}

export default Home;
