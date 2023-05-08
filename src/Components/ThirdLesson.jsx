// hooks - useState
// darkMode example
// onClick={...} with try-catch 
import { useState } from 'react';
import './theme.css'

function ThirdLesson(props) {
    let [lorem, setLorem] = useState(false)

    const showP = {display: "block"}
    const hideP = {display: "none"}

    return (
        <div> 
            <p style={lorem ? showP : hideP}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit, officiis. Quasi debitis vero eum libero voluptatem, quis nesciunt natus perspiciatis error praesentium tempore saepe quae quod id. Asperiores, ducimus exercitationem.</p>
            <p style={lorem ? hideP : showP}>Далеко-далеко за словесными горами в стране гласных и согласных, живут рыбные тексты. Щеке домах безорфографичный если. Lorem, эта текста, предупредила запятой составитель даже необходимыми, переписывается инициал маленький мир дал. Несколько, щеке бросил.</p>

            <button onClick={() => {setLorem(!lorem)}}>
                <span style={lorem ? showP : hideP}>Lorem</span>
                <span style={lorem ? hideP : showP}>Lorem RU</span>
            </button>
        </div>
    )
}


export default ThirdLesson;
