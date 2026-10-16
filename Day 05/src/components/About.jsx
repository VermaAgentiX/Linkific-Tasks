import { ArrowUpRight, Check } from "lucide-react";

const values = [
  "Clarity over complexity",
  "Curiosity in every iteration",
  "Progress you can measure",
];

export default function About() {
  return (
    <section className="about section-pad" id="about">
      <div className="container about-grid">
        <div className="about-visual">
          <div className="about-orb orb-a" />
          <div className="about-orb orb-b" />
          <div className="about-note note-one"><span>↗</span> Think clearly</div>
          <div className="about-note note-two"><span>✳</span> Make boldly</div>
          <div className="about-center">
            <span className="center-star">✳</span>
            <span>MAKE<br />IT MATTER</span>
          </div>
        </div>
        <div className="about-copy">
          <div className="eyebrow"><span className="eyebrow-line" /> A LITTLE ABOUT US</div>
          <h2>Good work starts with <span className="gradient-text">good questions.</span></h2>
          <p>We believe the best digital products come from listening closely, working collaboratively, and staying focused on the people who use them.</p>
          <ul className="value-list">
            {values.map((value) => (
              <li key={value}><span className="check-icon"><Check size={14} /></span>{value}</li>
            ))}
          </ul>
          <a className="text-link" href="#contact">More about our approach <ArrowUpRight size={17} /></a>
        </div>
      </div>
    </section>
  );
}
