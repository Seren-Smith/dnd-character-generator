function generateCharacter() {
    const classSelected = document.getElementById('classSelect').value;
    const raceSelected = document.getElementById('raceSelect').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({class: classSelected, race: raceSelected})
    })
    .then(response => response.json())
    .then(data => {
        let output = `<h2>Generated Character</h2>`;
        output += `<p>Class: ${data.class}</p>`;
        output += `<p>Race: ${data.race}</p>`;
        output += `<p>Stats:</p><ul>`;
        for (const [key, value] of Object.entries(data.stats)) {
            output += `<li>${key}: ${value}</li>`;
        }
        output += `</ul>`;
        document.getElementById('characterOutput').innerHTML = output;
    })
    .catch(error => console.error('Error:', error));
}
