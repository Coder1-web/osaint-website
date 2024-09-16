document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const ip = document.getElementById('ipInput').value;
    const resultsDiv = document.getElementById('results');
    
    resultsDiv.innerHTML = 'Searching...';

    try {
        const response = await fetch(`/host_info?ip=${ip}`);
        
        if (response.ok) {
            const data = await response.json();
            
            if (data.error) {
                resultsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                resultsDiv.innerHTML = `
                    <h3>Results for IP: ${data.ip}</h3>
                    <p><strong>Hostname:</strong> ${data.hostname}</p>
                    <p><strong>City:</strong> ${data.city}</p>
                    <p><strong>Region:</strong> ${data.region}</p>
                    <p><strong>Country:</strong> ${data.country}</p>
                    <p><strong>Location:</strong> ${data.loc}</p>
                `;
            }
        } else {
            const text = await response.text();
            resultsDiv.innerHTML = `<p>An error occurred: ${text}</p>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<p>An error occurred: ${error.message}</p>`;
    }
});
