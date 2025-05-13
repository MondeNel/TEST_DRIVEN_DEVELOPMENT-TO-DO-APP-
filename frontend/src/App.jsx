import React, { useState, useEffect } from 'react';
import todoService from '../services/todoService.js';
import TodoItem from './components/TodoItem';
import TodoForm from './components/TodoForm';

const App = () => {
  const [todos, setTodos] = useState([]);

  // Fetch todos on component mount
  useEffect(() => {
    const fetchTodos = async () => {
      const todos = await todoService.getTodos();
      setTodos(todos);
    };

    fetchTodos();
  }, []);

  // Add a new todo
  const handleAddTodo = (newTodo) => {
    setTodos([...todos, newTodo]);
  };

  // Toggle todo completion status
  const handleToggleTodo = (id) => {
    const updatedTodos = todos.map((todo) =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    );
    setTodos(updatedTodos);
  };

  // Handle todo update
  const handleUpdateTodo = (updatedTodo) => {
    const updatedTodos = todos.map((todo) =>
      todo.id === updatedTodo.id ? updatedTodo : todo
    );
    setTodos(updatedTodos);
  };

  // Handle todo deletion
  const handleDeleteTodo = (id) => {
    const updatedTodos = todos.filter((todo) => todo.id !== id);
    setTodos(updatedTodos);
  };

  return (
    <div>
      <TodoForm onAddTodo={handleAddTodo} />
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          {...todo}
          onToggle={handleToggleTodo}
          onDelete={handleDeleteTodo}
          onUpdate={handleUpdateTodo}
        />
      ))}
    </div>
  );
};

export default App;
