import { useEffect, useState } from "react";
import "./styles/App.css";

import api from "./services/api";

import MatchForm from "./components/MatchForm";
import PredictionCard from "./components/PredictionCard";
import LoadingSpinner from "./components/LoadingSpinner";

import trophy from "./assets/logos/trophy.png";

function App() {
  const [metadata, setMetadata] = useState(null);

  const [team1, setTeam1] = useState(null);
  const [team2, setTeam2] = useState(null);
  const [venue, setVenue] = useState(null);

  const [tossWinner, setTossWinner] = useState(null);
  const [tossDecision, setTossDecision] = useState(null);

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchMetadata() {
      try {
        const response = await api.get("/metadata");
        setMetadata(response.data);
      } catch (error) {
        console.error(error);
      }
    }

    fetchMetadata();
  }, []);

  useEffect(() => {
    setTossWinner(null);
  }, [team1, team2]);

  async function handlePredict() {
    if (
      !team1 ||
      !team2 ||
      !venue ||
      !tossWinner ||
      !tossDecision
    ) {
      alert("Please fill all fields.");
      return;
    }

    try {
      setLoading(true);
      setPrediction(null);

      const response = await api.post("/predict", {
        team1: team1.value,
        team2: team2.value,
        venue: venue.value,
        toss_winner: tossWinner.value,
        toss_decision: tossDecision.value,
      });

      setPrediction(response.data);
    } catch (error) {
      console.error(error);
      alert("Prediction failed.");
    } finally {
      setLoading(false);
    }
  }

  if (!metadata) {
    return (
      <div className="hero">
        <div className="hero-content">
          <img src={trophy} alt="IPL Trophy" />
          <h1>IPL Analytics Platform</h1>
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="hero">
        <div className="hero-content">
          <img src={trophy} alt="IPL Trophy" />

          <h1>IPL Analytics Platform</h1>

          <p>
            Predict IPL Match Winners using
            <br />
            Artificial Intelligence & Machine Learning
          </p>
        </div>
      </div>

      <div className="app-container">
        <div className="card">
          <MatchForm
            metadata={metadata}
            team1={team1}
            setTeam1={setTeam1}
            team2={team2}
            setTeam2={setTeam2}
            venue={venue}
            setVenue={setVenue}
            tossWinner={tossWinner}
            setTossWinner={setTossWinner}
            tossDecision={tossDecision}
            setTossDecision={setTossDecision}
            onPredict={handlePredict}
            loading={loading}
          />

          {loading && <LoadingSpinner />}

          <PredictionCard
            prediction={prediction}
            team1={team1}
            team2={team2}
          />
        </div>
      </div>
    </>
  );
}

export default App;