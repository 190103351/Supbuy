import React from 'react';

function login_page(){
    return (
        <div className='container login-container'>
            <div className='row'>
                <div className='col'>
                <h2>Supbuy.kz - Вход</h2>
                <div><input className ='fieldl' placeholder='Ваш номер телефона'></input></div>
                <div><input className ='fieldl' placeholder='Пароль' type='password'></input></div>
                <button className='orange-button' onClick={()=>{
                    window.location.href='/'
                }}>Войти</button>
                <a href='#'>Забыли пароль?</a>
                </div>

            </div>
            
        </div>
    )



}

export default login_page;