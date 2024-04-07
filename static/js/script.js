document.getElementById('submit-btn').addEventListener('click', function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var message = document.getElementById('message');

    if(username === "admin" && password === "admin") {
        message.innerHTML = "Успешная авторизация!";
    } else {
        message.innerHTML = "Проверьте данные или зарегистрируйтесь!";
    }
});
