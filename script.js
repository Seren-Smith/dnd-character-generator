document.addEventListener('DOMContentLoaded', function() {
    fetchDropdownData();

    // Fetching dropdown data from Lambda
    function fetchDropdownData() {
        axios.get('https://your_lambda_url')
            .then(function(response) {
                const data = response.data;
                populateDropdown('raceSelect', data.races);
                populateDropdown('classSelect', data.classes);
            })
            .catch(function(error) {
                console.error('Error fetching dropdown data:', error);
            });
    }

    // Helper function to populate dropdowns
    function populateDropdown(selectId, options) {
        const select = document.getElementById(selectId);
        options.forEach(option => {
            let opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option;
            select.appendChild(opt);
        });
    }
});

function loadRaceAndClassData() {
    const race = document.getElementById('raceSelect').value;
    const className = document.getElementById('classSelect').value;
    if (race && className) {
        axios.get('https://your_lambda_url_with_params', {
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
            document.getElementById('characterOutput').innerHTML = output;
        })
        .catch(function (error) {
            console.error('Error:', error);
            document.getElementById('characterOutput').innerHTML = `<p>Error loading character data. Please try again.</p>`;
        });
    } else {
        document.getElementById('characterOutput').innerHTML = `<p>Please select both a race and a class to see details.</p>`;
    }
}
