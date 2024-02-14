// commands.js

// Function to print a message on the website
function printMessage(message) {
    // Create a new paragraph element
    var paragraph = document.createElement('p');
    // Set the text content of the paragraph to the provided message
    paragraph.textContent = message;
    // Append the paragraph to the body of the document
    document.body.appendChild(paragraph);
}
