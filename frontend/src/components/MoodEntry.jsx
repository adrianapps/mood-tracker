import api from "../api";

function MoodEntry({ userId, moodEntries, handleRemoveMood, handleSort }) {
  const handleDelete = async (moodId) => {
    if (userId && moodId)
      try {
        await api.delete(`/api/users/${userId}/moods/${moodId}/`);
        handleRemoveMood(moodId);
      } catch (error) {
        console.log(`Error occured while deleting mood entry: ${error}`);
      }
  };

  return (
    <div>
      <h1 className="text-center">User Mood Entries</h1>
      {moodEntries.length > 0 ? (
        <div className="overflow-x-auto">
          <table className="table table-zebra">
            {/* head */}
            <thead>
              <tr>
                <th
                  onClick={() => handleSort("mood")}
                  style={{ cursor: "pointer" }}
                >
                  Mood
                </th>
                <th
                  onClick={() => handleSort("date")}
                  style={{ cursor: "pointer" }}
                >
                  Date
                </th>
                <th>Description</th>
                <th>Actions</th> 
              </tr>
            </thead>
            <tbody>
              {moodEntries.map((mood) => (
                <tr key={mood.id}>
                  <td>{mood.mood_display}</td>
                  <td>{new Date(mood.date).toLocaleDateString()}</td>
                  <td>
                    {mood.description ? mood.description : "No description"}
                  </td>
                  <td>
                    <button
                      onClick={() => handleDelete(mood.id)}
                      className="btn btn-secondary"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <p>No mood entries found.</p>
      )}
    </div>
  );
}

export default MoodEntry;
