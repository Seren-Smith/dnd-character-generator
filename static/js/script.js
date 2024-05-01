function generateCharacter() {
    const classSelected = document.getElementById('classSelect').value;
    const prestigeSelected = document.getElementById('prestigeSelect').value;
    const multiClassSelected = document.getElementById('multiClassSelect').value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({class: classSelected, prestige: prestigeSelected, multi_class: multiClassSelected})
    })
    .then(response => response.json())
    .then(data => {
        let output = `<h2>Generated Character</h2>`;
        output += `<p>Base Class: ${data.base_class}</p>`;
        if (data.prestige_class) {
            output += `<p>Prestige Class: ${data.prestige_class}</p>`;
        }
        if (data.multi_class) {
            output += `<p>Secondary Class: ${data.multi_class}</p>`;
        }
        output += `<p>Stats:</p><ul>`;
        for (const [key, value] of Object.entries(data.stats)) {
            output += `<li>${key}: ${value}</li>`;
        }
        output += `</ul>`;
        document.getElementById('characterOutput').innerHTML = output;
    })
    .catch(error => console.error('Error:', error));
}
