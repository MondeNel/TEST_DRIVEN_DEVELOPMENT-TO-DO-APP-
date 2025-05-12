import React, { useState } from 'react'
import TodoForm from './components/TodoForm'
import TodoList from './components/TodoList'

/**
 * Main application component for managing todos.
 *
 * @component
 */
function App() {
  const [todos, setTodos] = useState([])

  const handleAddTodo = (todo) => {
    // Add a unique ID when a new todo is added
    const newTodo = { ...todo, id: Date.now().toString() }
    setTodos(prev => [...prev, newTodo])
  }

  const handleToggle = (id) => {
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    )
  }

  const handleDelete = (id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id))
  }

  return (
    <div className="app">
      <h1>Todo App</h1>
      <TodoForm onAddTodo={handleAddTodo} />
      <TodoList todos={todos} onToggle={handleToggle} onDelete={handleDelete} />
    </div>
  )
}

export default App
