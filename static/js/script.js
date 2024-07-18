const yourname = localStorage.getItem('yourname')

document.addEventListener('DOMContentLoaded', function() {
    var socket = io();

    var chatBox = document.getElementById('chatBox');
    var messageForm = document.getElementById('messageForm');
    var messageInput = document.getElementById('messageInput');

    // Evento para enviar mensagem ao pressionar o botão Enviar
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        var message = messageInput.value.trim();
        if (message !== '') {
            socket.emit('message', message);
            messageInput.value = '';
            console.log(message)
        }
    });

    // Evento para exibir mensagens recebidas no chat
    socket.on('message', function(message) {
        var messageElement = document.createElement('div');
        if (yourname == message.username) {
            messageElement.classList.add('your-message');
        }
        else {
            messageElement.classList.add('message');
        }
        
        messageElement.textContent = `${message.username}: ${message.message}`;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Rolagem automática para a última mensagem
    });
});