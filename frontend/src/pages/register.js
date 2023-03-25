import React from 'react';

function register_page(){
    return (
        <div className='container  login-container'>
            <div className='row'>
                <div className='col'>
                <h3>Регистрация </h3>
                <p>Создайте свою учетную запись, чтобы получить все функции</p>
                <div><input className ='fieldl' placeholder='Название организации'></input></div>
                <div><input className ='fieldl' placeholder='ИИН/БИН'></input></div>
                <div><input className ='fieldl' placeholder='Полное имя'></input></div>
                <div><input className ='fieldl' placeholder='Мобильный телефон'></input></div>
                <div><input className ='fieldl' placeholder='Электронная  почта'></input></div>
                <div><input className ='fieldl' placeholder='Юридический адрес '></input></div>
                <div><input className ='fieldl' placeholder='Пароль'></input></div>
                <div><input className ='fieldl' placeholder='Повторите пароль'></input></div>
                <div><input className ='fieldl' placeholder=' Подтверждающий документ/лицензия '></input></div> 
                <button className='orange-button' id='register-btn'>
                        Зарегистрироваться
                    </button>               
                </div>
                <div className='col'>
                    <div className='content-register'>
                        <div>
                            <h3>Заполнение данных</h3>
                            <p>Для регистрации вам нужно заполнить все  необходимые данные.</p>
                        </div>
                        <div>
                            <h3>Придумайте пароль</h3>
                            <p>Пароль должен содержать не менее 8 символов, состоящих из не менее одной буквы в верхнем регистре, одной буквы в нижнем регистре и цифры</p>
                        </div>
                        <div>
                            <h3>Лицензия</h3>
                            <p>Для успешной регистрации вам нужно загрузить PDF вариант лицензии,подтверждающий о наличии ИП ТОО</p>
                        </div>
                    </div>
                </div>

            </div>
            
        </div>
    )



}

export default register_page;