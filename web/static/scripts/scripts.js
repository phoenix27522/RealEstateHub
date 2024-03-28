document.addEventListener('DOMContentLoaded', function() {
    // Fetch amenities
    fetch('/API/v1/amenities')
        .then(response => response.json())
        .then(data => {
            const amenitySelect = document.getElementById('amenity');
            data.forEach(amenity => {
                const option = document.createElement('option');
                option.value = amenity.id;
                option.textContent = amenity.name;
                amenitySelect.appendChild(option);
            });
        });

    // Fetch states
    fetch('/API/v1/states')
        .then(response => response.json())
        .then(data => {
            const stateSelect = document.getElementById('state');
            data.forEach(state => {
                const option = document.createElement('option');
                option.value = state.id;
                option.textContent = state.name;
                stateSelect.appendChild(option);
            });
        });

    // Handle form submission
   // Handle form submission
   document.getElementById('search-button').addEventListener('click', function() {
    const amenityId = document.getElementById('amenity').value;
    const stateId = document.getElementById('state').value;

    // Perform search based on selected amenity and state
    fetch('/API/v1/propertys_search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ amenityId, stateId })
    })
    .then(response => response.json())
    .then(data => {
        // Update the UI with search results
        // Example: You can render the properties in the properties-list div
        const propertiesList = document.getElementById('properties-list');
        propertiesList.innerHTML = ''; // Clear previous search results
        data.forEach(property => {
            const propertyElement = document.createElement('div');
            propertyElement.textContent = property.name; // Render property name, adjust as needed
            propertiesList.appendChild(propertyElement);
        });
    })
    .catch(error => {
        console.error('Error performing property search:', error);
    });
});
});