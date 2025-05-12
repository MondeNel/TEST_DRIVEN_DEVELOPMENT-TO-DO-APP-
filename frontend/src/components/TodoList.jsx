import React from 'react'
import TodoItem from './TodoItem'

/**
 * Component to display a list of todo items.
 *
 * @component
 * @param {Object} props - Props passed to the component.
 * @param {Array} props.todos - List of todos to display.
 * @param {Function} props.onToggle - Function to handle the toggle of the completion status.
 * @param {Function} props.onDelete - Function to handle the deletion of a todo item.
 * @returns {JSX.Element}
 */
const TodoList = ({ todos, onToggle, onDelete,  onUpdate }) => {
  return (
    <div className="todo-list">
      {todos.length === 0 ? (
        <p>No todos available.</p>
      ) : (
        todos.map(todo => (
          <TodoItem
            key={todo.id}
            id={todo.id}
            title={todo.title}
            description={todo.description}
            completed={todo.completed}
            onToggle={onToggle}
            onDelete={onDelete}
            onUpdate={onUpdate}
          />
        ))
      )}
    </div>
  )
}

export default TodoList
