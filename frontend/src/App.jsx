import React from 'react'
import TodoForm from './components/TodoForm'

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
    </div>
  )
}

export default App
