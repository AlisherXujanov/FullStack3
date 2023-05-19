import { useLocation } from 'react-router-dom'
const cards = [
    {
        id: 1,
        img: '',
        title: 'Главные турниры октября',
        subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
        owner: {
            img: '',
            name: 'Максим Рихтер',
            date: '12.10.2021',
            views: '1,2k'
        }
    },
    {
        id: 2,
        img: '',
        title: 'Lorem test text 2',
        subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
        owner: {
            img: '',
            name: 'Максим Рихтер',
            date: '12.10.2021',
            views: '1,2k'
        }
    },
    {
        id: 3,
        img: '',
        title: 'This is 3rd title',
        subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
        owner: {
            img: '',
            name: 'Максим Рихтер',
            date: '12.10.2021',
            views: '1,2k'
        }
    },
    {
        id: 4,
        img: '',
        title: 'Главные турниры октября',
        subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
        owner: {
            img: '',
            name: 'Максим Рихтер',
            date: '12.10.2021',
            views: '1,2k'
        }
    },
    {
        id: 5,
        img: '',
        title: 'Lorem test text 2',
        subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
        owner: {
            img: '',
            name: 'Максим Рихтер',
            date: '12.10.2021',
            views: '1,2k'
        }
    },
    {
        id: 6,
        img: '',
        title: 'This is 3rd title',
        subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
        owner: {
            img: '',
            name: 'Максим Рихтер',
            date: '12.10.2021',
            views: '1,2k'
        }
    },
]
function CardDetails() {
    const location = useLocation()
    const { from } = location.state

    // useLocation  => is used to get data from Link
    //                 to another page
    // RU: используется для получения данных из Link
    //                 на другую страницу

    let card = cards.find(card => card.id == from)

    return (
        <>
            <h1>Card Details</h1>
            <p>Title: { card.title }</p>
            <p>Subtitle: { card.subtitle }</p>
            <p>Owner: { card.owner.name }</p>
        </>
    );
}

export default CardDetails;