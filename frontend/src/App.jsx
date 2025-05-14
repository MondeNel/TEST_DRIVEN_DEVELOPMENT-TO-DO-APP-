import React, { useState, useEffect } from 'react'
import todoService from '../services/todoService.js'
import TodoItem from './components/TodoItem'
import TodoForm from './components/TodoForm'

/**
 * Main App component that handles fetching, creating, updating, and deleting todos.
 *
 * @component
 * @returns {JSX.Element}
 */
const App = () => {
  const [todos, setTodos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // Fetch all todos on initial render
  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const data = await todoService.getTodos()
        setTodos(data)
      } catch (err) {
        setError('Failed to load todos.')
      } finally {
        setLoading(false)
      }
    }

    fetchTodos()
  }, [])

  /**
   * Add a new todo to the list.
   * @param {Object} todo - The new todo object to add.
   */
  const handleAddTodo = async (todo) => {
    const createdTodo = await todoService.createTodo(todo)
    if (createdTodo) {
      setTodos((prev) => [...prev, createdTodo])
    }
  }

  /**
   * Delete a todo by ID.
   * @param {string} id - The ID of the todo to delete.
   */
  const handleDeleteTodo = async (id) => {
    const deleted = await todoService.deleteTodo(id)
    if (deleted) {
      setTodos((prev) => prev.filter((todo) => todo.id !== id))
    }
  }

  /**
   * Update a todo item.
   * @param {string} id - The ID of the todo to update.
   * @param {string} title - Updated title.
   * @param {string} description - Updated description.
   * @param {boolean} completed - Updated completion status.
   */
  const handleUpdateTodo = async (id, title, description, completed) => {
    const updated = await todoService.updateTodo(id, { title, description, completed })
    if (updated) {
      setTodos((prev) =>
        prev.map((todo) => (todo.id === id ? updated : todo))
      )
    }
  }

  return (
    <div className="app-container p-4 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Todo App</h1>
      <TodoForm onAddTodo={handleAddTodo} />

      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p className="text-red-500">{error}</p>
      ) : todos.length === 0 ? (
        <p>No todos available.</p>
      ) : (
        todos.map((todo) => (
          <TodoItem
            key={todo.id}
            {...todo}
            onDelete={handleDeleteTodo}
            onUpdate={handleUpdateTodo}
          />
        ))
      )}
    </div>
  )
}

export default App
