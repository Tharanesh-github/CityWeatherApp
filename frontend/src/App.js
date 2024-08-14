import React, { useState } from "react";
import axios from "axios";
import CityForm from "./components/CityForm";
import WeatherDisplay from "./components/WeatherDisplay";
import "./App.css";

function App() {
	const [weather, setWeather] = useState(null);
	const [error, setError] = useState(null);

	const getWeather = async (city) => {
		const apiKey = "2b1b3c4389b5475aa2c145524241108"; // Replace with your actual API key
		const url = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}&aqi=no`;
		try {
			const response = await axios.get(url);
			setWeather(response.data);
			setError(null); // Clear any previous errors
		} catch (error) {
			setError("Error fetching weather data. Please try again.");
			setWeather(null); // Clear previous weather data
		}
	};

	return (
		<div className="App">
			<h1>Weather App</h1>
			<CityForm getWeather={getWeather} />
			{error && <p className="error">{error}</p>}
			<WeatherDisplay weather={weather} />
		</div>
	);
}

export default App;
