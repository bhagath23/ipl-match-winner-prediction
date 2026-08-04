import Select from "react-select";
import "../styles/MatchForm.css";

const customStyles = {
  control: (provided) => ({
    ...provided,
    backgroundColor: "#ffffff",
    border: "2px solid #2b6cff",
    borderRadius: "12px",
    minHeight: "54px",
    boxShadow: "none",
  }),

  menu: (provided) => ({
    ...provided,
    backgroundColor: "#ffffff",
    color: "#111827",
    zIndex: 9999,
  }),

  menuList: (provided) => ({
    ...provided,
    maxHeight: "220px",
  }),

  option: (provided, state) => ({
    ...provided,
    backgroundColor: state.isSelected
      ? "#2563eb"
      : state.isFocused
      ? "#dbeafe"
      : "#ffffff",
    color: state.isSelected ? "#ffffff" : "#111827",
    cursor: "pointer",
    fontSize: "16px",
  }),

  singleValue: (provided) => ({
    ...provided,
    color: "#111827",
  }),

  input: (provided) => ({
    ...provided,
    color: "#111827",
  }),

  placeholder: (provided) => ({
    ...provided,
    color: "#6b7280",
  }),
};

function MatchForm({
  metadata,
  team1,
  setTeam1,
  team2,
  setTeam2,
  venue,
  setVenue,
  tossWinner,
  setTossWinner,
  tossDecision,
  setTossDecision,
  onPredict,
  loading,
}) {
  const teamOptions = metadata.teams.map((team) => ({
    value: team,
    label: team,
  }));

  const venueOptions = metadata.venues.map((venue) => ({
    value: venue,
    label: venue,
  }));

  const tossDecisionOptions = [
    { value: "bat", label: "Bat First" },
    { value: "field", label: "Bowl First" },
  ];

  return (
    <>
      <div className="form-group">
        <label>Team 1</label>

        <Select
          value={team1}
          onChange={setTeam1}
          options={teamOptions}
          styles={customStyles}
          placeholder="Select Team 1"
          isSearchable
        />
      </div>

      <div className="form-group">
        <label>Team 2</label>

        <Select
          value={team2}
          onChange={setTeam2}
          options={teamOptions.filter(
            (team) => team.value !== team1?.value
          )}
          styles={customStyles}
          placeholder="Select Team 2"
          isSearchable
        />
      </div>

      <div className="form-group">
        <label>Venue</label>

        <Select
          value={venue}
          onChange={setVenue}
          options={venueOptions}
          styles={customStyles}
          placeholder="Select Venue"
          isSearchable
        />
      </div>

      <div className="form-group">
        <label>Toss Winner</label>

        <Select
          value={tossWinner}
          onChange={setTossWinner}
          options={[
            team1,
            team2,
          ].filter(Boolean)}
          styles={customStyles}
          placeholder="Select Toss Winner"
          isSearchable={false}
        />
      </div>

      <div className="form-group">
        <label>Toss Decision</label>

        <Select
          value={tossDecision}
          onChange={setTossDecision}
          options={tossDecisionOptions}
          styles={customStyles}
          placeholder="Select Toss Decision"
          isSearchable={false}
        />
      </div>

      <button
        className="predict-btn"
        onClick={onPredict}
        disabled={loading}
      >
        {loading ? "Predicting..." : "Predict Winner"}
      </button>
    </>
  );
}

export default MatchForm;