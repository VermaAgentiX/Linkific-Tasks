import { useMemo, useState } from 'react'
import { ArrowDown, CheckCircle2, Code2, Component, Database, MousePointerClick, Puzzle, Sparkles } from 'lucide-react'
import Header from './components/Header.jsx'
import TopicCard from './components/TopicCard.jsx'
import PracticePanel from './components/PracticePanel.jsx'
import './App.css'

const topics = [
  { number: '01', icon: '⌘', title: 'JSX', description: 'Write UI with HTML-like syntax inside JavaScript. Use className and curly braces for expressions.', example: '<h1>{title}</h1>' },
  { number: '02', icon: '▦', title: 'Components', description: 'Split an interface into small, reusable function components with clear responsibilities.', example: '<Header />' },
  { number: '03', icon: '⇢', title: 'Props', description: 'Pass data from a parent to a child. Props are read-only inputs to a component.', example: '<TopicCard title="JSX" />' },
  { number: '04', icon: '↻', title: 'State · useState', description: 'Store values that change over time. Updating state tells React to render the UI again.', example: 'const [n, setN] = useState(0)' },
  { number: '05', icon: '⚡', title: 'Events', description: 'Respond to clicks and input changes by passing event handlers to JSX elements.', example: 'onClick={() => setN(n + 1)}' },
  { number: '06', icon: '≋', title: 'Lists · map()', description: 'Render repeated UI from arrays and give each item a stable key.', example: 'items.map(x => <Card key={x.id} />)' },
  { number: '07', icon: '◇', title: 'Conditional UI', description: 'Show different content based on state or props using ternaries and logical AND.', example: '{done ? "Done" : "Start"}' },
  { number: '08', icon: '⇄', title: 'useEffect', description: 'Synchronize a component with external systems when needed; do not use it for every calculation.', example: 'useEffect(() => { ... }, [])' },
]

function SummaryStat({ icon: Icon, value, label }) {
  return <div className="summary-stat"><span className="summary-icon"><Icon size={17} /></span><strong>{value}</strong><span>{label}</span></div>
}

export default function App() {
  const [completed, setCompleted] = useState([])
  const [count, setCount] = useState(0)
  const [name, setName] = useState('')
  const progress = useMemo(() => Math.round((completed.length / topics.length) * 100), [completed.length])

  function toggleTopic(number) {
    setCompleted(current => current.includes(number) ? current.filter(item => item !== number) : [...current, number])
  }

  return (
    <div id="top">
      <Header />
      <main>
        <section className="hero container">
          <div className="hero-copy">
            <div className="hero-badge"><Sparkles size={14} /> DAY 5 · FRONTEND REVISION</div>
            <h1>React basics,<br /><span>made practical.</span></h1>
            <p>One small playground to revise JSX, components, props, state, events, lists, and Hooks. Read a card, try the interactive examples, and mark topics as revised.</p>
            <a className="primary-link" href="#topics">Start revising <ArrowDown size={17} /></a>
            <div className="hero-note"><CheckCircle2 size={16} /> Learn by exploring, not just reading.</div>
          </div>
          <div className="hero-visual" aria-label="Illustration of React concepts">
            <div className="visual-grid" />
            <div className="visual-ring ring-a" /><div className="visual-ring ring-b" />
            <div className="react-orb"><Code2 size={54} strokeWidth={1.3} /></div>
            <div className="floating-label label-jsx"><Code2 size={15} /> JSX</div>
            <div className="floating-label label-props"><Puzzle size={15} /> Props</div>
            <div className="floating-label label-state"><Database size={15} /> State</div>
            <div className="floating-label label-components"><Component size={15} /> Components</div>
            <div className="click-hint"><MousePointerClick size={14} /> Interactive playground</div>
          </div>
        </section>

        <section className="progress-section container" aria-label="Revision progress">
          <div className="progress-copy"><div><span className="section-kicker">YOUR REVISION</span><h2>{completed.length} of {topics.length} topics completed</h2></div><strong>{progress}%</strong></div>
          <div className="progress-track"><div className="progress-fill" style={{ width: `${progress}%` }} /></div>
          <div className="summary-stats">
            <SummaryStat icon={Component} value="08" label="Core topics" />
            <SummaryStat icon={Code2} value="03" label="Interactive examples" />
            <SummaryStat icon={CheckCircle2} value={`${completed.length.toString().padStart(2, '0')}`} label="Marked revised" />
          </div>
        </section>

        <section className="topics-section container" id="topics">
          <div className="section-heading"><div><span className="section-kicker">THE BUILDING BLOCKS</span><h2>Eight concepts to know.</h2></div><p>Mark each topic as revised to track your progress. You can unmark it any time.</p></div>
          <div className="topic-grid">
            {topics.map(topic => <TopicCard key={topic.number} topic={topic} completed={completed.includes(topic.number)} onToggle={() => toggleTopic(topic.number)} />)}
          </div>
        </section>

        <div className="container"><PracticePanel count={count} setCount={setCount} name={name} setName={setName} /></div>

        <section className="challenge container">
          <div><span className="section-kicker">QUICK SELF-CHECK</span><h2>Can you explain these?</h2><p>Try answering out loud without looking at the cards.</p></div>
          <ol><li>What is the difference between props and state?</li><li>Why should list items have a stable key?</li><li>When would you use useEffect?</li><li>What causes a component to re-render?</li></ol>
        </section>
      </main>
      <footer className="footer"><div className="container footer-inner"><a className="brand" href="#top"><span className="brand-icon"><Sparkles size={17} /></span> React Basics Lab</a><span>Built for Day 5 learning · React + Vite</span><a href="#top">Back to top ↑</a></div></footer>
    </div>
  )
}
