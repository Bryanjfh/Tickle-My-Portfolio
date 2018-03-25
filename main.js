// AWS GATEWAY:
// var aws = "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api";
var rip = "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/addstocks/user/adam";
var rip2 ="https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/portfolio/user/adam";

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
         var getstock = this.responseText;
         getstock = JSON.parse;
        }
    };
    // xhttp.open("POST", aws + "/addvalue/crypto/user/adam", true);
    xhttp.open("GET", rip2, true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8",);
    xhttp.send(null);
    return false;
}

function displayStocks() {
    // alert("Display Stocks in List.");
    // Make 'GET' call to API
    var i, x, j, z, w, e = "";
    var xhttp = new XMLHttpRequest();

   xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
       var str = this.responseText;
       var obj = JSON.parse(str);
       var stuck = new Array();
       stuck.push(["Name", "Quantity", "Price Paid"]);

       for (i = 0; i<obj.stocks.length;i++) {
         x = "<h2>" + obj.stocks[i].symbol + "</h2>";
         for (j = 0; j<obj.stocks.length;j++) {
           w = "<h2>" + obj.stocks[j].paid + "</h2>";
           for (z = 0; z<obj.stocks.length;z++) {
             e = "<h2>" + obj.stocks[z].quantity + "</h2>";
             stuck.push([x, w, e]);
           }
         }
       }

       //Create a HTML Table element.
       var table = document.createElement("TABLE");
       table.border = "1";

       //Get the count of columns.
       var columnCount = stuck[0].length;

       //Add the header row.
       var row = table.insertRow(-1);
       for (var i = 0; i < columnCount; i++) {
           var headerCell = document.createElement("TH");
           headerCell.innerHTML = stuck[0][i];
           row.appendChild(headerCell);
       }

       //Add the data rows.
       for (var i = 1; i < stuck.length; i++) {
           row = table.insertRow(-1);
           for (var j = 0; j < columnCount; j++) {
               var cell = row.insertCell(-1);
               cell.innerHTML = stuck[i][j];
           }
       }

       var dvTable = document.getElementById("dvTable");
       dvTable.innerHTML = "";
       dvTable.appendChild(table);

     }
   };
   xhttp.open("GET", rip2, true);
   xhttp.send();
}

function displayCryptos() {
    alert("Display Cryptos in List.");
    return true;
}
