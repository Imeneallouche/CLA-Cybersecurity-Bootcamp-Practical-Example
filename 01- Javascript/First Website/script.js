// document.getElementById(id):

// document.getElementsByClassName(className):

// document.getElementsByTagName("img"):

function turnOnLight() {
  let objects = Array.from(document.getElementsByClassName("light_state"));

  objects.forEach((elemnt) => {
    elemnt.innerHTML = "on";
  });
  document.getElementById("myImage").src = "light_on.png";
}

function turnOffLight() {
  document.getElementById("myImage").src = "light_off.png";

  let objects = Array.from(document.getElementsByClassName("light_state"));

  objects.forEach((elemnt) => {
    elemnt.innerHTML = "off";
  });
}
