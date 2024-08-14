# Weather Application using React and Python

This is a simple web application that allows users to get the current weather information for any city. The application is built using React for the frontend and Python (Flask) for the backend.
<br>
<br>
<img src="images\Screenshot of Code.png" alt="Screenshot of Code">
<br>

## Features

- Get current weather information for any city.
- Displays temperature.
- Shows the current date and time of the searched city.
- Error message displayed if no city is entered.

## Project Structure

```
weather_app/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── __pycache__/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── weather_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── weather.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── weather_service.py
│   └── utils/
│       ├── __pycache__/
│       └── cache.py
├── frontend/
│   ├── node_modules/ (created after npm install)
│   ├── public/
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── CityForm.js
│   │   │   └── WeatherDisplay.js
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── reportWebVitals.js
│   │   └── setupTests.js
│   ├── .gitignore
│   ├── package-lock.json
│   ├── package.json
│   └── README.md
├── images/
│   ├── Screenshot of Code.png
│   └── Screenshot of Website.png
├── venv/ (created after 'python -m venv venv')
├── README.md
├── run.py
└── requirements.txt

```

## Installation

### Backend (Python/Flask)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather_app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather_app
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the backend server:
   ```bash
   python run.py
   ```

### Frontend (React)

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install the required packages:
   ```bash
   npm install
   ```
3. Start the frontend development server:
   ```bash
   npm start
   ```

## Usage

1. Ensure the backend server is running.
2. Open your web browser and navigate to `http://localhost:3000`.

   <img src="images\Screenshot of Output.png" alt="Screenshot of Output">

3. Enter a city name and click "Get Weather" to view the weather information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Reference Utilised

1. [React JS Tutorial – Build a Weather App With Cities Autocomplete](https://youtu.be/Reny0cTTv24?si=c8rBKb1QnqP2u_qL)
2. [Professional Weather App with Django in Python](https://youtu.be/lyeK0aE_qRg?si=6XPBjSUDwvbpNh5T)
3. [How To Make Weather App Using React JS 2024 | Weather API React Project Tutorial](https://youtu.be/zs1Nq2s_uy4?si=3jwWFvfSfkqZ54jP)
4. [React Tutorial](https://www.w3schools.com/REACT/DEFAULT.ASP)
5. [React Js Tutorial for beginners in Tamil 2024 |Full Course for Beginners |Basic to Advanced concepts](https://youtu.be/Uv7cKlZFXU8?si=TH8wr7-qEjb6gcsB)
