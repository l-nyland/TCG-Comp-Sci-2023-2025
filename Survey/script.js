// script.js
document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Collect data
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const email = document.getElementById('email').value;

    console.log('Name:', name);
    console.log('Age:', age);
    console.log('Email:', email);
    
    // Validate data
    if (!name || !age || !email ) {
        alert('All fields are required!');
        return;
    }
    
    // Store data in local storage
    const userData = { name, age, email };
    let users = JSON.parse(localStorage.getItem('users')) || [];
    users.push(userData);
    localStorage.setItem('users', JSON.stringify(users));
    
    // Display summary
    displaySummary();
});

function displaySummary() {
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const summaryDiv = document.getElementById('summary');
    summaryDiv.innerHTML = '<h2>Summary of Collected Data</h2>';
    
    users.forEach(user => {
        summaryDiv.innerHTML += `<p>Name: ${user.name}, Age: ${user.age}, Email: ${user.email}</p>`;
    });
}

// Display summary on page load
displaySummary();
