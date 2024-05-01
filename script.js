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
    
    // Add Random option
    let opt = document.createElement('option');
    opt.value = "Random";
    opt.textContent = "Random";
    select.appendChild(opt);
    
    // Populate other options
    options.forEach(option => {
        opt = document.createElement('option');
        opt.value = option;
        opt.textContent = option;
        select.appendChild(opt);
    });
}

function loadRaceAndClassData() {
    // Here, define logic to calculate and display character data based on selections.
    const raceSelect = document.getElementById('raceSelect');
    const classSelect = document.getElementById('classSelect');
    
    let race, className;
    
    if (raceSelect.value === "Random") {
        race = getRandomOption(raceSelect);
    } else {
        race = raceSelect.value;
    }
    
    if (classSelect.value === "Random") {
        className = getRandomOption(classSelect);
    } else {
        className = classSelect.value;
    }
    
    // Display the selected race and class on the HTML page
    const characterOutput = document.getElementById('characterOutput');
    characterOutput.innerHTML = `<p>Class: ${className}, Race: ${race}</p>`;
}

function getRandomOption(select) {
    const options = select.options;
    const randomIndex = Math.floor(Math.random() * (options.length - 1)) + 1; // Exclude "Random" option
    return options[randomIndex].value;
}
