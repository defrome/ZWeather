document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('city-input');
    const searchBtn = document.getElementById('search-btn');
    const cityName = document.getElementById('city-name');
    const currentDate = document.getElementById('current-date');
    const temperature = document.getElementById('temperature');
    const weatherCondition = document.getElementById('weather-condition');
    const windSpeed = document.getElementById('wind-speed');
    const pressure = document.getElementById('pressure');
    const hourlyForecast = document.getElementById('hourly-forecast');

    // Установка текущей даты
    function updateDateTime() {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        currentDate.textContent = now.toLocaleDateString('en-US', options);
    }
    updateDateTime();

    // Поиск погоды
    searchBtn.addEventListener('click', fetchWeather);
    cityInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') fetchWeather();
    });

    // Загрузка погоды по умолчанию
    fetchWeather('London');

    async function fetchWeather(city = null) {
        const searchCity = city || cityInput.value.trim();
        if (!searchCity) return;

        try {
            // Показываем состояние загрузки
            cityName.textContent = 'Loading...';
            temperature.textContent = '-';
            weatherCondition.textContent = '-';
            windSpeed.textContent = '- km/h';
            pressure.textContent = '- in';
            hourlyForecast.innerHTML = '';

            const response = await fetch(`/current_weather?city=${encodeURIComponent(searchCity)}`);
            if (!response.ok) {
                throw new Error('City not found');
            }

            const data = await response.json();

            // Обновляем UI
            cityName.textContent = data.city;
            temperature.textContent = Math.round(data.temp);
            weatherCondition.textContent = data.condition;
            windSpeed.textContent = `${data.wind} km/h`;
            pressure.textContent = `${data.pressure} in`;

            // Генерируем почасовой прогноз (заглушка)
            generateHourlyForecast(data.temp);

        } catch (error) {
            cityName.textContent = 'Error';
            weatherCondition.textContent = error.message;
            console.error('Error fetching weather:', error);
        }
    }

    function generateHourlyForecast(currentTemp) {
        hourlyForecast.innerHTML = '';

        const now = new Date();
        const currentHour = now.getHours();

        for (let i = 0; i < 24; i += 3) {
            const hour = (currentHour + i) % 24;
            const hourTemp = Math.round(currentTemp + (Math.random() * 4 - 2));

            const hourCard = document.createElement('div');
            hourCard.className = 'hour-card';
            hourCard.innerHTML = `
                <div class="time">${hour}:00</div>
                <div class="temp">${hourTemp}°</div>
            `;

            hourlyForecast.appendChild(hourCard);
        }
    }
});