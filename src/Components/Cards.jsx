import Card from './Card'
import './style.css'

function Cards(props) {

    const cards = [
        {
            img: '',
            title: 'Главные турниры октября',
            subtitle: 'FURIA представила помощника тренера. Отныне tacitus...',
            owner: {
                img: '',
                name: 'Максим Рихтер',
                date: '12.10.2021',
                views: '1,2k'
            }
        }
    ]
    return (
        <div className='cards'>
            {cards.map((card, index) => {
                return (
                    <Card key={index} card={card} />
                )
            })}
        </div>
    );
}

export default Cards;