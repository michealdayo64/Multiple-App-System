const usernameField = document.querySelector('#usernameField');
const emailField = document.querySelector('#emailField');
const invalidFeeback = document.querySelector('.username-errorr');
const invalidEmail = document.querySelector('.email-errorr');
const usernameChecking = document.querySelector('#username-cheking');
const passToggle = document.querySelector('.password-toggle');
const passToggle2 = document.querySelector('.password-toggle2');
const passwordField = document.querySelector('#passwordField');
const passwordField2 = document.querySelector('#passwordField2');
const passwordValidation = document.querySelector('.password-val');
const registerBtn = document.querySelector('.registerBtn');

var passwordInput;
var passwordInput2;

passwordValidation.style.display = 'none';

passwordField.addEventListener('keyup', (e) =>{
    passwordInput = e.target.value;
    if(passwordInput === passwordInput2 && passwordInput.length > 0){
        passwordValidation.style.display = 'block';
        passwordValidation.innerHTML = `<p style="color:green;">Password Match </p>`
    }else if(passwordInput !== passwordInput2){
        //passwordValidation.style.display = 'block';
        passwordValidation.innerHTML = `<p style="color:red;">Password does Match </p>`
        passwordValidation.style.display = 'block';
    }
})

passwordField2.addEventListener('keyup', (e) => {
    passwordInput2 = e.target.value;
    if(passwordInput2 === passwordInput && passwordInput2.length > 0){
        passwordValidation.style.display = 'block';
        passwordValidation.innerHTML = `<p style="color:green;">Password Match </p>`
    }else if(passwordInput !== passwordInput2){
        passwordValidation.style.display = 'block';
        passwordValidation.innerHTML = `<p style="color:red;">Password does Match </p>`
    }
})



const toggleBtn = (e) =>{
    if(passToggle.textContent === 'SHOW'){
        passToggle.textContent = 'HIDE'
        passToggle.style.color = "grey";
        passwordField.setAttribute("type", "text");
    }else{
        passToggle.textContent = "SHOW";
        passToggle.style.color = "green";
        passwordField.setAttribute("type", "password");
    }
}

const toggleBtn2 = (e) =>{
    if(passToggle2.textContent === 'SHOW'){
        passToggle2.textContent = 'HIDE'
        passToggle.style.color = "grey";
        passwordField2.setAttribute("type", "text");
    }else{
        passToggle2.textContent = "SHOW";
        passToggle.style.color = "grey";
        passwordField2.setAttribute("type", "password");
    }
}

// Password Toggle 1
passToggle.addEventListener('click', toggleBtn)

// Password Toggle 2
passToggle2.addEventListener('click', toggleBtn2);


// Username Validation
usernameField.addEventListener("keyup", (e) =>{
    const userInput = e.target.value;
    //console.log(userInput);
    if(userInput.length > 0){
        usernameChecking.style.display = 'block';
        usernameChecking.textContent = `Checking ${userInput}`

        fetch('http://127.0.0.1:8000/account/usernameValidation/',{
        body: JSON.stringify({'username': userInput}),
        method: 'POST'
    }).then((res) => res.json()).then((data) =>{
        console.log(data)
        usernameChecking.style.display = 'none';
        if(data.username_error){
            //usernameField.classList.add('is-invalid')
            //usernameChecking.style.display = 'none';
            registerBtn.disabled = true;
            invalidFeeback.style.display = 'block';
            invalidFeeback.innerHTML = `<p style="color:red; font-size:10px;">${data.username_error}</p>`
        }else if(data.username_exist){
            registerBtn.disabled = true;
            invalidFeeback.style.display = 'block';
            invalidFeeback.innerHTML = `<p style="color:red; font-size:10px;">${data.username_exist}</p>`
        }else{
            invalidFeeback.style.display = 'none';
            registerBtn.disabled = false;
            //usernameChecking.style.display = 'block';
        }
    })
    }

});


// Email Validation
emailField.addEventListener("keyup", (e) =>{
    const emailInput = e.target.value;
    console.log(emailInput);
    if(emailInput.length > 0){
        fetch('http://127.0.0.1:8000/account/emailValidation/',{
        body: JSON.stringify({'email': emailInput}),
        method: 'POST'
    }).then((res) => res.json()).then((data) =>{
        console.log(data)
        if(data.email_error){
            console.log(data.email_error)
            //usernameField.classList.add('is-invalid')
            registerBtn.disabled = true;
            invalidEmail.style.display = 'block';
            invalidEmail.innerHTML = `<p style="color:red; font-size:10px;">${data.email_error}</p>`
        }else{
            invalidEmail.style.display = 'none';
            registerBtn.disabled = false;
        }
    })
    }
});
