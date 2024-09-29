import React, { useState } from 'react';
import api from '../api';


function MoodEntryForm({ userId }) {
  const [mood, setMood] = useState(0);
  const [description, setDescription] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (userId) {
      try {
        const response = await api.post(`/api/users/${userId}/moods/`, { user: userId, mood: mood, description: description });
        console.log('Mood entry created:', response.data);
        setMood(0);
        setDescription('');
      } catch (error) {
        console.error('Error creating mood entry:', error);
      }
    } else {
      console.warn('No userId available for creating mood entry');
    }
  };

  const openModal = () => {
    document.getElementById('my_modal_1').showModal();
  };

  const closeModal = () => {
    document.getElementById('my_modal_1').close();
  };

  return (
    <>
      {/* Open the modal using document.getElementById('my_modal_1').showModal() method */}
      <button className="btn" onClick={openModal}>
        Open Modal
      </button>

      <dialog id="my_modal_1" className="modal">
        <div className="modal-box">

          <form onSubmit={handleSubmit}>
            {/* Description text area */}
            <textarea
              className="textarea textarea-bordered"
              placeholder="Bio"
              value={description}
              onChange={(e) => setDescription(e.target.value)}></textarea>
            {/* Heart rating */}
            <div className="rating gap-1">
              <input type="radio" name="rating-3" value={-2} checked={mood === -2} onChange={() => setMood(-2)} className="mask mask-heart bg-red-400" />
              <input type="radio" name="rating-3" value={-1} checked={mood === -1} onChange={() => setMood(-1)} className="mask mask-heart bg-orange-400" />
              <input type="radio" name="rating-3" value={0} checked={mood === 0} onChange={() => setMood(0)} className="mask mask-heart bg-yellow-400" />
              <input type="radio" name="rating-3" value={1} checked={mood === 1} onChange={() => setMood(1)} className="mask mask-heart bg-lime-400" />
              <input type="radio" name="rating-3" value={2} checked={mood === 2} onChange={() => setMood(2)} className="mask mask-heart bg-green-400" />
            </div>
            <div className="modal-action">
              {/* if there is a button in form, it will close the modal */}
              <button type="submit" className="btn btn-primary">Save</button>
              {/* if there is a button in form, it will close the modal */}
              <button className="btn btn-secondary" onClick={closeModal}>Close</button>
            </div>
          </form>
        </div>
      </dialog>
    </>
  );

}

export default MoodEntryForm;