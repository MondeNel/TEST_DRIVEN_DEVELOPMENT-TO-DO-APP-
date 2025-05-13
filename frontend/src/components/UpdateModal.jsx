import React, { useState } from 'react'
import '../styles/todoform.css'
import '../styles/modal.css' // only for overlay

/**
 * Modal component for updating a todo item.
 *
 * @component
 * @param {Object} props
 * @param {string} props.title - Current title of the todo
 * @param {string} props.description - Current description of the todo
 * @param {Function} props.onClose - Callback to close the modal
 * @param {Function} props.onSave - Callback to save the updated todo
 * @returns {JSX.Element} The modal component
 */
const UpdateModal = ({ title: currentTitle, description: currentDesc, onClose, onSave }) => {
  const [title, setTitle] = useState(currentTitle)
  const [description, setDescription] = useState(currentDesc)

  const handleUpdate = (e) => {
    e.preventDefault()
    if (!title.trim()) return alert('Title cannot be empty.')
    onSave(title, description)
    onClose()
  }

  return (
    <div className="modal-overlay">
      <div className="todo-form-container">
        <h2>Update Todo</h2>
        <form onSubmit={handleUpdate} className="todo-form">
          <div className="form-group">
            <label htmlFor="update-title">Title</label>
            <input
              id="update-title"
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Update title"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="update-description">Description</label>
            <textarea
              id="update-description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Update description"
            />
          </div>
          <div style={{ display: 'flex', gap: '1rem', justifyContent: 'flex-end' }}>
            <button type="submit">Update Todo</button>
            <button
              type="button"
              onClick={onClose}
              style={{
                backgroundColor: '#6c757d',
              }}
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default UpdateModal
