// Cookies are just names for demonstration purposes

// Sets a new cookie for a new user
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

// retrieves cookie
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

// Checks if cookie exists and if so uses it
function checkCookie() {
  let user = getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) {
      setCookie("username", user, 30);
    }
  }
}

// Checks what user is recognized as the one that made the request
function whoami() {
  let user = getCookie("username");
  console.log(user);
  return user;
}

function printWhoAmI() {
  let name = whoami();
  document.getElementById("name").innerHTML =
    "Hello Mr. " + name.charAt(0).toUpperCase() + name.slice(1);
}

function getParams(){
  let params = {};
      location.search
        .slice(1)
        .split("&")
        .forEach(function (pair) {
          pair = pair.split("=");
          params[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
        });

  return params;
}

// Todd is our supposed admin
function ChangePriceAPI(params) {
  if ("price" in params && "value" in params && whoami() == "Todd") {
    console.log(params["value"]);
    document.getElementById(params["value"]).innerHTML = params["price"];
  }
}
