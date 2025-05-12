import React, { useState } from 'react'
import TodoForm from './components/TodoForm'
import TodoItem from './components/TodoItem'


/**
 * Main application component for managing todos.
 *
 * @component
 */
function App() {
  const [todos, setTodos] = useState([])

  const handleAddTodo = (todo) => {
    setTodos(prev => [...prev, todo])
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
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          id={todo.id}
          title={todo.title}
          description={todo.description}
          completed={todo.completed}
          onToggle={handleToggle}
          onDelete={handleDelete}
        />
      ))}
    </div>
  )
}

export default App
