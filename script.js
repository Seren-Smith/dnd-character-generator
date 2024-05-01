document.addEventListener('DOMContentLoaded', function() {
    fetch('races.json')
        .then(response => response.json())
        .then(data => populateDropdown('raceSelect', data.races.map(race => race.name)));

    fetch('classes.json')
        .then(response => response.json())
        .then(data => populateDropdown('classSelect', data.classes.map(cls => cls.name)));
});

function populateDropdown(selectId, options) {
    const select = document.getElementById(selectId);
    select.innerHTML = '<option value="">Select an Option</option>';
    options.forEach(option => {
        let opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

function loadRaceAndClassData() {
    // Here, define logic to calculate and display character data based on selections.
    const race = document.getElementById('raceSelect').value;
    const className = document.getElementById('classSelect').value;
    
    // Display the selected race and class on the HTML page
    const characterOutput = document.getElementById('characterOutput');
    characterOutput.innerHTML = `<p>Class: ${className}, Race: ${race}</p>`;
}
