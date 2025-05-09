import React, { useState } from 'react'
import './todoform.css'

/**
 * A form component to add new todos.
 * 
 * @component
 * @returns {JSX.Element} TodoForm
 */
const TodoForm = () => {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  /**
   * Handles form submission for creating a new todo.
   * @param {React.FormEvent} e 
   */
  const handleSubmit = (e) => {
    e.preventDefault()

    if (!title.trim()) return

    const newTodo = {
      title,
      description,
      completed: false
    }

    // TODO: Send newTodo to the backend API
    console.log('Creating todo:', newTodo)

    // Clear form
    setTitle('')
    setDescription('')
  }

  return (
    <form onSubmit={handleSubmit} className="todo-form">
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter title"
          required
        />
      </div>

      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Enter description"
        />
      </div>

      <button type="submit">Add Todo</button>
    </form>
  )
}

export default TodoForm
