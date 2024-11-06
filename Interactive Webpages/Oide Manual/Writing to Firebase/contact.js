//alert("welcome to the Contact Us page");

// TASK 4B – Copy your web app's Firebase configuration here ...
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCJ33RvZHLS8mBL_d9Ae5XFbth5W-Dfu_o",
  authDomain: "compscidatabase1.firebaseapp.com",
  databaseURL: "https://compscidatabase1-default-rtdb.firebaseio.com",
  projectId: "compscidatabase1",
  storageBucket: "compscidatabase1.firebasestorage.app",
  messagingSenderId: "841980546961",
  appId: "1:841980546961:web:a4774ec5dfe24c0e971430",
  measurementId: "G-4SL2FLZ8LK"
};

// TASK 4C
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Retrieve the database handle
const myDBCxn = firebase.database().ref('/contacts');


// Task 2D - tell JavaScript to call saveContacts when SUBMIT button is clicked
const btn = document.getElementById("submit-data");
btn.addEventListener("click", saveContacts);

// Submit clicked so post the data to the server
function saveContacts() {
 // alert("SUBMIT clicked!!!");
  // Task 2E - read the data from the email field
  const emailField = document.getElementById("email");
  const emailFieldValue = emailField.value;
  alert(emailFieldValue);

  //reset form
  emailField.value = ''; //clear the field
  emailField.focus(); //set the focus
 // <-- GOTCHA!

//code to save data to firebase
const data = myDBCxn.push();
data.set( {email: emailFieldValue
          });

}
// Task 5B - Code to retrieve and display the data goes here ...



// Task 5C - Code to retrieve and display the data in a list goes here ...
