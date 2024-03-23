const listItems = document.querySelectorAll('ul li form');
const form = document.querySelector("form");
listItems.forEach(item => {
  item.addEventListener('click', () => {
    form.submit();
  });
});



