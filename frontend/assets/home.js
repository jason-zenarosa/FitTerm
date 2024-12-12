function createActivityComponent(description, name, timestamp, completion) {
    // Create a container div to hold the paragraphs
    const container = document.createElement('div');
    container.classList.add('activity');

    // Create a paragraph for each input and set its text content
    const nameParagraph = document.createElement('p');
    nameParagraph.textContent = name;
    container.appendChild(nameParagraph);

    const descriptionParagraph = document.createElement('p');
    descriptionParagraph.textContent = description;
    container.appendChild(descriptionParagraph);

    const timestampParagraph = document.createElement('p');
    timestampParagraph.textContent = timestamp;
    container.appendChild(timestampParagraph);

    const completionParagraph = document.createElement('p');
    completionParagraph.textContent = completion === 'true' ? 'Complete' : 'Incomplete';
    container.appendChild(completionParagraph);

    // Return the container with all paragraphs
    return container;
}

fetch(`http://localhost:8080/get-activities?username=${sessionStorage.getItem('username')}`, {
    method: 'GET'
})
.then(response => response.json())
.then(data => {
    const activitiesContainer = document.querySelector('.activities-container');
    for (activity of data.activities) {
        const activityComponent = createActivityComponent(activity.description, activity.name, activity.timestamp, activity.completion);
        activitiesContainer.appendChild(activityComponent)
    }
});