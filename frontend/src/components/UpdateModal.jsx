import React, { useState } from 'react'
import '../styles/modal.css'

/**
 * Modal component for updating a todo.
 *
 * @param {Object} props
 * @param {string} props.title - Current title of the todo
 * @param {string} props.description - Current description of the todo
 * @param {Function} props.onClose - Function to close the modal
 * @param {Function} props.onSave - Function to save the updated todo
 */
const UpdateModal = ({ title: currentTitle, description: currentDesc, onClose, onSave }) => {
  const [title, setTitle] = useState(currentTitle)
  const [description, setDescription] = useState(currentDesc)

  const handleSave = () => {
    onSave(title, description)
    onClose()
  }

  return (
    <div className="modal-overlay">
      <div className="modal">
        <h3>Update Todo</h3>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Update title"
        />
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Update description"
        />
        <div className="modal-actions">
          <button onClick={handleSave}>Save</button>
          <button onClick={onClose}>Cancel</button>
        </div>
      </div>
    </div>
  )
}

export default UpdateModal
