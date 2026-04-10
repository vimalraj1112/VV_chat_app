async function get_chats() {
  try {
    const res = await fetch("http://127.0.0.1:5000/messages", {
      credentials: "include",
    });
    if (res.status == 401) {
      location.href = "../index.html";
    }
    if (!res.ok) {
      alert("failed to fetch");
      return;
    }
    const data = await res.json();
    const chats = data.data;

    const chat_list = document.getElementById("chat_list");
    for (let i = 0; i < chats.length; i++) {
      const name = chats[i].username;
      const last_msg = chats[i].last_message;
      const last_msg_at = chats[i].last_message_at;
      const chat_id = chats[i].chat_id;
      const user_id = chats[i].user_id;
      const format_time = new Intl.DateTimeFormat([], {
        hour: "2-digit",
        minute: "2-digit",
        hour12: true,
      }).format(new Date(last_msg_at));

      const listuser = `
    <a href="./chat.html?" class="list-row">
              <div>
                <img class="size-10 rounded-box" src="../images/images.jpg" />
              </div>
              <div>
                <div>${name}</div>
                <div class="text-xs uppercase font-semibold opacity-60">
                  ${last_msg}
                </div>
              </div>
              <p class="text-xs">${format_time}</p>

              <button class="btn btn-square btn-ghost">
                <i data-lucide="message-square-more" class="w-4"></i>
              </button>
            </a>`;
      const li = document.createElement("li");
      li.onclick = function (e) {
        sessionStorage.setItem("username", name);
        sessionStorage.setItem("chat_id", chat_id);
        sessionStorage.setItem("user_id", user_id);
      };
      li.innerHTML = listuser;
      chat_list.appendChild(li);
    }
  } catch (error) {
    console.error(error);
    alert("failed to fetch chat");
  }
}
async function logout() {
  const res = await fetch("http://127.0.0.1:5000/auth/logout", {
    credentials: "include",
    method: "POST",
  });
  if (!res.ok) {
    alert("failed");
    return;
  }
  location.href = "../index.html";
}
get_chats();
