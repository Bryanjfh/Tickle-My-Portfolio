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
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

      var str = this.responseText;
      // var res = str.substring(1, str.length - 1);

      var obj = JSON.parse(str);

      // var final = obj.cryptos[0].symbol + " purchased at:" + obj.cryptos[0].paid + " quantity: " + obj.cryptos[0].quantity + "\n";
      var stocks_obj = obj.stocks;

      var final = "";
      for (var i = 0; i < stocks_obj.length; i++) {
        final += stocks_obj[i].symbol + "<br><br>" + " purchased at:" + stocks_obj[i].paid + "<br><br>" + " quantity: " + stocks_obj[i].quantity + "<br><br>"+ " \n";
        // console.log(stocks_obj[i].symbol);
      }
      // for(var crypto in cryptos_obj) {
      //   console.log(crypto.symbol);
      // }

      // document.getElementById("stocktable").innerHTML = "Cryptocurrency Portfolio Value: " + obj.value;

      document.getElementById("stocktable").innerHTML = final;


    }
  };
  xhttp.open("GET", "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/portfolio/user/adam", true);
  xhttp.send();

  var x = document.getElementById("stocktable");
  if (x.style.display === "none") {
      x.style.display = "block";
  } else {
      x.style.display = "none";
  }
  return true;
}

function displayCryptos() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

        var str = this.responseText;
        // var res = str.substring(1, str.length - 1);

        var obj = JSON.parse(str);

        // var final = obj.cryptos[0].symbol + " purchased at:" + obj.cryptos[0].paid + " quantity: " + obj.cryptos[0].quantity + "\n";
        var cryptos_obj = obj.cryptos;

        var final = "";
        for (var i = 0; i < cryptos_obj.length; i++) {
          final += cryptos_obj[i].symbol + "<br><br>" + " purchased at:" + cryptos_obj[i].paid + "<br><br>" + " quantity: " + cryptos_obj[i].quantity + "<br><br>"+ " \n";
          // console.log(cryptos_obj[i].symbol);
        }
        // for(var crypto in cryptos_obj) {
        //   console.log(crypto.symbol);
        // }

        // document.getElementById("stocktable").innerHTML = "Cryptocurrency Portfolio Value: " + obj.value;

        document.getElementById("stocktable").innerHTML = final;


      }
    };
    xhttp.open("GET", "https://2ji8y26hd8.execute-api.us-east-1.amazonaws.com/api/value/crypto/user/adam", true);
    xhttp.send();

    var x = document.getElementById("stocktable");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
    return true;
}
