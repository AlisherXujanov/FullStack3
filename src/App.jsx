import SecondLesson from './Components/SecondLesson'

function App() {
  let people = [
    { name: 'John', age: 20 },
    { name: 'Jane', age: 30 },
    { name: 'Joe', age: 40 },
    { name: 'Jill', age: 50 },
    { name: 'Jack', age: 60 }
  ]
  let фрукты = [
    { name: 'olma',     cost: 1000,    color: 'red' },
    { name: 'anor',     cost: 2000,    color: 'orange' },
    { name: 'shaftoli', cost: 3000,    color: 'green' },
    { name: 'gilos',    cost: 4000,    color: 'yellow' },
    { name: 'olcha',    cost: 5000,    color: 'brown' }
  ]

  return (
    <div className="App">
      <h1>Hello world</h1>

      <SecondLesson люди={people} fruits={фрукты}>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto nulla rem nisi alias minus cum voluptatibus placeat laboriosam reiciendis incidunt. In, accusantium! Possimus iure molestiae, maiores voluptatibus minus distinctio similique?</p>
      </SecondLesson>
    </div>
  );
}

export default App;
