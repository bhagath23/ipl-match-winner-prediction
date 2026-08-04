import "../styles/PredictionCard.css";
import teamAssets from "../utils/teamAssets";

function PredictionCard({ prediction, team1, team2 }) {
  if (!prediction) return null;

  const winner = teamAssets[prediction.predicted_winner];
  const team1Asset = teamAssets[team1?.label];
  const team2Asset = teamAssets[team2?.label];

  const winnerProbability =
    prediction.predicted_winner === team1.label
      ? prediction.team1_probability
      : prediction.team2_probability;

  const loserProbability =
    prediction.predicted_winner === team1.label
      ? prediction.team2_probability
      : prediction.team1_probability;

  const reasons = [];

  if (prediction.team1_strength > prediction.team2_strength) {
    reasons.push(`${team1.label} has a stronger overall team strength.`);
  } else if (prediction.team2_strength > prediction.team1_strength) {
    reasons.push(`${team2.label} has a stronger overall team strength.`);
  }

  if (prediction.team1_recent_form > prediction.team2_recent_form) {
    reasons.push(`${team1.label} has better recent form.`);
  } else if (prediction.team2_recent_form > prediction.team1_recent_form) {
    reasons.push(`${team2.label} has better recent form.`);
  }

  if (prediction.team1_h2h > prediction.team2_h2h) {
    reasons.push(`${team1.label} has a better head-to-head record.`);
  } else if (prediction.team2_h2h > prediction.team1_h2h) {
    reasons.push(`${team2.label} has a better head-to-head record.`);
  }

  if (
    prediction.team1_venue_strength >
    prediction.team2_venue_strength
  ) {
    reasons.push(`${team1.label} has performed better at this venue.`);
  } else if (
    prediction.team2_venue_strength >
    prediction.team1_venue_strength
  ) {
    reasons.push(`${team2.label} has performed better at this venue.`);
  }

  return (
    <div className="prediction-card">
      <h2 className="prediction-title">🏆 Match Prediction</h2>

      {winner && (
        <img
          src={winner.logo}
          alt={prediction.predicted_winner}
          style={{
            width: "140px",
            display: "block",
            margin: "20px auto",
          }}
        />
      )}

      <h1
        className="winner-name"
        style={{
          color: winner?.color || "#FFD700",
        }}
      >
        {prediction.predicted_winner}
      </h1>

      <h3 className="probability-title">
        Winning Probability
      </h3>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "15px",
          marginBottom: "15px",
        }}
      >
        {team1Asset && (
          <img
            src={team1Asset.logo}
            alt={team1.label}
            style={{
              width: "55px",
              height: "55px",
              objectFit: "contain",
            }}
          />
        )}

        <div style={{ flex: 1 }}>
          <p className="team-name">{team1.label}</p>

          <progress
            className="progress-bar"
            value={prediction.team1_probability}
            max="100"
          />

          <p className="team-percent">
            {prediction.team1_probability.toFixed(2)}%
          </p>
        </div>
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "15px",
        }}
      >
        {team2Asset && (
          <img
            src={team2Asset.logo}
            alt={team2.label}
            style={{
              width: "55px",
              height: "55px",
              objectFit: "contain",
            }}
          />
        )}

        <div style={{ flex: 1 }}>
          <p className="team-name">{team2.label}</p>

          <progress
            className="progress-bar"
            value={prediction.team2_probability}
            max="100"
          />

          <p className="team-percent">
            {prediction.team2_probability.toFixed(2)}%
          </p>
        </div>
      </div>

      <div
        style={{
          marginTop: "35px",
          padding: "20px",
          borderRadius: "12px",
          background: "rgba(255,255,255,0.06)",
          textAlign: "left",
        }}
      >
        <h2 style={{ marginBottom: "15px" }}>
          📝 Match Summary
        </h2>

        <p style={{ lineHeight: "1.8" }}>
          <strong>{prediction.predicted_winner}</strong> is predicted to
          win this match with a{" "}
          <strong>{winnerProbability.toFixed(2)}%</strong> probability.
          The opposing team still has a{" "}
          <strong>{loserProbability.toFixed(2)}%</strong> chance, making
          this prediction competitive.
        </p>

        <h3 style={{ marginTop: "20px" }}>
          Key Factors
        </h3>

        <ul style={{ marginTop: "10px", lineHeight: "2" }}>
          {reasons.map((reason, index) => (
            <li key={index}>{reason}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default PredictionCard;