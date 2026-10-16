# Linkific Internship — Day 5: React Fundamentals

## Objective
Learn React fundamentals and build a responsive landing page using React and Vite.

## Topics Covered

### 1. React and Vite Setup
- Understand React as a JavaScript library for building user interfaces.
- Create a React project with Vite.
- Install dependencies and start the development server.
- Commands used:
  ```bash
  npm create vite@latest
  npm install
  npm run dev
  ```

### 2. React Project Structure
- `index.html` — HTML entry point.
- `src/main.jsx` — mounts the React application.
- `src/App.jsx` — main application component.
- `src/components/` — reusable UI components.
- `src/index.css` and `src/App.css` — global and application styles.
- `package.json` — project metadata, dependencies, and scripts.
- `vite.config.js` — Vite configuration.

### 3. JSX
- Write HTML-like markup inside JavaScript.
- Use `className` instead of `class`.
- Insert JavaScript expressions with `{}`.
- Return a single parent element or use a React Fragment.
- Close tags and use self-closing syntax where required.

### 4. Components
- Build reusable function components.
- Use PascalCase component names.
- Split the landing page into smaller parts:
  - `Navbar`
  - `Hero`
  - `Features`
  - `About`
  - `Footer`

### 5. Props
- Pass information from parent components to child components.
- Destructure props inside components.
- Keep props read-only.
- Use a reusable `FeatureCard` component to display feature data.

### 6. State and `useState`
- Understand state as data managed by a component.
- Use `useState` for interactive UI.
- Implement a mobile navigation menu that opens and closes.
- Update UI when state changes.

### 7. Hooks and `useEffect`
- Learn the purpose of React Hooks.
- Understand the basic `useEffect` dependency patterns.
- Review how effects can synchronize a component with external systems.
- Follow the Rules of Hooks: call Hooks at the top level of React function components or custom Hooks.

### 8. Landing Page Implementation
The project includes:
- Responsive navigation with a mobile menu.
- Hero section with call-to-action links.
- Feature cards rendered from an array using `map()`.
- About section with values.
- Footer with a dynamically generated current year.
- Responsive layouts for smaller screens.
- Reusable components and CSS styling.

## Python and DSA Practice

### Dictionary vs List
- A list stores an ordered sequence of values and is accessed by index.
- A dictionary stores key-value pairs and is accessed by key.
- Dictionaries are useful for fast average-case lookups by key.

### Missing Number
**Problem:** Given distinct numbers from `0` to `n` with one number missing, return the missing number.

```python
def missing_number(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

print(missing_number([3, 0, 1]))  # 2
```

- Time complexity: `O(n)`
- Extra space: `O(1)`

### Two Sum
**Problem:** Return the indices of two numbers whose sum equals the target.

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

- Average time complexity: `O(n)`
- Extra space: `O(n)`

## Run the React Project

Requirements: Node.js and npm installed.

1. Extract the project into a normal working folder. Do not place the project inside another repository's `.git` directory.
2. Open the project folder—the folder containing `package.json`—in VS Code.
3. Open a terminal in that folder.
4. Install dependencies:
   ```bash
   npm install
   ```
5. Start the development server:
   ```bash
   npm run dev
   ```
6. Open the Local URL printed by Vite.

To create a production build:
```bash
npm run build
```

## GitHub Checklist

- [ ] Confirm the project runs locally.
- [ ] Check the landing page on desktop and mobile widths.
- [ ] Test the mobile navigation menu.
- [ ] Confirm all navigation links work.
- [ ] Review the component structure and remove unused files.
- [ ] Run `npm run build` and fix any errors.
- [ ] Review changes using `git status`.
- [ ] Commit and push the Day 5 work to the intended repository.

Example Git commands (run from the correct Git repository):
```bash
git status
git add .
git commit -m "Complete Day 5 React fundamentals"
git push
```

Only run the Git commands after confirming that the terminal is inside the intended repository and that `git status` shows the expected files.

## Learning Outcomes
By completing these tasks, you practise:
- React project setup with Vite.
- JSX syntax and component composition.
- Passing props to reusable components.
- Managing UI state with `useState`.
- Understanding `useEffect` and Hook rules.
- Rendering lists from arrays.
- Responsive CSS and landing page structure.
- Python dictionaries and list comparison.
- Solving Missing Number and Two Sum problems.

## Day 5 Deliverables
- [ ] React + Vite project created.
- [ ] Landing page implemented using reusable components.
- [ ] Python practice for Dictionary vs List, Missing Number, and Two Sum completed.
- [ ] Project tested locally.
- [ ] README added and GitHub updated.
