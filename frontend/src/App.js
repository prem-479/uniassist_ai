import React, { useState, useEffect, useRef } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [agent, setAgent] = useState("meal");
  const [loading, setLoading] = useState(false);
  const [recording, setRecording] = useState(false);

  // -------------------------------
  // DARK MODE STATE + HANDLER
  // -------------------------------
  const [darkMode, setDarkMode] = useState(
    localStorage.getItem("theme") === "dark"
  );

  const toggleTheme = () => {
    const newTheme = !darkMode;
    setDarkMode(newTheme);

    if (newTheme) {
      document.body.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  };

  useEffect(() => {
    if (darkMode) {
      document.body.classList.add("dark");
    }
  }, []);

  // -------------------------------
  // AUTOSCROLL
  // -------------------------------
  const chatEndRef = useRef(null);
  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  useEffect(scrollToBottom, [messages]);

  // -------------------------------
  // VOICE INPUT (MIC)
  // -------------------------------
  const startRecording = () => {
    if (!("webkitSpeechRecognition" in window)) {
      alert("Speech Recognition not supported in this browser");
      return;
    }

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    setRecording(true);
    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript);
    };

    recognition.onerror = () => setRecording(false);
    recognition.onend = () => setRecording(false);
  };

  // -------------------------------
  // SEND MESSAGE TO BACKEND
  // -------------------------------
  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input, agent }),
      });

      const data = await response.json();

      const botMsg = {
        sender: "bot",
        text: data.reply,
      };

      setMessages((prev) => [...prev, botMsg]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "⚠ Error contacting backend." },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      {/* HEADER WITH AGENT DROPDOWN + DARK MODE TOGGLE */}
      <header
        style={{
          padding: 10,
          background: "var(--header-bg)",
          borderBottom: "1px solid #444",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <select
          value={agent}
          onChange={(e) => setAgent(e.target.value)}
          style={{
            padding: 6,
            borderRadius: 6,
            border: "1px solid #555",
            background: "var(--input-bg)",
            color: "var(--text)",
          }}
        >
          <option value="meal">🍽 Meal</option>
          <option value="gym">🏋️ Gym</option>
          <option value="travel">✈️ Travel</option>
          <option value="shopping">🛒 Shopping</option>
          <option value="academic">📚 Academic</option>
        </select>

        <button
          onClick={toggleTheme}
          style={{
            background: "transparent",
            border: "none",
            fontSize: 26,
            cursor: "pointer",
            color: "var(--text)",
          }}
        >
          {darkMode ? "🌙" : "☀️"}
        </button>
      </header>

      {/* CHAT WINDOW */}
      <div className="chat-window">
        {messages.map((m, i) => (
          <div
            key={i}
            className={m.sender === "user" ? "bubble-user" : "bubble-bot"}
          >
            {m.text}
          </div>
        ))}

        {loading && (
          <div className="bubble-bot">Gemini is thinking… ⏳</div>
        )}

        <div ref={chatEndRef} />
      </div>

      {/* INPUT AREA */}
      <div className="input-area">
        <button
          onClick={startRecording}
          className="mic-btn"
        >
          {recording ? "🎤..." : "🎤"}
        </button>

        <input
          className="chat-input"
          placeholder="Type your message…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />

        <button className="send-btn" onClick={sendMessage}>
          ➤
        </button>
      </div>
    </div>
  );
}

export default App;
