document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("surprise-btn");
    const surprise = document.getElementById("surprise");

    if (button && surprise) {
        button.addEventListener("click", () => {
            surprise.style.display = "block";
            button.style.display = "none"; // hide button after opening
        });
    }
});
document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("surprise-btn");
  const surprise = document.getElementById("surprise");

  if (button && surprise) {
    button.addEventListener("click", () => {
      surprise.style.display = "block";
      button.style.display = "none";

      // Start floating hearts after surprise is shown
      startFloatingHearts();
    });
  }
});

function startFloatingHearts() {
  setInterval(() => {
    const heart = document.createElement("div");
    heart.classList.add("heart");
    heart.innerHTML = "💖";

    // Random horizontal position
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.fontSize = Math.random() * 20 + 20 + "px";

    document.body.appendChild(heart);

    // Remove after animation
    setTimeout(() => {
      heart.remove();
    }, 5000);
  }, 500);
}
