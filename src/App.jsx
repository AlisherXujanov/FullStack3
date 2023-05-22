import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Layout from './Components/Layout'
import MainPage from './Pages/MainPage'
import About from './Pages/About'
import NoPage from './Pages/NoPage'
import Register from './Components/Authentication/Register'
import Login from './Components/Authentication/Login'
import CardDetails from './Components/Card/CardDetails'
import UseReducer from './Pages/UseReducer'
import SendEmail from './Pages/SendEmail'
import 'bootstrap/dist/css/bootstrap.min.css'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    <div className="App">
      <ToastContainer />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<MainPage />} />
            <Route path="/About" element={<About toast={toast} />} />
            <Route path="/Register" element={<Register />} />
            <Route path="/Login" element={<Login />} />
            <Route path="/cardDetails" element={<CardDetails />} />
            <Route path="/useReducer" element={<UseReducer toast={toast} />} />
            <Route path="/sendEmail" element={<SendEmail />} />
            <Route path="*" element={<NoPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;