let username = sessionStorage.getItem("username");
let chat_id = sessionStorage.getItem("chat_id");

function set_user_name() {
  const user_name = document.getElementById("name");
  user_name.textContent = username;
}
function send_message(e) {
  e.preventDefault();
  const msg_input = document.getElementById("msg_input");
  const msg_text = msg_input.value;
  msg_input.value = "";
  const date = new Date();
  const msg_bubble = `
  <div class="chat chat-end">
            <div class="chat-image avatar">
              <div class="w-10 rounded-full">
                <img
                  alt="Tailwind CSS chat bubble component"
                  src="https://img.daisyui.com/images/profile/demo/anakeen@192.webp"
                />
              </div>
            </div>
            <div class="chat-header">
              ${username}
              <time class="text-xs opacity-50">${date.getHours() % 12 || "12"}:${date.getMinutes()}</time>
            </div>
            <div class="chat-bubble">${msg_text}</div>
            
          </div>`;
  const chat_screen = document.getElementById("chat_screen");
  const new_msg = document.createElement("div");
  new_msg.innerHTML = msg_bubble;
  chat_screen.append(new_msg);
}
async function fetch_msgs() {
  const res = await fetch(`http://127.0.0.1:5000/messages/${chat_id}`, {
    credentials: "include",
  });
  const data = await res.json();
  const content = data.data;
  for (let i = 0; i < content.length; i++) {
    const time = content[i].created_at;
    const content_msg = content[i].content;
    const format = new Intl.DateTimeFormat([], {
      hour: "2-digit",
      minute: "2-digit",
      hour12: true,
    }).format(new Date(time));
    const msg_bubble = `
  <div class="chat chat-end">
            <div class="chat-image avatar">
              <div class="w-10 rounded-full">
                <img
                  alt="Tailwind CSS chat bubble component"
                  src="https://img.daisyui.com/images/profile/demo/anakeen@192.webp"
                />
              </div>
            </div>
            <div class="chat-header">
              vimal
              <time class="text-xs opacity-50">${format}</time>
            </div>
            <div class="chat-bubble">${content_msg}</div>
            
          </div>`;
    const chat_screen = document.getElementById("chat_screen");
    const new_msg = document.createElement("div");
    new_msg.innerHTML = msg_bubble;
    chat_screen.append(new_msg);
  }
}

fetch_msgs();
set_user_name();
