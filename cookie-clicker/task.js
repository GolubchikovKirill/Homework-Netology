const cookie = document.getElementById('cookie');
const counterEl = document.getElementById('clicker__counter');

let counter = parseInt(counterEl.textContent, 10) || 0;
let isShrunk = false;

const baseWidth = 200;
const baseHeight = 200;
const shrinkFactor = 0.9;

cookie.addEventListener('click', () => {
  counter += 1;
  counterEl.textContent = counter;

  isShrunk = !isShrunk;
  if (isShrunk) {
    cookie.width = Math.round(baseWidth * shrinkFactor);
    cookie.height = Math.round(baseHeight * shrinkFactor);
  } else {
    cookie.width = baseWidth;
    cookie.height = baseHeight;
  }
});
