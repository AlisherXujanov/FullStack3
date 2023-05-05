// hooks - useState
// darkMode example
// onClick={...} with try-catch 
import { useState } from 'react';
import './theme.css'

function ThirdLesson(props) {
    let [theme, setTheme] = useState(false)

    function toggleTheme() {
        setTheme(!theme)
        // theme === true ? setTheme(false) : setTheme(true)
        // try {
        //     throw new Error("Some error")
        //     theme === 'dark' ? setTheme("light") : setTheme("dark")
        // } catch (error) {
        //     console.error(error)
        // } finally {
        //     console.log("finally. This is the code that will always run")
        // }
    }
    return (
        <div className={theme ? "dark-mode" : "light-mode"}> 
            <h3>Third Lesson</h3>
            {theme}
            <button onClick={toggleTheme}>
                Click me!
            </button>
        </div>
    )
}


export default ThirdLesson;
