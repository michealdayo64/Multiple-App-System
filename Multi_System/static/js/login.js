const passToggle = document.querySelector('.password-toggle');
const passwordField = document.querySelector('#passwordField');

const togglePasswordBtn = (e) =>{
    if(passToggle.textContent === "SHOW"){
        passToggle.textContent = 'HIDE'
        passwordField.setAttribute('type', 'text');
    }else{
        passToggle.textContent = 'SHOW'
        passwordField.setAttribute('type', 'password')
    }
} 

passToggle.addEventListener('click', togglePasswordBtn)