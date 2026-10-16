import { ArrowUpRight, Blocks, Gauge, Layers3, WandSparkles } from "lucide-react";

const features = [
  {
    number: "01",
    icon: WandSparkles,
    title: "Digital experiences",
    text: "Clear, intuitive interfaces that help people get things done without getting in the way.",
    tag: "DESIGN",
  },
  {
    number: "02",
    icon: Blocks,
    title: "Web development",
    text: "Flexible, reliable websites and apps built with modern tools and a solid foundation.",
    tag: "ENGINEERING",
  },
  {
    number: "03",
    icon: Layers3,
    title: "Brand systems",
    text: "A distinctive visual language that keeps every touchpoint consistent and recognizable.",
    tag: "IDENTITY",
  },
  {
    number: "04",
    icon: Gauge,
    title: "Growth & optimization",
    text: "Thoughtful improvements driven by feedback, performance, and measurable outcomes.",
    tag: "STRATEGY",
  },
];

function FeatureCard({ item }) {
  const Icon = item.icon;

  return (
    <article className="feature-card">
      <div className="feature-card-top">
        <span className="feature-number">{item.number}</span>
        <span className="feature-icon"><Icon size={21} strokeWidth={1.8} /></span>
      </div>
      <h3>{item.title}</h3>
      <p>{item.text}</p>
      <div className="feature-card-bottom">
        <span>{item.tag}</span>
        <a href="#contact" aria-label={`Discuss ${item.title}`}><ArrowUpRight size={18} /></a>
      </div>
    </article>
  );
}

export default function Features() {
  return (
    <section className="features section-pad" id="features">
      <div className="container">
        <div className="section-heading">
          <div>
            <div className="eyebrow"><span className="eyebrow-line" /> WHAT WE BRING</div>
            <h2>Small details.<br /><span className="muted-heading">Big difference.</span></h2>
          </div>
          <p>From the first sketch to the final launch, we connect strategy, design, and technology to make the complex feel simple.</p>
        </div>

        <div className="feature-grid">
          {features.map((item) => <FeatureCard key={item.number} item={item} />)}
        </div>
      </div>
    </section>
  );
}
