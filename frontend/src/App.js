import React, { useState } from "react";

function App() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const handleSubmit = async () => {
        const response = await fetch("http://localhost:8000/query/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question }),
        });
        const data = await response.json();
        setAnswer(data.answer);
    };

    return (
        <div>
            <h1>Oil and Gas Reasoning Agent</h1>
            <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} />
            <button onClick={handleSubmit}>Ask</button>
            <p>{answer}</p>
        </div>
    );
}

export default App;
