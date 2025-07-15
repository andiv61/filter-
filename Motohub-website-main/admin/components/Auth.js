import React from 'react';

const Auth = () => {
 return (
 <div className="auth-container">
 <h1>Вход в админ-панель</h1>
 <form>
 <input type="text" placeholder="Логин" />
 <input type="password" placeholder="Пароль" />
 <button type="submit">Войти</button>
 </form>
 </div>
 );
};

export default Auth;
