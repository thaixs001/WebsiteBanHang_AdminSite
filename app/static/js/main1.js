function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password-field").value;

    if (username === "admin" && password === "123456") {
        swal({
            title: "",
            text: "Xin chào Nguyễn Thái",
            icon: "success",
            close: true,
            button: false
        });
        window.location = "home_page.html";
        return true;
    }


    if (username === "" && password === "") {
        swal({
            title: "",
            text: "Bạn chưa điền đầy đủ thông tin đăng nhập...",
            icon: "error",
            close: true,
            button: "Thử lại"
        });
        return false;
    }

    if (username === "admin" && password === "") {
        swal({
            title: "",
            text: "Bạn nhập mật khẩu không đúng...",
            icon: "warning",
            close: true,
            button: "Thử lại"
        });
        return false;
    }

    if (username === null || username === "") {
        swal({
            title: "",
            text: "Tài khoản đang trống...",
            icon: "warning",
            close: true,
            button: "Thử lại"
        });
        return false;
    }

    if (password === null || password === "") {
        swal({
            title: "",
            text: "Mật khẩu đang trống...",
            icon: "warning",
            close: true,
            button: "Thử lại"
        });
        return false;
    } else {
        swal({
            title: "",
            text: "Sai thông tin đăng nhập hãy kiểm tra lại...",
            icon: "error",
            close: true,
            button: "Thử lại"
        });
        return false;
    }
}

function RegexEmail(emailFieldId) {
    var email = document.getElementById(emailFieldId).value;
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    var isValidEmail = emailPattern.test(email);

    if (!isValidEmail) {
        swal({
            title: "",
            text: "Bạn vui lòng nhập đúng định dạng email...",
            icon: "error",
            close: true,
            button: "Thử lại"
        });
        document.getElementById(emailFieldId).focus();
    } else {
        swal({
            title: "",
            text: "Chúng tôi vừa gửi cho bạn email hướng dẫn đặt lại mật khẩu...",
            icon: "success",
            close: true,
            button: "Đóng"
        });
        document.getElementById(emailFieldId).focus();
        window.location = "#";
    }
}