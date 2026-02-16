function toggleMode() {
    document.body.classList.toggle("dark");
}

function updateCityClock() {
    const clockElement = document.getElementById("liveClock");
    if (!clockElement) return;

    const offset = parseInt(clockElement.dataset.timezone);

    const now = new Date();

    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);

    const cityTime = new Date(utc + (offset * 1000));

    const timeString = cityTime.toLocaleTimeString();
    const dateString = cityTime.toLocaleDateString(undefined, {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });

    clockElement.innerHTML = `${dateString}<br><strong>${timeString}</strong>`;
}

setInterval(updateCityClock, 1000);
updateCityClock();
