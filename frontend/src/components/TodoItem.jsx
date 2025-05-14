import React, { useState } from 'react'
import UpdateModal from './UpdateModal'
import '../styles/todoitem.css'
import todoService from '../../services/todoService.js'

/**
 * A single Todo item.
 *
 * @component
 * @param {object} props
 * @param {string} props.id - Todo ID
 * @param {string} props.title - Todo title
 * @param {string} props.description - Todo description
 * @param {boolean} props.completed - Completion status
 * @param {function} props.onUpdate - Callback when a todo is updated
 * @param {function} props.onDelete - Callback when a todo is deleted
 */
const TodoItem = ({ id, title, description, completed, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false)

  const handleToggleCompleted = async () => {
    const updatedTodo = await todoService.updateTodo(id, {
      title,
      description,
      completed: !completed,
    })
    if (updatedTodo) {
      onUpdate(updatedTodo)
    }
  }

  const handleSave = async (updatedTitle, updatedDesc) => {
    const updatedTodo = await todoService.updateTodo(id, {
      title: updatedTitle,
      description: updatedDesc,
      completed,
    })
    if (updatedTodo) {
      onUpdate(updatedTodo)
      setIsEditing(false)
    }
  }

  const handleDelete = async () => {
    const deleted = await todoService.deleteTodo(id)
    if (deleted) {
      onDelete(id)
    }
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
            onChange={handleToggleCompleted}
          />
          Completed
        </label>
        <button className="update-button" onClick={() => setIsEditing(true)}>Update</button>
        <button className="delete-button" onClick={handleDelete}>Delete</button>
      </div>

      {isEditing && (
        <UpdateModal
          title={title}
          description={description}
          onClose={() => setIsEditing(false)}
          onSave={handleSave}
        />
      )}
    </div>
  )
}

export default TodoItem
