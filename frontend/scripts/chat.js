let username = "";

function set_user_name() {
  const url = new URL(window.location);
  const name = url.searchParams.get("name");
  username = name;
  const user_name = document.getElementById("name");
  user_name.textContent = name;
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

set_user_name();
