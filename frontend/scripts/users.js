async function get_users() {
  const res = await fetch("http://127.0.0.1:5000/users/", {
    credentials: "include",
  });
  const data = await res.json();
  if (!data.success) {
    alert(data.message || "failed");
    return;
  }
  const users = data.data;
  render_users(users);
}

function render_users(users) {
  const userlist = document.getElementById("user-list");

  for (let i = 0; i < users.length; i++) {
    const username = users[i].username;
    const email = users[i].email;
    const listuser = `
    <a href="./chat.html?name=${username}" class="list-row">
              <div>
                <img class="size-10 rounded-box" src="../images/images.jpg" />
              </div>
              <div>
                <div>${username}</div>
                <div class="text-xs uppercase font-semibold opacity-60">
                  ${email}
                </div>
              </div>

              <button class="btn btn-square btn-ghost">
                <i data-lucide="message-square-more" class="w-4"></i>
              </button>
            </a>`;
    const li = document.createElement("li");
    li.innerHTML = listuser;
    userlist.appendChild(li);
  }
}
get_users();
