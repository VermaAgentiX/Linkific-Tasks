'use strict';

// A small helper keeps element selection readable.
const getElement = (id) => document.getElementById(id);

// 1. DOM manipulation: update existing content.
getElement('change').addEventListener('click', () => {
    getElement('msg').textContent = 'Nice work! JavaScript has updated this message.';
});

// 2. DOM manipulation: create a new element and add it to the page.
let noteCount = 0;

getElement('add').addEventListener('click', () => {
    noteCount += 1;

    const note = document.createElement('li');
    note.textContent = `Practice note ${noteCount}: keep learning by building.`;
    getElement('notes').appendChild(note);
});

// 3. Event handling: read a value from an input and respond to the user.
getElement('greet').addEventListener('click', () => {
    const name = getElement('name').value.trim();
    const greeting = name
        ? `Hello, ${name}! Welcome to your JavaScript practice page.`
        : 'Please enter your name first.';

    getElement('greeting').textContent = greeting;
});

// 4. Factorial: n! = n × (n - 1) × ... × 1, and 0! = 1.
function factorial(number) {
    if (!Number.isInteger(number) || number < 0 || number > 170) {
        throw new Error('Please enter a whole number from 0 to 170.');
    }

    let result = 1;

    for (let current = 2; current <= number; current += 1) {
        result *= current;
    }

    return result;
}

getElement('factBtn').addEventListener('click', () => {
    const number = Number(getElement('factN').value);

    try {
        getElement('factOut').textContent = `${number}! = ${factorial(number)}`;
    } catch (error) {
        getElement('factOut').textContent = error.message;
    }
});

// 5. Fibonacci: each term is the sum of the two previous terms.
function fibonacci(termCount) {
    if (!Number.isInteger(termCount) || termCount < 1 || termCount > 40) {
        throw new Error('Please enter between 1 and 40 terms.');
    }

    const sequence = [];
    let first = 0;
    let second = 1;

    for (let index = 0; index < termCount; index += 1) {
        sequence.push(first);
        [first, second] = [second, first + second];
    }

    return sequence;
}

getElement('fibBtn').addEventListener('click', () => {
    const termCount = Number(getElement('fibN').value);

    try {
        getElement('fibOut').textContent = fibonacci(termCount).join(', ');
    } catch (error) {
        getElement('fibOut').textContent = error.message;
    }
});

// 6. Find each duplicate value once using Set.
function findDuplicates(values) {
    const seen = new Set();
    const duplicates = new Set();

    for (const value of values) {
        if (seen.has(value)) {
            duplicates.add(value);
        } else {
            seen.add(value);
        }
    }

    return [...duplicates];
}

getElement('dupBtn').addEventListener('click', () => {
    const values = [1, 2, 3, 2, 4, 5, 1];
    const duplicates = findDuplicates(values);

    getElement('dupOut').textContent = duplicates.length
        ? `Duplicate values: ${duplicates.join(', ')}`
        : 'No duplicates found.';
});

// 7. Variable example: let can be reassigned; const object properties can change.
getElement('varBtn').addEventListener('click', () => {
    let score = 10;
    score = 15;

    const learner = { name: 'Learner' };
    learner.name = 'JavaScript learner';

    console.log('Updated let variable:', score);
    console.log('Updated property on const object:', learner);

    getElement('varOut').textContent =
        'Examples logged. Open your browser developer tools and select Console to view them.';
});

// 8. Responsive navigation menu.
getElement('menuBtn').addEventListener('click', () => {
    const menu = getElement('nav');
    const isOpen = menu.classList.toggle('open');

    getElement('menuBtn').setAttribute('aria-expanded', String(isOpen));
});

// 9. Render the checklist from an array of objects.
const tasks = [
    { title: 'Revise variables, data types, and operators', done: false },
    { title: 'Practice loops, functions, arrays, and objects', done: false },
    { title: 'Try DOM manipulation and event handling', done: false },
    { title: 'Run factorial, Fibonacci, and duplicate-finding programs', done: false },
    { title: 'Update the project documentation and GitHub repository', done: false }
];

function renderTasks() {
    const taskList = getElement('taskList');
    taskList.replaceChildren();

    tasks.forEach((task, index) => {
        const item = document.createElement('li');
        item.textContent = `${task.done ? '✓' : '○'} ${task.title}`;
        item.classList.toggle('done', task.done);
        item.setAttribute('role', 'checkbox');
        item.setAttribute('aria-checked', String(task.done));
        item.setAttribute('tabindex', '0');

        const toggleTask = () => {
            tasks[index].done = !tasks[index].done;
            renderTasks();
        };

        item.addEventListener('click', toggleTask);
        item.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                toggleTask();
            }
        });

        taskList.appendChild(item);
    });

    const completedCount = tasks.filter((task) => task.done).length;
    getElement('progress').textContent =
        `${completedCount} of ${tasks.length} tasks completed.`;
}

// Set the current year and render the initial checklist.
renderTasks();
getElement('year').textContent = new Date().getFullYear();
