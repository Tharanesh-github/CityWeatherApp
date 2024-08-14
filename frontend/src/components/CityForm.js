import React, { useState } from "react";

const CityForm = ({ getWeather }) => {
	const [city, setCity] = useState("");
	const [error, setError] = useState("");

	const handleSubmit = (e) => {
		e.preventDefault();
		if (city.trim() === "") {
			setError("Please enter a city");
		} else {
			setError("");
			getWeather(city);
		}
	};

	return (
		<form onSubmit={handleSubmit}>
			<input
				type="text"
				placeholder="Enter city"
				value={city}
				onChange={(e) => setCity(e.target.value)}
			/>
			<button type="submit">Get Weather</button>
			{error && <p className="error">{error}</p>}
		</form>
	);
};

export default CityForm;
