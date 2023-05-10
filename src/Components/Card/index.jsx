import cardStyle from './style.css'

function Card({card}) {
    return (
        <div style={cardStyle} className="card">
            <div className="card-img">
                <img src={card.img} width='100%' height='200' />
            </div>
            <div className="card-footer">
                <h4 className='card-title'>{card.title}</h4>
                <p className='card-subtitle'>{card.subtitle}</p>
                <div className="bottom">
                    <div className="left">
                        <img src={card.owner.img} width='15' height='15' />
                        <p>{card.owner.name}  {card.owner.date}</p>
                    </div>
                    <div className="right">
                        <p>{card.owner.views}</p>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Card;