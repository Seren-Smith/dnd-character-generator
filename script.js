document.addEventListener('DOMContentLoaded', function() {
    fetch('races.json')
        .then(response => response.json())
        .then(data => {
            let races = data.races.map(race => race.name);
            races.unshift("Random"); // Add "Random" option at the beginning
            populateDropdown('raceSelect', races);
        });

    fetch('classes.json')
        .then(response => response.json())
        .then(data => {
            let classes = data.classes.map(cls => cls.name);
            classes.unshift("Random"); // Add "Random" option at the beginning
            populateDropdown('classSelect', classes);
        });
});

function populateDropdown(selectId, options) {
    const select = document.getElementById(selectId);
    select.innerHTML = '';
    options.forEach(option => {
        let opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

function loadRaceAndClassData() {
    // Here, define logic to calculate and display character data based on selections.
    const raceSelect = document.getElementById('raceSelect');
    const classSelect = document.getElementById('classSelect');
    
    const race = raceSelect.value === "Random" ? getRandomOption(raceSelect) : raceSelect.value;
    const className = classSelect.value === "Random" ? getRandomOption(classSelect) : classSelect.value;
    
    // Display the selected race and class on the HTML page
    const characterOutput = document.getElementById('characterOutput');
    characterOutput.innerHTML = `<p>Class: ${className}, Race: ${race}</p>`;
}

function getRandomOption(select) {
    const options = select.options;
    const randomIndex = Math.floor(Math.random() * (options.length - 1)); // Exclude "Random" option
    return options[randomIndex + 1].value;
}
