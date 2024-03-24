document.addEventListener('DOMContentLoaded', function() {
    const clientsLink = document.querySelector('#sidebar ul li:first-child a');
    const contentContainer = document.getElementById('content-container');

    clientsLink.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent the default link behavior

        // Corrected fetch URL to match the Django URL pattern for the clients view
        fetch('/clients/')
            .then(response => {
                // Check if the request was successful
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(html => {
                contentContainer.innerHTML = html;
            })
            .catch(error => {
                console.error('Error loading clients content:', error);
                // Optionally update the contentContainer or log to inform the user
                contentContainer.innerHTML = '<p>Error loading content. Please try again later.</p>';
            });
    });
});
