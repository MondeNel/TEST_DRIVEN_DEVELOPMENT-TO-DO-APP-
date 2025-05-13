import React, { useState } from 'react';
import UpdateModal from './UpdateModal';
import '../styles/todoitem.css';
import todoService from '../../services/todoService.js';

const TodoItem = ({ id, title, description, completed, onToggle, onDelete, onUpdate }) => {
  const [isEditing, setIsEditing] = useState(false);

  // Handle closing the modal on outside click or escape key
  const handleCloseModal = () => setIsEditing(false);

  const handleSave = async (updatedTitle, updatedDesc) => {
    const updatedData = {
      title: updatedTitle,
      description: updatedDesc,
      completed,
    };

    const updatedTodo = await todoService.updateTodo(id, updatedData);
    if (updatedTodo) {
      onUpdate(updatedTodo);
      handleCloseModal();
    }
  };

  const handleDelete = async () => {
    const deletedTodo = await todoService.deleteTodo(id);
    if (deletedTodo) {
      onDelete(id); // Remove the deleted todo from the parent component state
    }
  };

  return (
    <div className={`todo-item ${completed ? 'completed' : ''}`}>
      <div className="todo-text">
        <h3 className="todo-title">{title}</h3>
        <p className="todo-description">{description}</p>
      </div>
      <div className="todo-actions">
        <label>
          <input
            type="checkbox"
            checked={completed}
            onChange={() => onToggle(id)}
          />
          Completed
        </label>
        <button className="delete-button" onClick={handleDelete}>Delete</button>
        <button className="update-button" onClick={() => setIsEditing(true)}>Update</button>
      </div>

      {isEditing && (
        <UpdateModal
          title={title}
          description={description}
          onClose={handleCloseModal}
          onSave={handleSave}
        />
      )}
    </div>
  );
};

export default TodoItem;
