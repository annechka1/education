$(document).ready(function () {
    $("#button_1").click(function (e) {
        x = $("#exampleInputUsername1").val()
        if (x.length < 4) {
            alert("Введите в поле имя пользователя больше 4 символов")
            e.preventDefault()
        }
    });
});

$(document).ready(function () {
    $("#button_2").click(function (e) {
        x = $("#exampleInputUsername2").val()
        if (x.length < 4) {
            alert("Введите в поле имя пользователя больше 4 символов")
            e.preventDefault()
        }
    });
});
$("#exampleInputUsername2").blur(function() {
    $.post("cheak_login",
        {
            "login": $("#exampleInputUsername2").val()
        },
        function(response) {
            if(response.exist === 1){
                alert("Пользователь с таким логином уже существует")
            }
        }
    )
});


$(document).ready(function () {
    $("#button_1").click(function (e) {
        k = $("#exampleInputPassword1").val()
        if (k.length < 3) {
            alert("Введите в поле пароль больше 3 символов")
            e.preventDefault()
        }
    });
});
$(document).ready(function () {
    $("#button_2").click(function (e) {
        g = $("#exampleInputPassword2").val()
        if (g.length < 4) {
            alert("Введите в поле пароль больше 3 символов")
            e.preventDefault()
        }
    });
});

let anchors = document.querySelectorAll('container-fluid a[href*="#"]');

    for (anchor of anchors){
        if (anchor){
            anchor.addEventListener("click",function (e){
                e.preventDefault();
                anchorId = this.getAttribute("href");
                document.querySelector(anchorsId).scrollIntoView({
                    behavior:"smooth",block:"start"
                    }
                )
            })
        }
    }