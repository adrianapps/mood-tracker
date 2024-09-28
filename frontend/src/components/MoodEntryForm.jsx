import React, { useState } from 'react';
import PropTypes from 'prop-types';
import api from '../api';


export default function MoodEntryForm({ userId }) {
  const [mood, setMood] = useState(2);
  const [description, setDescription] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (userId) {
      try {
        const response = await api.post(`/api/users/${userId}/moods/`, {
          mood: mood,
          description: description,
        });
        console.log('Mood entry created:', response.data);
        setMood(2);
        setDescription('');
      } catch (error) {
        console.error('Error creating mood entry:', error);
      }
    } else {
      console.warn('No userId available for creating mood entry');
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
      <h2>Create Mood Entry</h2>
      <StyledRating
        name="highlight-selected-only"
        value={mood}
        IconContainerComponent={IconContainer}
        getLabelText={(value) => customIcons[value].label}
        highlightSelectedOnly
        onChange={(event, newValue) => {
          setMood(newValue);
        }}
      />
      <TextField
        fullWidth
        label="Description"
        multiline
        rows={4}
        variant="outlined"
        value={description}
        onChange={(event) => setDescription(event.target.value)}
        sx={{ mt: 2 }}
      />
      <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
        Submit
      </Button>
    </Box>
  );
}
