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

function Todos(props) {
    const [todos, dispatch] = useReducer(reducer, initialTodos);

    const [cards, setCards] = useState([{id: 0, title: "Card 1"}]);
    function addCard() {
        let cardDiv = document.getElementById("card-text");
        let cardText = cardDiv.value === "" ? `Next Card` : cardDiv.value;
        setCards([...cards, {id: cards.length, title: cardText}]);
        props.toast(`${cardText} added!`);
        cardDiv.value = "";
    }

    // useReducer =>  is used to manage state in complex cases
    // RU: используется для управления состоянием в сложных случаях 

    const handleComplete = (todo) => {
        dispatch({ type: "COMPLETE",  id: todo.id });
    };
    let lineThroug = { textDecoration: "line-through" }
    let cardStyle = {
        margin: "10px",
        padding: "10px",
        display: "inline-block",
        background: 'linear-gradient(to right, #4facfe, #00f2fe)',
        color: 'snow',
    }


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
            <hr />
            <input type="text" id="card-text" />
            <button onClick={addCard}>Add Card</button>
            <hr />
            {cards.map(card => (
                <div style={cardStyle} className="card" key={card.id}>
                    <h1>{card.title}</h1>
                </div>
            ))}
        </>
    );
}

export default Todos