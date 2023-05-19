import { useReducer, useState } from "react";

const initialTodos = [
    {
        id: 1,
        title: "Todo 1",
        complete: false,
    },
    {
        id: 2,
        title: "Todo 2",
        complete: false,
    },
];
const reducer = (state, action) => {
    switch (action.type) {
        case "COMPLETE":
            return state.map((todo) => {
                if (todo.id === action.id) {
                    return { ...todo, complete: !todo.complete };
                } else {
                    return todo;
                }
            });
        default:
            return state;
    }
};

function Todos() {
    const [todos, dispatch] = useReducer(reducer, initialTodos);

    // useReducer =>  is used to manage state in complex cases
    // RU: используется для управления состоянием в сложных случаях 

    const handleComplete = (todo) => {
        dispatch({ type: "COMPLETE",  id: todo.id });
    };
    let lineThroug = { textDecoration: "line-through" }

    return (
        <>
            {todos.map(todo => (
                <div key={todo.id}>
                    <label style={ todo.complete ? lineThroug : null }>
                        <input
                            type="checkbox"
                            checked={todo.complete}
                            onChange={() => handleComplete(todo)}
                            
                        />
                        {todo.title}
                    </label>
                </div>
            ))}
        </>
    );
}

export default Todos