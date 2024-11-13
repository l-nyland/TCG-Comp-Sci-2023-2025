//document.addEventListener('DOMContentLoaded', () => {
    //console.log('Javascript is running'););

const menus = {
    Monday: ["Pasta & Meatballs - €5", "Salad - €3"],
    Tuesday: ["Chicken Curry & Rice - €6", "Naan Bread - €2"],
    Wednesday: ["Burger & Chips - €7", "Coleslaw - €2"],
    Thursday: ["Pizza - €6", "Garlic Bread - €3"],
    Friday: ["Fish & Chips - €9", "Peas - €2"]
};

const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const today = new Date().getDay();
const todayMenu = menus[days[today]];

document.getElementById('day').innerText = days[today];
const menuItems = document.getElementById('menu-items');
todayMenu.forEach(item => {
    const li = document.createElement('li');
    li.innerText = item;
    menuItems.appendChild(li);
});
