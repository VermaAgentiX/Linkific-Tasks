'use strict';
const $ = id => document.getElementById(id);

// DOM manipulation: select an element and change its text.
$('change').addEventListener('click', () => {$('msg').textContent='JavaScript changed this HTML element!';});
let notes=0;
$('add').addEventListener('click',()=>{const li=document.createElement('li');li.textContent=`Dynamically created note ${++notes}`;$('notes').appendChild(li);});

// Event handling: read input and update the DOM.
$('greet').addEventListener('click',()=>{const name=$('name').value.trim();$('greeting').textContent=name?`Hello, ${name}!`:'Please enter your name.';});

// Factorial: 0! is 1. Restrict input to 0..170 for JavaScript Number precision/range.
function factorial(n){if(!Number.isInteger(n)||n<0||n>170)throw Error('Enter an integer from 0 to 170.');let ans=1;for(let i=2;i<=n;i++)ans*=i;return ans;}
$('factBtn').addEventListener('click',()=>{try{$('factOut').textContent=`${$('factN').value}! = ${factorial(Number($('factN').value))}`;}catch(e){$('factOut').textContent=e.message;}});

// Fibonacci: each number is the sum of the previous two.
function fibonacci(n){if(!Number.isInteger(n)||n<1||n>40)throw Error('Enter 1 to 40 terms.');const out=[];let a=0,b=1;for(let i=0;i<n;i++){out.push(a);[a,b]=[b,a+b];}return out;}
$('fibBtn').addEventListener('click',()=>{try{$('fibOut').textContent=fibonacci(Number($('fibN').value)).join(', ');}catch(e){$('fibOut').textContent=e.message;}});

// Unique duplicate values using Set.
function findDuplicates(arr){const seen=new Set(),dups=new Set();for(const x of arr){if(seen.has(x))dups.add(x);else seen.add(x);}return [...dups];}
$('dupBtn').addEventListener('click',()=>{$('dupOut').textContent=findDuplicates([1,2,3,2,4,5,1]).join(', ');});

// var vs let vs const example. Open browser DevTools > Console.
$('varBtn').addEventListener('click',()=>{let score=10;score=15;const user={name:'Learner'};user.name='JS learner';console.log({score,user});$('varOut').textContent='Logged examples to the browser console.';});

// Responsive mobile menu.
$('menuBtn').addEventListener('click',()=> $('nav').classList.toggle('open'));

// Arrays + objects + DOM: render a clickable task list.
const tasks=[
 {title:'Revise variables, data types and operators',done:false},
 {title:'Practice loops, functions, arrays and objects',done:false},
 {title:'Demonstrate DOM manipulation and events',done:false},
 {title:'Write factorial, Fibonacci and duplicate programs',done:false},
 {title:'Update GitHub repository',done:false}
];
function renderTasks(){const ul=$('taskList');ul.replaceChildren();tasks.forEach((task,i)=>{const li=document.createElement('li');li.textContent=(task.done?'✓ ':'○ ')+task.title;li.classList.toggle('done',task.done);li.addEventListener('click',()=>{tasks[i].done=!tasks[i].done;renderTasks();});ul.appendChild(li);});$('progress').textContent=`${tasks.filter(t=>t.done).length}/${tasks.length} tasks completed.`;}
renderTasks();$('year').textContent=new Date().getFullYear();
