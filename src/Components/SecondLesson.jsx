const TestComponent = (props) => {
    let mevalar = props.fruits.map((fruit, index) => {
        return (
            <>
                <tr key={index}>
                    <td> {fruit.name}  </td>
                    <td> {fruit.cost}  </td>
                    <td> {fruit.color} </td>
                </tr>
            </>
        )
    })
    return (
        <div>
            <table border={props.width} bordercolor={props.color}>
                {mevalar}
            </table>
        </div>
    )
}


function SecondLesson(props) {
    // props.люди   =>  people
    // let x = ['aaaa', 'bbbb', 'cccc']
    // let [a, b, c] = x

    // props.children  =>  is used to access the content between the 
    //                     opening and closing tags of a component
    // RU: props.children  =>  используется для доступа к содержимому 
    //                     между открывающим и закрывающим тегами компонента

    let odamlar = props.люди.map((person, index) => {
        return (
            <li key={index}>
                {person.name} - {person.age}
            </li>
        )
    })

    // fruits, width, color
    return (
        <>
            <h2>People</h2>
            {props.children}
            <ol>{odamlar}</ol>

            <TestComponent fruits={props.fruits} width={'10'} color={'red'} />
        </>
    )
}
export default SecondLesson

