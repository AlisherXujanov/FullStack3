// Prop drilling and using useContext
import { useContext, createContext } from "react";
const TextContext = createContext();

// useContext => is used to pass data from parent to 
//               child without prop drilling
// RU: используется для передачи данных от родителя к
//    ребенку без 'prop drilling'

// We have to use createContext() to create context
// and show that context is a variable in useContext()
// EX: 
// const TextContext = createContext();
// let x = useContext(TextContext);


function Test(props) {
    return (
        <>
            <Test2 />
        </>
    );
}

function Test2(props) {
    return (
        <>
            <Test3 />
        </>
    );
}
function Test3(props) {
    return (
        <>
            <Test4 />
        </>
    );
}
function Test4(props) {
    return (
        <>
            <Test5 />
        </>
    );
}
function Test5(props) {
    const qwe = useContext(TextContext);
    return (
        <>
            <h1>{ qwe.key }</h1>
        </>
    );
}
     


function About(props) {

    const notify = () => props.toast("Wow so easy!");

    return (
        <div>
            <h1>About</h1>

            <TextContext.Provider value={{key: "Hello world"}}>
                <Test />
            </TextContext.Provider>

            <button onClick={notify}>
                Show toast
            </button>

        </div>
    )
}
export default About