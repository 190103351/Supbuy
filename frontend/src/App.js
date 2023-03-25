
import React from 'react';
import Navbar from './components/Navbar';
import { BrowserRouter, Link, Outlet, useRoutes } from 'react-router-dom';
import Footer from './components/footer';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css';
import Home from './pages/home';
import Login from './pages/login';
import Register from './pages/register';
import Profile from './pages/profile';


function App() {
  const routes = useRoutes([
    { path: '/', element: <Home /> },
    { path: 'login', element: <Login /> },
    {path:'register',element:<Register/>},
    {path:'profile',element:<Profile/>}
   
  ]);
  return routes;
}

export default App;
