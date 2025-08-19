const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(dropdown => {
  const value = dropdown.querySelector('.dropdown__value');
  const list = dropdown.querySelector('.dropdown__list');
  const links = dropdown.querySelectorAll('.dropdown__link');

  value.addEventListener('click', () => {
    list.classList.toggle('dropdown__list_active');
  });

  links.forEach(link => {
    link.addEventListener('click', (event) => {
      event.preventDefault(); // блокируем переход по ссылке

      value.textContent = link.textContent.trim(); // обновляем значение
      list.classList.remove('dropdown__list_active'); // закрываем список
    });
  });
});
