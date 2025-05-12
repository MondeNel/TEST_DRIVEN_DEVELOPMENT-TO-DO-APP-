import React from 'react'
import '../styles/todoitem.css'

/**
 * Component to display a single Todo item.
 * 
 * @param {Object} props
 * @param {string} props.id - Todo item ID
 * @param {string} props.title - Title of the todo
 * @param {string} props.description - Description of the todo
 * @param {boolean} props.completed - Completion status
 * @param {Function} props.onToggle - Toggle completion handler
 * @param {Function} props.onDelete - Delete handler
 * @param {Function} props.onUpdate - Update handler
 */
const TodoItem = ({ id, title, description, completed, onToggle, onDelete, onUpdate }) => {
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
        <button className="update-btn" onClick={() => onUpdate(id)}>Update</button>
        <button className="delete-btn" onClick={() => onDelete(id)}>Delete</button>
      </div>
    </div>
  )
}

export default TodoItem
