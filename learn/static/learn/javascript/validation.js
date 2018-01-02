


function validateForm() {
    var x = document.forms["signForm"]["username"].value;
    var y = document.forms["signForm"]["email"].value;
    var z = document.forms["signForm"]["password1"].value;
    var w = document.forms["signForm"]["password2"].value;
    var email_check = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;

    if (x == "") {
        alert("Name must be filled out");
        return false;
    }

    else if (y == "") {
        alert("email must be filled out");
        return false;

    }

    else if (z == "") {
        alert("password must be filled out");
        return false;
    }


    else if (w == "") {
        alert("confirm password must be filled out");
        return false;
    }

    else if (z != w){
        alert("password are not matching");
        return false;
    }

     else if (!email_check.test(y)){
        alert("email does not contain valid syntax");
        return false;
    }

}

function loginValidate() {

    var x = document.forms["loginForm"]["username"].value;
    var y = document.forms["loginForm"]["password"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }

    else if (y == "") {
        alert("password must be filled out");
        return false;
    }

}

function forgetValidate() {

    var x = document.forms["forgetForm"]["email"].value;
    var email_check = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})+$/;
    if (x == "") {
        alert("email must be filled out");
        return false;
    }

    else if (!email_check.test(x)) {
        alert("email does not contain valid syntax");
        return false;
    }
}