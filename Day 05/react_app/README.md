# React Basics Lab — Revision App

A small interactive React app for revising the fundamentals: JSX, components, props, state, event handling, list rendering, and conditional rendering.

## Requirements
- Node.js LTS and npm

## Run on Windows
1. Extract the ZIP into a normal folder outside any `.git` directory.
2. Open the extracted `React_Basics_Revision_App` folder itself in VS Code.
3. Open **Terminal → New Terminal**. Ensure the terminal path is the folder containing `package.json`.
4. Run:

```powershell
npm install
npm run dev
```

5. Open `http://127.0.0.1:5176/` in your browser.

This app uses port **5176** to avoid the common Vite port `5173`. If port 5176 is already in use, stop the other process or change `server.port` in `vite.config.js` and the `dev` script in `package.json` to the same port.

## Production build
```powershell
npm run build
npm run preview
```

## What to practise
- **JSX:** inspect the markup in `src/App.jsx`.
- **Components:** see `Header`, `TopicCard`, and `PracticePanel`.
- **Props:** `TopicCard` receives a topic object and completion status.
- **State:** `useState` manages completed topics, counter, and text input.
- **Events:** click buttons and type into the input.
- **List rendering:** topic cards use `.map()` with stable keys.
- **Conditional rendering:** completion badges and the preview update based on state.

## Folder structure
```text
React_Basics_Revision_App/
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── TopicCard.jsx
│   │   └── PracticePanel.jsx
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
├── index.html
├── package.json
└── vite.config.js
```
