import React from 'react'
import { Link } from 'react-router-dom'
import '../styles/home.css'

/**
 * Home page component.
 *
 * @component
 * @returns {JSX.Element}
 */
const Home = () => {
  return (
    <div className="home-page">
      <h2>Welcome to the Todo App</h2>
      <p>This is your home page. You can manage your todos from here.</p>
      <Link to="/todos">Go to Todos</Link>
    </div>
  )
}

export default Home
