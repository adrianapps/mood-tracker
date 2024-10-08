import { useState } from "react";
import api from "../api";

function MoodEntryForm({ userId, handleAddMood }) {
  const [mood, setMood] = useState(0);
  const [description, setDescription] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (userId) {
      try {
        const response = await api.post(`/api/users/${userId}/moods/`, {
          user: userId,
          mood: mood,
          description: description,
        });
        console.log("Mood entry created:", response.data);
        handleAddMood(response.data);
        setMood(0);
        setDescription("");
      } catch (error) {
        console.error("Error creating mood entry:", error);
      }
    } else {
      console.warn("No userId available for creating mood entry");
    }
  };

  const openModal = () => {};

  const closeModal = () => {};

  return (
    <>
      {/* Open the modal using document.getElementById('my_modal_1').showModal() method */}
      <button
        className="btn btn-primary"
        onClick={() => document.getElementById("my_modal_1").showModal()}
      >
        Add Mood
      </button>

      <dialog
        id="my_modal_1"
        className="modal flex justify-center items-center"
      >
        <div className="modal-box">
          <form onSubmit={handleSubmit}>
            {/* Description text area */}
            <div className="flex flex-col space-y-4">
              <textarea
                className="textarea textarea-bordered"
                placeholder="Bio"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              ></textarea>
              {/* Heart rating */}
              <div className="rating gap-1 mx-auto">
                <input
                  type="radio"
                  name="rating-3"
                  value={-2}
                  checked={mood === -2}
                  onChange={() => setMood(-2)}
                  className="mask mask-heart bg-red-400"
                />
                <input
                  type="radio"
                  name="rating-3"
                  value={-1}
                  checked={mood === -1}
                  onChange={() => setMood(-1)}
                  className="mask mask-heart bg-orange-400"
                />
                <input
                  type="radio"
                  name="rating-3"
                  value={0}
                  checked={mood === 0}
                  onChange={() => setMood(0)}
                  className="mask mask-heart bg-yellow-400"
                />
                <input
                  type="radio"
                  name="rating-3"
                  value={1}
                  checked={mood === 1}
                  onChange={() => setMood(1)}
                  className="mask mask-heart bg-lime-400"
                />
                <input
                  type="radio"
                  name="rating-3"
                  value={2}
                  checked={mood === 2}
                  onChange={() => setMood(2)}
                  className="mask mask-heart bg-green-400"
                />
              </div>
            </div>
            <div className="modal-action">
              {/* if there is a button in form, it will close the modal */}
              <button type="submit" className="btn btn-primary">
                Save
              </button>
              {/* if there is a button in form, it will close the modal */}
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => document.getElementById("my_modal_1").close()}
              >
                Close
              </button>
            </div>
          </form>
        </div>
      </dialog>
    </>
  );
}

export default MoodEntryForm;
