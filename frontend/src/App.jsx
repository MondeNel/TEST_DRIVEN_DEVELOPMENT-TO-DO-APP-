import React from 'react'
import TodoForm from './components/TodoForm'
import TodoItem from './components/TodoItem'

/**
 * Root App component that renders the TodoForm.
 *
 * @component
 * @returns {JSX.Element}
 */
function App() {
  return (
    <div className="app">
      <h1>Todo App</h1>
      <TodoForm />
      <TodoItem />
    </div>
  )
}

export default App
