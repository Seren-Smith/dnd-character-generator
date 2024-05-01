document.addEventListener('DOMContentLoaded', function() {
    fetch('data/races.json')
        .then(response => response.json())
        .then(data => populateDropdown('raceSelect', data.races.map(race => race.name)));

    fetch('data/classes.json')
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
    console.log(`Selected Race: ${race}, Selected Class: ${className}`);
    // Additional logic to handle races and classes can be added here.
}
