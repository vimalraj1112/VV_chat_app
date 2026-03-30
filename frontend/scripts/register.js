async function register_user(e) {
  e.preventDefault();
  const name = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const body = { name, email, password };

  const res = await fetch("http://127.0.0.1:5000/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!data.success) {
    alert(data.message || "failed");
    return;
  } else {
    alert(data.message || "Successfully");
    window.open("../html/user.html");
  }
}
