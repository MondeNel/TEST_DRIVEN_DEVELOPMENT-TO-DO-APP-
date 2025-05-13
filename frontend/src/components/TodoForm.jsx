import React, { useState } from 'react';
import '../styles/todoform.css';
import todoService from '../services/todoService';

/**
 * Form component for creating a new todo item.
 *
 * @component
 * @param {Function} onAddTodo - Function to handle adding a new todo.
 * @returns {JSX.Element}
 */
const TodoForm = ({ onAddTodo }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false); // Loading state
  const [error, setError] = useState(''); // Error state

  // Submit handler for the form
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Early return if form is invalid
    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    setLoading(true); // Start loading
    setError(''); // Reset previous error

    // Create a new todo object
    const newTodo = {
      title,
      description,
      completed: false,
    };

    try {
      // Call the API to create the todo on the backend
      const createdTodo = await todoService.createTodo(newTodo);

      // If the todo is successfully created, update the parent component
      if (createdTodo) {
        onAddTodo(createdTodo);
        setTitle(''); // Clear the title input
        setDescription(''); // Clear the description input
      } else {
        setError('Failed to create todo. Please try again.');
      }
    } catch (error) {
      console.error('Error creating todo:', error);
      setError('Error creating todo. Please try again.');
    } finally {
      setLoading(false); // End loading
    }
  };

  return (
    <div className="todo-form-container">
      <h2>Create a Todo</h2>
      <form onSubmit={handleSubmit} className="todo-form">
        {error && <p className="error-message">{error}</p>} {/* Display error message */}
        
        <div className="form-group">
          <label htmlFor="title">Title</label>
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter title"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Description</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Enter description"
          />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Adding Todo...' : 'Add Todo'}
        </button>
      </form>
    </div>
  );
};

export default TodoForm;
