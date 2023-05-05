import SecondLesson from './Components/SecondLesson'
import ThirdLesson from './Components/ThirdLesson'

function App() {
  let people = [
    { name: 'John', age: 20 },
    { name: 'Jane', age: 30 },
    { name: 'Joe', age: 40 },
    { name: 'Jill', age: 50 },
    { name: 'Jack', age: 60 }
  ]
  const thirdLessonStyle = {
    padding: "20px",
    margin: "20px",
  }
  return (
    <div className="App">
      <h1>Hello world</h1>

      <SecondLesson люди={people} >
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto nulla rem nisi alias minus cum voluptatibus placeat laboriosam reiciendis incidunt. In, accusantium! Possimus iure molestiae, maiores voluptatibus minus distinctio similique?</p>
      </SecondLesson>

      <div style={thirdLessonStyle}>
        <ThirdLesson />
      </div>

    </div>
  );
}

export default App;