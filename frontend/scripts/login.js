async function login_user(e) {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const body = { email, password };

  const res = await fetch("http://127.0.0.1:5000/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
    body: JSON.stringify(body),
  });
  const data = await res.json();
  if (!data.success) {
    alert(data.message || "failed");
  } else {
    alert(data.message || "Successfully Login");
    window.open("../html/user.html");
  }
}
