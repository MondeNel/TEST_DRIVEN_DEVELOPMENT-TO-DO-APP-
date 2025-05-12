import React from 'react'
import '../styles/todoitem.css'

/**
 * Component to display a single Todo item.
 * @param {Object} props 
 * @param {string} props.id - The ID of the todo item.
 * @param {string} props.title - Title of the todo.
 * @param {string} props.description - Description of the todo.
 * @param {boolean} props.completed - Completion status.
 * @param {Function} props.onToggle - Handler to toggle completion.
 * @param {Function} props.onDelete - Handler to delete the todo.
 */
const TodoItem = ({ id, title, description, completed, onToggle, onDelete }) => {
  return (
    <div className={`todo-item ${completed ? 'completed' : ''}`}>
      <div className="todo-text">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
      <div className="todo-actions">
        <input
          type="checkbox"
          checked={completed}
          onChange={() => onToggle(id)}
        />
        <button onClick={() => onDelete(id)}>Delete</button>
      </div>
    </div>
  )
}

export default TodoItem
