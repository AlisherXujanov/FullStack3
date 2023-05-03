import SecondLesson from './Components/SecondLesson'
import CarTable from './Components/CarTable.jsx'

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
  let cars = [
    { name: 'BMW',      cost: 10000,   color: 'red' },
    { name: 'Mercedes', cost: 20000,   color: 'orange' },
    { name: 'Toyota',   cost: 30000,   color: 'green' },
    { name: 'Nissan',   cost: 40000,   color: 'yellow' },
    { name: 'Lexus',    cost: 50000,   color: 'brown' }
  ]

  return (
    <div className="App">
      <h1>Hello world</h1>

      <SecondLesson люди={people} fruits={фрукты}>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto nulla rem nisi alias minus cum voluptatibus placeat laboriosam reiciendis incidunt. In, accusantium! Possimus iure molestiae, maiores voluptatibus minus distinctio similique?</p>
      </SecondLesson>

      <CarTable cars={cars} />
    </div>
  );
}

export default App;


// FIRST TASK
// 1. Create a CarTable component and call it from App.jsx
//    RU Создайте компонент CarTable и вызовите его из App.jsx

// 2. Send cars data to CarTable component as props
//    RU: Отправьте данные автомобилей в компонент CarTable в качестве props

// 3. Use loop to create table rows and each row should 
//    be a separate component called Car
//    RU: Используйте цикл для создания строк таблицы,