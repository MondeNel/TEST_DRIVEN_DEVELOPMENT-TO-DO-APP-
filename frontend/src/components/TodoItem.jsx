import React, { useState } from 'react'
import UpdateModal from './UpdateModal'
import '../styles/todoitem.css'

const TodoItem = ({ id, title, description, completed, onToggle, onDelete, onUpdate }) => {
  const [isEditing, setIsEditing] = useState(false)

  // Handle closing the modal on outside click or escape key
  const handleCloseModal = () => setIsEditing(false)

  const handleSave = (updatedTitle, updatedDesc) => {
    onUpdate(id, updatedTitle, updatedDesc)
    handleCloseModal()
  }

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
        <button onClick={() => onDelete(id)}>Delete</button>
        <button onClick={() => setIsEditing(true)}>Update</button>
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
  )
}

export default TodoItem
