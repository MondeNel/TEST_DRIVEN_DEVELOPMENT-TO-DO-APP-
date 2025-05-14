import axios from 'axios';

// Base URL of your FastAPI backend
const API_URL = 'http://127.0.0.1:8000'; // FastAPI running on PORT

/**
 * Service to interact with the Todo API.
 * Contains methods for CRUD operations.
 */
const todoService = {
  /**
   * Get all todos from the API.
   * @returns {Promise<Array>} List of all todo items.
   */
  getTodos: async () => {
    try {
      const response = await axios.get(`${API_URL}/todos`);
      return response.data;
    } catch (error) {
      console.error('Error fetching todos:', error);
      return [];
    }
  },

  /**
   * Create a new todo.
   * @param {Object} todoData - The data of the todo to create.
   * @returns {Promise<Object|null>} The created todo item or null if error occurs.
   */
  createTodo: async (todoData) => {
    try {
      const response = await axios.post(`${API_URL}/todos`, todoData);
      return response.data;
    } catch (error) {
      console.error('Error creating todo:', error);
      return null;
    }
  },

  /**
   * Update an existing todo.
   * @param {string} id - The ID of the todo to update.
   * @param {Object} updatedData - The data to update in the todo.
   * @returns {Promise<Object|null>} The updated todo item or null if error occurs.
   */
  updateTodo: async (id, updatedData) => {
    try {
      const response = await axios.put(`${API_URL}/todos/${id}`, updatedData);
      return response.data;
    } catch (error) {
      console.error('Error updating todo:', error);
      return null;
    }
  },

  /**
   * Delete a todo by ID.
   * @param {string} id - The ID of the todo to delete.
   * @returns {Promise<Object|null>} The response from the server or null if error occurs.
   */
  deleteTodo: async (id) => {
    try {
      // Log the ID to see it's being passed correctly
      console.log(`Deleting todo with ID: ${id}`);
      const response = await axios.delete(`${API_URL}/todos/${id}`);
      return response.data;
    } catch (error) {
      console.error('Error deleting todo:', error);
      return null;
    }
  }

};

export default todoService;
