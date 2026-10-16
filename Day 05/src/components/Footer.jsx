import { ArrowUpRight, Sparkles } from "lucide-react";

export default function Footer() {
  return (
    <footer className="footer" id="contact">
      <div className="container">
        <div className="footer-cta">
          <div>
            <div className="eyebrow"><span className="eyebrow-line" /> HAVE A GOOD ONE IN MIND?</div>
            <h2>Let's make it<br /><span className="gradient-text">happen.</span></h2>
          </div>
          <a className="button button-primary" href="mailto:hello@example.com">
            Start a conversation <ArrowUpRight size={18} />
          </a>
        </div>
        <div className="footer-bottom">
          <a className="brand" href="#home">
            <span className="brand-mark"><Sparkles size={18} /></span>
            <span>nova<span className="brand-dot">.</span></span>
          </a>
          <p>Independent by nature. Collaborative by design.</p>
          <span>© {new Date().getFullYear()} Nova Studio</span>
        </div>
      </div>
    </footer>
  );
}
