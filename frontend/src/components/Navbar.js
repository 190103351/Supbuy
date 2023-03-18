import { useRef } from 'react';
import IMAGES from '../constants/image.js';

function Navbar() {
    const navRef = useRef()

    const showNavbar = ()=>{
        navRef.current.classList.toggle('responsive_nav')
    }

    return(
        <header>
            <h3 className='text-color-dark'>
                <img  />
            </h3>
            <nav ref={navRef}>
                <a href='#'><img src={IMAGES.img2 } height={50} width={60}/><span>Алматы</span></a>
                <a href='#'><img src={IMAGES.img1} height={50} width={60}/></a>
                
                

            <button onClick={()=>{
                console.log("Click")
            }} className = 'login-btn'>
               Вход
            </button>
            </nav>
           


        </header>
    );
    
}
export default Navbar;