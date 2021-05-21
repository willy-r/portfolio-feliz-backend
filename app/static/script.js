// Global variables.
var timeout;

// Flash messages elements.
const divMessages = document.querySelector('.flash-messages');
const closeButton = document.querySelector('.close-button');

// Form elements.
const form = document.querySelector('.main-form');
const emailInput = document.querySelector('#email');
const helpMessage = document.querySelector('.help');

// Add the message element, and show the message.
function showFlashMessage(message, category) {
  const messageElement = `<p class="message-category  -${category}">${message}</p>`;

  divMessages.insertAdjacentHTML('afterbegin', messageElement);
  divMessages.style.display = 'flex';
}

// Remove the message element, and close the flash message.
function closeFlashMessage() {
  divMessages.removeChild(divMessages.firstChild);
  divMessages.style.display = 'none';
}

form.addEventListener('submit', event => {
  // Prevent default, don't refresh the page.
  event.preventDefault();
  
  const data = new FormData(form);

  fetch(`${location.origin}/send-email`, { method: 'POST', body: data })
  .then(response => response.json())
  .then(json => {
    const message = json.message;
    const messageCategory = json.sent ? 'success' : 'error';

    // Show the message.
    showFlashMessage(message, messageCategory);

    // Reset the form to default (blank form).
    form.reset();

    // Set timout to close the message automatically after 10 sec.
    timeout = setTimeout(closeFlashMessage, 10000);
  })
  .catch(err => console.error(err));
});

closeButton.addEventListener('click', () => {
  closeFlashMessage();
  clearTimeout(timeout);
});

emailInput.addEventListener('focusin', () => {
  helpMessage.style.visibility = 'visible';
});

emailInput.addEventListener('focusout', () => {
  helpMessage.style.visibility = 'hidden';
});
