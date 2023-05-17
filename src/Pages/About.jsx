import Test from "../Components/Test.jsx";
import { useState } from "react";

function About(props) {
    // memo  ->  is used to prevent re-rendering of the component
    // RU:  используется для предотвращения повторного рендеринга компонента

    // useState  ->  is used to create a memory of the component
    // RU: используется для создания памяти компонента

    

    const [count, setCount] = useState(0);
    const [str, setStr] = useState("Hello world");

    return (
        <div>
            <h1>About</h1>
            <button onClick={() => setCount(count+1)}>
                Increment +1  = {count}
            </button>

            <Test str={str} />
        </div>
    )
}
export default About