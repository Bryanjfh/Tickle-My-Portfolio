// AWS GATEWAY:
var aws = "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api";

function fakeLogin() {
    document.location.href = "home.html";
    return true;
}

function addClick() {
    var symbol = document.getElementById("stockName").value;
    var shares = document.getElementById("stockShares").value;
    var price = document.getElementById("stockPrice").value;
    // Make  'POST' call to API
    var xhttp = new XMLHttpRequest();
    var json = {};
    json.symbol = symbol;
    json.shares = shares;
    json.price = price;
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
        }
    };
    xhttp.open("POST", aws + "/addvalue/crypto/user/adam", true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8", "Access-Control-Allow-Origin");
    xhttp.send(JSON.stringify(json));
    return false;
}

function displayStocks() {
    alert("Display Stocks in List.");
    // Make 'GET' call to API
    return true;
}

function displayCryptos() {
    alert("Display Cryptos in List.");
    return true;
}

function displayAll() {
    alert("Display all holdings in List.");
    return true;
}