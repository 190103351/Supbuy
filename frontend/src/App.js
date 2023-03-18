
import React from 'react';
import Navbar from './components/Navbar';
import Home1 from './components/home1';
import Home2 from './components/home2';
import Footer from './components/footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css';
import Home from './pages/home';
function App() {
  return (
    <React.Fragment>
      <Navbar/>
       <Home/>
       <Footer/>
    </React.Fragment>
  );
}

export default App;
