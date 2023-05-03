function Car({ car }) {
    return (
        <tr>
            <td>{car.name}</td>
            <td>{car.cost}</td>
            <td>{car.color}</td>
        </tr>
    )
}
function CarTable(props) {
    return (
        <table border="5" bordercolor='blue'>
            {props.cars.map((car, index) => {
                return (
                    <Car car={car} key={index} />
                )
            })}
        </table>
    )
}


export default CarTable;