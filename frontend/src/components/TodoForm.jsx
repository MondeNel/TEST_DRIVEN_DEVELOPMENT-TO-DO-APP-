import React, { useState } from 'react'
import '../styles/todoform.css'

const TodoForm = () => {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    const newTodo = {
      title,
      description,
      completed: false,
    }
    console.log('New Todo:', newTodo)
    // Clear form
    setTitle('')
    setDescription('')
  }

  return (
    <div className="todo-form-container">
      <h2>Create a Todo</h2>
      <form onSubmit={handleSubmit} className="todo-form">
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
        <button type="submit">Add Todo</button>
      </form>
    </div>
  )
}

export default TodoForm
