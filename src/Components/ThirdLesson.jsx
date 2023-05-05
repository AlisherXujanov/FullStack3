// hooks - useState
// darkMode example
// onClick={...} with try-catch 
import { useState } from 'react';

function ThirdLesson(props) {
    let [theme, setTheme] = useState('light')
    return (
        <>
            <h3>Third Lesson</h3>
            { theme }
            <button>
                Click me!
            </button>
        </>
    )
}


export default ThirdLesson;
