import layout from './style.scss'
import { Link, Outlet } from 'react-router-dom'
import { useEffect } from 'react'

function Layout(props) {
    useEffect(() => {
        activateCurrentPath()
    }, [])

    function activateCurrentPath() {
        let currentPath = window.location.pathname
        const links = document.querySelectorAll('nav a')
        links.forEach(link => {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active')
            }
        })
    }
    const activate = (event) => {
        const links = document.querySelectorAll('nav a')
        links.forEach(link => {
            link.classList.remove('active')
        })
        event.target.classList.add('active')
    }

    return (
        <>
            <nav style={layout}>
                <div className='left'>
                    <Link onClick={(event) => activate(event)} to="/">Home</Link>
                    <Link onClick={(event) => activate(event)} to="/About">About</Link>
                    <Link onClick={(event) => activate(event)} to="/useReducer">Use Reducer</Link>
                    <Link onClick={(event) => activate(event)} to="/sendEmail">Send email</Link>
                </div>
                <div>
                    <Link onClick={(event) => activate(event)} to="/Login">Login</Link>
                    <Link onClick={(event) => activate(event)} to="/Register">Register</Link>
                </div>
            </nav>
            <Outlet />
        </>
    )
}

export default Layout