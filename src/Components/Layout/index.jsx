import layout from './style.css'
import { Link, Outlet } from 'react-router-dom'

function Layout(props) {
    return (
        <>
            <nav style={layout}>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/About">About</Link>
                    </li>
                    <li>
                        <Link to="/404">404</Link>
                    </li>
                    <li>
                        <Link to="/Login">Login</Link>
                    </li>
                    <li>
                        <Link to="/Register">Register</Link>
                    </li>
                    <li>
                        <Link to="/useReducer">Use Reducer</Link>
                    </li>
                    
                </ul>
            </nav>
            <Outlet />
        </>
    )
}

export default Layout