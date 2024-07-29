document.addEventListener('DOMContentLoaded', () => {
    const personForm = document.getElementById('person-form');
    const searchInput = document.getElementById('search');
    const personList = document.getElementById('person-list');

    let people = [];

    const apiUrl = 'http://localhost:8080';

    // Fetch existing people from the backend
    fetch(`${apiUrl}/people/listAll`)
        .then(response => response.json())
        .then(data => {
            people = data;
            renderPeople(people);
        })
        .catch(error => {
            console.error('Error fetching people:', error);
        });

    personForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;
        const job = document.getElementById('job').value;

        const newPerson = { name, age, job };

        // Send new person data to the backend
        fetch(`${apiUrl}/api/people/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newPerson)
        })
            .then(response => response.json())
            .then(person => {
                people.push(person);
                renderPeople(people);
                personForm.reset();
            })
            .catch(error => {
                console.error('Error adding person:', error);
            });
    });

    searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.toLowerCase();
        const filteredPeople = people.filter(person =>
            person.name.toLowerCase().includes(searchTerm) ||
            person.job.toLowerCase().includes(searchTerm)
        );
        renderPeople(filteredPeople);
    });

    function renderPeople(people) {
        personList.innerHTML = '';
        if (people.length === 0) {
            personList.innerHTML = '<p>No people found.</p>';
            return;
        }
        people.forEach(person => {
            const personDiv = document.createElement('div');
            personDiv.className = 'pa3 ba b--black-10 mb2';
            personDiv.innerHTML = `
                <p><strong>Name:</strong> ${person.name}</p>
                <p><strong>Age:</strong> ${person.age}</p>
                <p><strong>Job:</strong> ${person.job}</p>
            `;
            personList.appendChild(personDiv);
        });
    }
});