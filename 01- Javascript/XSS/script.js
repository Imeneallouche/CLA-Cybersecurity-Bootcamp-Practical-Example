document.cookie = "username=imene.allouche@codelabsacademy.com";
document.cookie = "password=super_safe_password";

if (document.readyState == "loading") {
  document.addEventListener("DOMContentLoaded", ready);
} else {
  ready();
}

function ready() {
  var query = new URL(window.location).searchParams.get("query");
  document.getElementById("query-input").value = query;
  document.getElementById("query-output").innerText = query;
}
