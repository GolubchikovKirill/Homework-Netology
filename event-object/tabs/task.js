const tabsContainers = document.querySelectorAll('.tabs');

tabsContainers.forEach(tabsBlock => {
  const tabs = tabsBlock.querySelectorAll('.tab');
  const contents = tabsBlock.querySelectorAll('.tab__content');

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
      tabs.forEach(tab => tab.classList.remove('tab_active'));
      contents.forEach(content => content.classList.remove('tab__content_active'));
      tab.classList.add('tab_active');
      contents[index].classList.add('tab__content_active');
    });
  });
});
