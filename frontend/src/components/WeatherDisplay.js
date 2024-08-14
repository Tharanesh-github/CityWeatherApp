import React from "react";

const WeatherDisplay = ({ weather }) => {
	if (!weather) {
		return <div>No weather data available</div>;
	}

	const { name, region, country, localtime } = weather.location;
	const { temp_c, condition } = weather.current;

	return (
		<div className="weather-data">
			<h2>
				Weather in {name}, {region}, {country}
			</h2>
			<p>Local Time: {localtime}</p>
			<p>Temperature: {temp_c}°C</p>
			<p>Condition: {condition.text}</p>
			<img
				src={condition.icon}
				alt="weather icon"
			/>
		</div>
	);
};

export default WeatherDisplay;
