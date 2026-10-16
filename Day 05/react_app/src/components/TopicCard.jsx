import { Check, ChevronRight } from 'lucide-react'

export default function TopicCard({ topic, completed, onToggle }) {
  return (
    <article className={`topic-card ${completed ? 'is-complete' : ''}`}>
      <div className="topic-card-top">
        <span className="topic-number">{topic.number}</span>
        <span className="topic-icon">{topic.icon}</span>
      </div>
      <h3>{topic.title}</h3>
      <p>{topic.description}</p>
      <div className="topic-example"><span>QUICK EXAMPLE</span><code>{topic.example}</code></div>
      <button className={`complete-btn ${completed ? 'done' : ''}`} onClick={onToggle} type="button">
        {completed ? <><Check size={16} /> Revised</> : <>Mark as revised <ChevronRight size={16} /></>}
      </button>
    </article>
  )
}
