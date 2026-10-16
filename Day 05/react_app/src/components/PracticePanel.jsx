import { Minus, Plus, RotateCcw } from 'lucide-react'

export default function PracticePanel({ count, setCount, name, setName }) {
  return (
    <section className="practice-panel" aria-labelledby="practice-title">
      <div className="practice-intro">
        <span className="section-kicker">TRY IT YOURSELF</span>
        <h2 id="practice-title">See state in action.</h2>
        <p>Change a value below. React re-renders the UI when state changes.</p>
      </div>
      <div className="practice-widgets">
        <div className="widget counter-widget">
          <span className="widget-label">STATE COUNTER</span>
          <div className="counter-row">
            <button type="button" aria-label="Decrease counter" onClick={() => setCount(c => c - 1)}><Minus size={17} /></button>
            <strong>{count}</strong>
            <button type="button" aria-label="Increase counter" onClick={() => setCount(c => c + 1)}><Plus size={17} /></button>
          </div>
          <button className="reset-btn" type="button" onClick={() => setCount(0)}><RotateCcw size={13} /> Reset counter</button>
        </div>
        <div className="widget input-widget">
          <label className="widget-label" htmlFor="name-input">CONTROLLED INPUT</label>
          <input id="name-input" value={name} onChange={event => setName(event.target.value)} placeholder="Type your name..." />
          <div className="live-preview"><span>LIVE PREVIEW</span><strong>{name.trim() || 'Your name appears here'}</strong></div>
        </div>
      </div>
    </section>
  )
}
