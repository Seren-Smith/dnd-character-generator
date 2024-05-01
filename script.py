function loadRaceBonus() {
    const race = document.getElementById('raceSelect').value;
    if (race) {
        axios.get('https://your_lambda_url', {
            params: { race_name: race }
        })
        .then(function (response) {
            const data = response.data;
            let output = `<h2>${race} Race Bonuses</h2><ul>`;
            for (const [key, value] of Object.entries(data.bonuses)) {
                output += `<li>${key}: ${value}</li>`;
            }
            output += `</ul>`;
            document.getElementById('raceOutput').innerHTML = output;
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
    } else {
        document.getElementById('raceOutput').innerHTML = `<p>Please select a race to see bonuses.</p>`;
    }
}
