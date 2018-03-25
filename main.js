// AWS GATEWAY:
// var aws = "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api";
var rip = "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/addstocks/user/adam";

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
    var json = [{"stocks": [{"symbol": "BRK.B", "price": 205, "quantity": 5},
                      {"symbol": "SNAP", "price": 1, "quantity": 150}]}
   ];
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
        }
    };
    // xhttp.open("POST", aws + "/addvalue/crypto/user/adam", true);
    xhttp.open("POST", rip, true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8",);
    xhttp.send(JSON.stringify(json));
    return false;
}

function displayStocks() {
    // alert("Display Stocks in List.");
    // Make 'GET' call to API

    var totalRows = 5;
    var cellsInRow = 4;
    var min = 1;
    var max = 10;

        // function drawTable() {
            // get the reference for the body
            var div1 = document.getElementById('div1');

            // creates a <table> element
            var tbl = document.createElement("table");

            // creating rows
            for (var r = 0; r < totalRows; r++) {
                var row = document.createElement("tr");

    	     // create cells in row
                 for (var c = 0; c < cellsInRow; c++) {
                    var cell = document.createElement("td");
                    var cellText = document.createTextNode("hi");
                    cell.appendChild(cellText);
                    row.appendChild(cell);
                }

    	           tbl.appendChild(row); // add the row to the end of the table body
            }

         div1.appendChild(tbl); // appends <table> into <div1>
    // }
    // window.onload=drawTable;

    // return true;
}

function displayCryptos() {
    alert("Display Cryptos in List.");
    return true;
}
