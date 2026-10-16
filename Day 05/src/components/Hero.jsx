import { ArrowDownRight, ArrowUpRight, Play } from "lucide-react";

export default function Hero() {
  return (
    <section className="hero section-pad" id="home">
      <div className="hero-glow hero-glow-one" aria-hidden="true" />
      <div className="hero-glow hero-glow-two" aria-hidden="true" />

      <div className="container hero-grid">
        <div className="hero-copy">
          <div className="eyebrow"><span className="status-dot" /> DIGITAL STUDIO FOR WHAT'S NEXT</div>
          <h1>Build something <span className="gradient-text">remarkable.</span></h1>
          <p className="hero-lede">
            We turn bold ideas into thoughtful digital experiences — crafted with
            clarity, powered by curiosity, and made to move your business forward.
          </p>
          <div className="hero-actions">
            <a className="button button-primary" href="#features">
              Explore what we do <ArrowUpRight size={18} />
            </a>
            <a className="button button-quiet" href="#about">
              <span className="play-icon"><Play size={13} fill="currentColor" /></span>
              Meet the studio
            </a>
          </div>
          <div className="hero-proof">
            <div className="avatar-stack" aria-hidden="true">
              <span>JD</span><span>MK</span><span>AL</span><span>+</span>
            </div>
            <div><strong>Good people. Great work.</strong><small>Built around your next big idea.</small></div>
          </div>
        </div>

        <div className="hero-art" aria-label="Abstract layered gradient artwork">
          <div className="art-orbit orbit-one" />
          <div className="art-orbit orbit-two" />
          <div className="art-card art-card-back">
            <div className="mini-label">CREATIVE DIRECTION</div>
            <div className="skeleton skeleton-long" />
            <div className="skeleton skeleton-short" />
            <div className="mini-chart"><span /><span /><span /><span /><span /><span /><span /></div>
          </div>
          <div className="art-sphere">
            <div className="sphere-shine" />
            <div className="sphere-ring" />
          </div>
          <div className="art-card art-card-front">
            <span className="live-pill"><span /> LIVE PREVIEW</span>
            <strong>Ideas into<br />impact.</strong>
            <span className="card-arrow"><ArrowDownRight size={19} /></span>
          </div>
          <div className="floating-chip chip-top">✦ Strategy first</div>
          <div className="floating-chip chip-bottom">Design <span>×</span> Technology</div>
        </div>
      </div>

      <div className="container hero-bottom">
        <span>SCROLL TO EXPLORE</span>
        <div className="scroll-line" />
        <span>01 — 04</span>
      </div>
    </section>
  );
}
