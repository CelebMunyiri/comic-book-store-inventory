// Import necessary modules
const express = require('express');
const mysql = require('mysql');
const fs = require('fs');
const path = require('path');

// Create an instance of the express application
const app = express();

// Set up a connection to the MySQL database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'book_viewer'
});

// Connect to the database
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to the database: ' + err.stack);
        return;
    }

    console.log('Connected to the database.');
});

// Set up the route to get the books
app.get('/books', (req, res) => {
    // Define the path to the books folder
    const booksPath = path.join(__dirname, 'books');

    // Read the files in the books folder
    fs.readdir(booksPath, (err, files) => {
        if (err) {
            console.error('Error reading books folder: ' + err);
            res.sendStatus(500);
            return;
        }

        // Filter out any non-PDF files
        const pdfFiles = files.filter(file => path.extname(file).toLowerCase() === '.pdf');

        // Map the PDF files to embed tags
        const embedTags = pdfFiles.map((file, index) => {
            const src = `/books/${file}`;
            const title = `Book ${index + 1}`;

            return `<div class="book">
                        <div class="book-title">${title}</div>
                        <embed class="book-embed" src="${src}" type="application/pdf" />
                    </div>`;
        });

        // Send the embed tags as the response
        res.send(embedTags.join(''));
    });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
