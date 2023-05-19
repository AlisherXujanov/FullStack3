import cardStyle from './style.css'
import { Link, Outlet } from 'react-router-dom'

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
                    <Link to="/cardDetails" state={{ from: String(card.id) }}>
                        View
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default Card;