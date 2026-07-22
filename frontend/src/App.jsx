import { useState } from "react";
import "./App.css";

function TicketForm() {
  const [ticketId, setTicketId] = useState("");
  const [subcategory, setSubcategory] = useState("");
  const [priority, setPriority] = useState("");
  const [description, setDescription] = useState("");

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/analyze-ticket/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            ticket_id: ticketId,
            subcategory: subcategory,
            priority: priority,
            description: description,
          }),
        }
      );

      if (!response.ok) {
        const errorData = await response.json().catch(() => null);

        console.error("FastAPI error:", errorData);

        throw new Error(
          errorData?.detail
            ? JSON.stringify(errorData.detail)
            : `Request failed with status ${response.status}`
        );
      }

      const data = await response.json();

      console.log("Ticket analysis result:", data);
      setResult(data);
    } catch (requestError) {
      console.error("Request failed:", requestError);
      setError(requestError.message || "Unable to analyze the ticket.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Helpdesk Ticket Analyzer</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="ticket_id">Ticket ID</label>
          <br />

          <input
            id="ticket_id"
            type="text"
            value={ticketId}
            onChange={(event) => setTicketId(event.target.value)}
            placeholder="Enter the ticket ID"
            required
          />
        </div>

        <br />

        <div>
          <label htmlFor="subcategory">Subject / Subcategory</label>
          <br />

          <textarea
            id="subcategory"
            value={subcategory}
            onChange={(event) => setSubcategory(event.target.value)}
            placeholder="Example: Issues with Outlook"
            rows="3"
            cols="50"
            required
          />
        </div>

        <br />

        <div>
          <label htmlFor="priority">Priority</label>
          <br />

          <select
            id="priority"
            value={priority}
            onChange={(event) => setPriority(event.target.value)}
            required
          >
            <option value="">Select a priority</option>
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
            <option value="Critical">Critical</option>
          </select>
        </div>

        <br />

        <div>
          <label htmlFor="description">Description</label>
          <br />

          <textarea
            id="description"
            value={description}
            onChange={(event) => setDescription(event.target.value)}
            placeholder="Describe the user's issue"
            rows="8"
            cols="50"
          />
        </div>

        <br />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Ticket"}
        </button>
      </form>

      {error && (
        <div>
          <h2>Error</h2>
          <p>{error}</p>
        </div>
      )}

      {result && (
        <div>
          <h2>Analysis Result</h2>

          {result.category && (
            <p>
              <strong>Suggested Category:</strong> {result.category}
            </p>
          )}

          {result.confidence !== undefined && (
            <p>
              <strong>Confidence:</strong>{" "}
              {typeof result.confidence === "number"
                ? `${(result.confidence * 100).toFixed(2)}%`
                : result.confidence}
            </p>
          )}

          <h3>Full API Response</h3>

          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

function App() {
  return <TicketForm />;
}

export default App;