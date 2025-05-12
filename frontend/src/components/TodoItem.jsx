import React from 'react'
import '../styles/todoitem.css'

/**
 * Component to display a single Todo item.
 */
const TodoItem = ({ id, title, description, completed, onToggle, onDelete }) => {
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
        <button className="delete-btn" onClick={() => onDelete(id)}>Delete</button>
      </div>
    </div>
  )
}

export default TodoItem
