// Global variables.
var timeout;

// Flash messages elements.
const divMessages = document.querySelector('.flash-messages');
const closeButton = document.querySelector('.close-button');

// Form elements.
const form = document.querySelector('.main-form');
const emailInput = document.querySelector('#email');
const helpMessage = document.querySelector('.help');
const sendButton = document.querySelector('.main-button');

// Add and show the flash message.
function showFlashMessage(message, emailWasSent) {
  const variant = emailWasSent ? '-success' : '-error';
  const messageElement = `<p class="message-category  ${variant}">${message}</p>`;

  divMessages.insertAdjacentHTML('afterbegin', messageElement);
  divMessages.style.display = 'flex';
}

// Remove and close the flash message.
function closeFlashMessage() {
  divMessages.removeChild(divMessages.firstChild);
  divMessages.style.display = 'none';
}

// Add and show the spinner.
function showSpinner() {
  const spinner = '<span class="fas fa-spinner fa-spin"></span>';

  sendButton.textContent = '';
  sendButton.disabled = true;
  sendButton.insertAdjacentHTML('afterbegin', spinner);
}

// Remove and hide the spinner.
function hideSpinner() {
  sendButton.removeChild(sendButton.firstChild);
  sendButton.textContent = 'Enviar';
  sendButton.disabled = false;
}

form.addEventListener('submit', event => {
  // Prevent default, don't refresh the page.
  event.preventDefault();

  showSpinner();
  
  const data = new FormData(form);

  fetch(`${location.origin}/send-email`, { method: 'POST', body: data })
  .then(response => response.ok ? response.json() : Promise.reject(response))
  .then(json => {
    // Reset the form to default (blank form).
    form.reset();

    showFlashMessage(json.message, json.sent);
    hideSpinner();

    // Set timout to close the message automatically after 10 sec.
    timeout = setTimeout(closeFlashMessage, 10000);
  })
  .catch(err => {
    hideSpinner();
    console.error(`${err.status}: ${err.statusText}`);
  });
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
