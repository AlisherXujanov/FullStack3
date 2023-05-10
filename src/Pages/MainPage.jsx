import News from "../Components/News";
import mainStyle from '../Assets/styles/home.css'

function MainPage(props) {
    return (
        <header style={mainStyle}>
            <main>
                <News />
            </main>
        </header>
    )
}

export default MainPage