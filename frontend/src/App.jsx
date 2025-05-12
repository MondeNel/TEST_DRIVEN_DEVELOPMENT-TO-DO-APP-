import React, { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import TodoForm from './components/TodoForm'
import TodoList from './components/TodoList'
import Home from './pages/Home'

/**
 * Main application component for managing todos and routing.
 *
 * @component
 */
function App() {
  const [todos, setTodos] = useState([])

  const handleAddTodo = (todo) => {
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

  const handleUpdate = (id) => {
  const updatedTitle = prompt('Enter new title:')
  const updatedDescription = prompt('Enter new description:')

  if (updatedTitle !== null && updatedDescription !== null) {
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id
          ? { ...todo, title: updatedTitle, description: updatedDescription }
          : todo
      )
    )
  }
}


  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route 
            path="/todos" 
            element={<div>
                        <TodoForm onAddTodo={handleAddTodo} />
                        <TodoList todos={todos} onToggle={handleToggle} onDelete={handleDelete} onUpdate={handleUpdate}/>
                      </div>}
          />
        </Routes>
      </div>
    </Router>
  )
}

export default App
