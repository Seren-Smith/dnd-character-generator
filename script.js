function loadRaceAndClassData() {
    const race = document.getElementById('raceSelect').value;
    const className = document.getElementById('classSelect').value; // Ensure this exists in your HTML
    if (race && className) {
        axios.get('https://your_lambda_url', {
            params: { race_name: race, class_name: className }
        })
        .then(function (response) {
            const data = response.data;
            let output = `<h2>Character Details</h2>`;
            output += `<p>Race: ${data.race}</p>`;
            output += `<p>Class: ${data.class}</p>`;
            output += `<p>Stats:</p><ul>`;
            Object.entries(data.stats).forEach(([key, value]) => {
                output += `<li>${key}: ${value}</li>`;
            });
            output += `</ul>`;
            document.getElementById('raceOutput').innerHTML = output;
        })
        .catch(function (error) {
            console.error('Error:', error);
            document.getElementById('raceOutput').innerHTML = `<p>Error loading character data. Please try again.</p>`;
        });
    } else {
        document.getElementById('raceOutput').innerHTML = `<p>Please select both a race and a class to see details.</p>`;
    }
}
