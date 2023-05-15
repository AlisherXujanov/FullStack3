import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './Components/Layout'
import MainPage from './Pages/MainPage'
import About from './Pages/About'
import NoPage from './Pages/NoPage'
import Register from './Components/Authentication/Register'
import Login from './Components/Authentication/Login'
import  'bootstrap/dist/css/bootstrap.min.css'

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={ <Layout /> }>
            <Route index element={ <MainPage /> } />
            <Route path="/About" element={<About />} />
            <Route path="/Register" element={<Register />} />
            <Route path="/Login" element={<Login />} />
            <Route path="*" element={<NoPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;