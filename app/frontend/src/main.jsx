import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return (
    <main className="page">
      <header>
        <h1>ShopStack</h1>
        <span>Production-style E-Commerce Demo</span>
      </header>
      <section className="hero">
        <h2>Build. Secure. Ship.</h2>
        <p>React + FastAPI + Kubernetes + AWS EKS</p>
      </section>
      <section className="cards">
        {["Laptop", "Headphones", "Keyboard"].map((item, index) => (
          <article key={item}>
            <h3>{item}</h3>
            <p>Demo product #{index + 1}</p>
            <button>Add to cart</button>
          </article>
        ))}
      </section>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
