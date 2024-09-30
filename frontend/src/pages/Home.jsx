import { useState, useEffect } from "react";
import api, { getUserIdFromToken } from "../api";
import MoodEntry from "../components/MoodEntry";
import Navbar from "../components/Navbar";

function Home() {
  const userId = getUserIdFromToken();

  return (
    <div>
      <Navbar userId={userId} />
      <div className="flex flex-col items-center justify-center min-h-screen">
        <MoodEntry userId={userId} />
      </div>
    </div>
  );
}

export default Home;
