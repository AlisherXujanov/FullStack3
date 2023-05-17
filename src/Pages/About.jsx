import Test from "../Components/Test.jsx";
import { useState, useEffect } from "react";

function About(props) {
    const [count, setCount] = useState(0);
    const [str, setStr] = useState("Hello world");


    // useEffect(callback, dependency)   =>   is used to update the component 
    //                              every time when the dependency is changed
    // RU: используется для обновления компонента каждый раз, когда изменяется зависимость

    
    const reqresUrl = "https://reqres.in/api/users?page=2"
    useEffect(() => {
        fetch(reqresUrl)
            .then(response => response.json())
            .then(info => console.log(info.data))
    }, [count])

    return (
        <div>
            <h1>About</h1>
            <button onClick={() => setCount(count+1)}>
                Increment +1  = {count}
            </button>

            <br />
            <br />
            <input onChange={(e) => setStr(e.target.value)} value={str} />
            <p>{ str }</p>

        </div>
    )
}
export default About