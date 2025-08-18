const timerEl = document.getElementById('timer');

let timeLeft = parseInt(timerEl.textContent);

const countdown = setInterval(() => {
    timeLeft--;
    timerEl.textContent = timeLeft;

    if (timeLeft <= 0) {
        clearInterval(countdown);
        alert("Вы победили в конкурсе!");
    }
}, 1000);
