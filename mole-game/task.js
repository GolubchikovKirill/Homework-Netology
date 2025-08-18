const deadEl = document.getElementById('dead');
const lostEl = document.getElementById('lost');

function getHole(index) {
  return document.getElementById(`hole${index}`);
}

function resetStats() {
  deadEl.textContent = '0';
  lostEl.textContent = '0';
}

function checkEnd() {
  const dead = parseInt(deadEl.textContent, 10);
  const lost = parseInt(lostEl.textContent, 10);

  if (dead >= 10) {
    alert('Победа! Вы уничтожили 10 кротов!');
    resetStats();
  } else if (lost >= 5) {
    alert('Игра окончена! Вы промахнулись 5 раз.');
    resetStats();
  }
}

// Вешаем обработчики на все 9 лунок
for (let i = 1; i <= 9; i++) {
  const hole = getHole(i);

  hole.addEventListener('click', () => {
    if (hole.classList.contains('hole_has-mole')) {
      deadEl.textContent = String(parseInt(deadEl.textContent, 10) + 1);
    } else {
      lostEl.textContent = String(parseInt(lostEl.textContent, 10) + 1);
    }

    checkEnd();
  });
}
