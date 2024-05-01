document.addEventListener('DOMContentLoaded', function() {
    fetch('races.json')
        .then(response => response.json())
        .then(data => {
            const races = data.races.map(race => race.name);
            populateDropdown('raceSelect', races);
        });

    fetch('classes.json')
        .then(response => response.json())
        .then(data => {
            const classes = data.classes.map(cls => cls.name);
            populateDropdown('classSelect', classes);
        });
});

function populateDropdown(selectId, options) {
    const select = document.getElementById(selectId);
    select.innerHTML = '';
    
    // Populate options
    options.forEach(option => {
        let opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

function generateRandomStats() {
    const randomStat = () => Math.floor(Math.random() * 14) + 5; // Generates a random number between 5 and 18

    return {
        Strength: randomStat(),
        Dexterity: randomStat(),
        Constitution: randomStat(),
        Intelligence: randomStat(),
        Wisdom: randomStat(),
        Charisma: randomStat()
    };
}

function loadRaceAndClassData() {
    // Here, define logic to calculate and display character data based on selections.
    const raceSelect = document.getElementById('raceSelect');
    const classSelect = document.getElementById('classSelect');
    
    const race = raceSelect.value;
    const className = classSelect.value;

    const stats = generateRandomStats();

    // Display the selected race and class on the HTML page
    const characterOutput = document.getElementById('characterOutput');
    characterOutput.innerHTML = `<p>Class: ${className}, Race: ${race}</p>`;

    characterOutput.innerHTML += '<p>Stats:</p><ul>';
    for (const stat in stats) {
        characterOutput.innerHTML += `<li>${stat}: ${stats[stat]}</li>`;
    }
    characterOutput.innerHTML += '</ul>';
}
