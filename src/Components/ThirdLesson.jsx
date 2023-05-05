// hooks - useState
// darkMode example
// onClick={...} with try-catch 
import { useState } from 'react';

function ThirdLesson(props) {
    let [theme, setTheme] = useState('light')

    function toggleTheme() {
        theme === 'dark' ? setTheme("light") : setTheme("dark")
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
        <>
            <h3>Third Lesson</h3>
            {theme}
            <button onClick={toggleTheme}>
                Click me!
            </button>
        </>
    )
}


export default ThirdLesson;
