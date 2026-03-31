function set_user_name() {
  const url = new URL(window.location);
  const name = url.searchParams.get("name");

  const user_name = document.getElementById("name");
  user_name.textContent = name;
}

set_user_name();
