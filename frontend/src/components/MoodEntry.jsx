import api from "../api";

function MoodEntry({ userId, moodEntries, handleRemoveMood }) {

  const handleDelete = async (moodId) => {
    if (userId && moodId)
      try {
        await api.delete(`/api/users/${userId}/moods/${moodId}/`);
        handleRemoveMood(moodId)
      } catch (error) {
        console.log(`Error occured while deleting mood entry: ${error}`);
      }
  };

  return (
    <div>
      <h1 className="text-center">User Mood Entries</h1>
      <ul>
        {moodEntries.length > 0 ? (
          moodEntries.map((mood, index) => (
            <li key={index}>
              <div className="overflow-x-auto">
                <table className="table table-zebra">
                  {/* head */}
                  <thead>
                    <tr>
                      <th>Mood</th>
                      <th>Date</th>
                      <th>Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    {/* row 1 */}
                    <tr>
                      <th>{mood.mood_display}</th>
                      <th>{new Date(mood.date).toLocaleDateString()}</th>
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
                  </tbody>
                </table>
              </div>
            </li>
          ))
        ) : (
          <p>No mood entries found.</p>
        )}
      </ul>
    </div>
  );
}

export default MoodEntry;
