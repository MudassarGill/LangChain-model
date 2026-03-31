document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const messageInput = document.getElementById('message-input');
    const sendBtn = document.getElementById('send-btn');
    const clearBtn = document.getElementById('clear-chat');

    // Auto-resize textarea
    messageInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        if(this.value === '') {
            this.style.height = 'auto'; // Reset when empty
        }
    });

    // Send message on Enter (but allow Shift+Enter for new lines)
    messageInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    sendBtn.addEventListener('click', sendMessage);

    clearBtn.addEventListener('click', async () => {
        // Keep only the first bot message
        const firstMessage = chatBox.firstElementChild;
        chatBox.innerHTML = '';
        if(firstMessage) chatBox.appendChild(firstMessage);
        
        // Notify backend to clear memory
        try {
            await fetch('/clear', { method: 'POST' });
        } catch(e) {
            console.error('Failed to clear backend memory:', e);
        }
    });

    async function sendMessage() {
        const text = messageInput.value.trim();
        if (!text) return;

        // 1. Add User Message
        appendMessage(text, 'user');
        
        // Reset Input
        messageInput.value = '';
        messageInput.style.height = 'auto';

        // 2. Add Typing Indicator
        const typingId = showTypingIndicator();

        // 3. Fetch from API
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            
            // Remove typing indicator
            removeTypingIndicator(typingId);
            
            // 4. Add Bot Message
            appendMessage(data.response || 'No response received.', 'bot');

        } catch (error) {
            console.error('Error:', error);
            removeTypingIndicator(typingId);
            appendMessage('Connection error. Is the local server running?', 'bot');
        }
    }

    function appendMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}-message`;
        
        const avatarHtml = sender === 'user' 
            ? '<i class="fa-solid fa-user"></i>' 
            : '<i class="fa-solid fa-microchip"></i>';
            
        const bubbleClass = sender === 'bot' ? 'msg-bubble glass-panel' : 'msg-bubble';

        // Format code snippets loosely if any
        let formattedText = text.replace(/\n/g, '<br>');

        msgDiv.innerHTML = `
            <div class="msg-avatar">${avatarHtml}</div>
            <div class="${bubbleClass}">
                <p>${formattedText}</p>
            </div>
        `;

        chatBox.appendChild(msgDiv);
        scrollToBottom();
    }

    function showTypingIndicator() {
        const id = 'typing-' + Date.now();
        const msgDiv = document.createElement('div');
        msgDiv.className = 'message bot-message';
        msgDiv.id = id;
        
        msgDiv.innerHTML = `
            <div class="msg-avatar"><i class="fa-solid fa-microchip"></i></div>
            <div class="msg-bubble glass-panel">
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;

        chatBox.appendChild(msgDiv);
        scrollToBottom();
        return id;
    }

    function removeTypingIndicator(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }

    function scrollToBottom() {
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
