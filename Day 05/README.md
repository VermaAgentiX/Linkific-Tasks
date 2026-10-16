# Nova — React Landing Page

A responsive, component-based landing page created as a React Fundamentals practice project.

## Features
- Responsive navigation with a mobile menu
- Hero section and calls to action
- Reusable feature cards rendered from an array
- About section and simple stats
- Footer with the current year
- React state with `useState`
- Icons from `lucide-react`
- Responsive CSS and reduced-motion support

## Requirements
- Node.js (use a current LTS release)
- npm (included with Node.js)

## Run locally
```bash
npm install
npm run dev
```
Open the local URL printed by Vite, usually `http://localhost:5173`.

## Production build
```bash
npm run build
npm run preview
```

## Project structure
```text
src/
├── components/
│   ├── Navbar.jsx
│   ├── Hero.jsx
│   ├── Features.jsx
│   ├── About.jsx
│   └── Footer.jsx
├── App.jsx
├── App.css
├── index.css
└── main.jsx
```

## Concepts practiced
JSX, components, props, `useState`, event handling, array `map()`, semantic HTML, responsive CSS, and Vite.

## Customize
Edit the content in the components and styles in `src/App.css` and `src/index.css`.
