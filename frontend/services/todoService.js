import axios from 'axios';

// Base URL of your FastAPI backend
const API_URL = 'http://127.0.0.1:8000'; 

const todoService = {
  // Get all todos
  getTodos: async () => {
    try {
      const response = await axios.get(`${API_URL}/todos`);
      return response.data;
    } catch (error) {
      console.error('Error fetching todos:', error);
      return [];
    }
  },

  // Create a new todo
  createTodo: async (todoData) => {
    try {
      const response = await axios.post(`${API_URL}/todos`, todoData);
      return response.data;
    } catch (error) {
      console.error('Error creating todo:', error);
      return null;
    }
  },

  // Update a todo
  updateTodo: async (id, updatedData) => {
    try {
      const response = await axios.put(`${API_URL}/todos/${id}`, updatedData);
      return response.data;
    } catch (error) {
      console.error('Error updating todo:', error);
      return null;
    }
  },

  // Delete a todo
  deleteTodo: async (id) => {
    try {
      const response = await axios.delete(`${API_URL}/todos/${id}`);
      return response.data;
    } catch (error) {
      console.error('Error deleting todo:', error);
      return null;
    }
  },
};

export default todoService;
