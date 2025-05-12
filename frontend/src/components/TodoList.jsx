import React from 'react'
import TodoItem from './TodoItem'

/**
 * Renders a list of todo items.
 *
 * @component
 * @param {Object} props
 * @param {Array} props.todos - Array of todo objects.
 * @param {Function} props.onToggle - Function to toggle completion.
 * @param {Function} props.onDelete - Function to delete a todo.
 * @returns {JSX.Element}
 */
const TodoList = ({ todos, onToggle, onDelete }) => {
  return (
    <div className="todo-list">
      {todos.length === 0 ? (
        <p>No todos added yet.</p>
      ) : (
        todos.map((todo) => (
          <TodoItem
            key={todo.id}
            id={todo.id}
            title={todo.title}
            description={todo.description}
            completed={todo.completed}
            onToggle={onToggle}
            onDelete={onDelete}
          />
        ))
      )}
    </div>
  )
}

export default TodoList
