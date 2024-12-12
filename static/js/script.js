document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('messageInput');
    const checkButton = document.getElementById('checkButton');
    const resultDiv = document.getElementById('result');

    checkButton.addEventListener('click', async () => {
        const message = messageInput.value.trim();
        
        if (!message) {
            resultDiv.textContent = 'Please enter a message';
            resultDiv.className = 'result';
            return;
        }

        try {
            const response = await fetch('/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            
            resultDiv.textContent = `Result: ${data.result.toUpperCase()}`;
            resultDiv.className = `result ${data.result.toLowerCase()}`;
        } catch (error) {
            resultDiv.textContent = 'Error occurred while checking the message';
            resultDiv.className = 'result';
        }
    });
});
