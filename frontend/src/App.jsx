import React, { useState, useEffect } from 'react'
import todoService from '../services/todoService.js'
import TodoForm from './components/TodoForm'
import TodoList from './components/TodoList'

const App = () => {
  const [todos, setTodos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

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

  const handleAddTodo = async (todo) => {
    const createdTodo = await todoService.createTodo(todo)
    if (createdTodo) {
      setTodos((prev) => [...prev, createdTodo])
    }
  }

  const handleDeleteTodo = async (id) => {
    const deleted = await todoService.deleteTodo(id)
    if (deleted) {
      setTodos((prev) => prev.filter((todo) => todo.id !== id))
    }
  }

  const handleUpdateTodo = async (id, title, description, completed) => {
    const updated = await todoService.updateTodo(id, { title, description, completed })
    if (updated) {
      setTodos((prev) =>
        prev.map((todo) => (todo.id === id ? updated : todo)) // this ensures UI updates
      )
    }
  }

  return (
    <div className="app-container">
      <h1>Todo App</h1>
      <TodoForm onAddTodo={handleAddTodo} />
      <TodoList
        todos={todos}
        onDelete={handleDeleteTodo}
        onUpdate={handleUpdateTodo}
      />
    </div>
  )
}

export default App
