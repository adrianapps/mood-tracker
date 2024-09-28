import { useState, useEffect } from "react"
import api, { getUserIdFromToken } from "../api"
import MoodEntry from "../components/MoodEntry"
import MoodEntryForm from "../components/MoodEntryForm";
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
        // return <MoodEntryForm userId={userId} />
    )
}


export default Home