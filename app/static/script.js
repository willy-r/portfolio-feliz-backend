var timeout;
const divMessages = document.querySelector('.flash-messages');
const helpMessage = document.querySelector('.help');
const emailInput = document.querySelector('#email');

function closeMessages() {
  divMessages.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
  if (divMessages) {
    timeout = setTimeout(closeMessages, 5000);
  }
});

document.addEventListener('click', (event) => {
  const element = event.target;

  if (element.className === 'close-button') {
    closeMessages();
    clearTimeout(timeout);
  }
});

emailInput.addEventListener('focusin', () => {
    helpMessage.style.visibility = 'visible';
});

emailInput.addEventListener('focusout', () => {
  helpMessage.style.visibility = 'hidden';
});
