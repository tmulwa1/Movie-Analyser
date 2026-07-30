// Page selector dropdown
const pageSelect = document.getElementById('page-select')

if (pageSelect) {
    pageSelect.addEventListener('change', function() {
        const genreId = this.dataset.genreId;
        const selectedPage = this.value;
        window.location.href = `/discover/genre/${genreId}?page=${selectedPage}`;
    });
}

const cards = document.querySelectorAll('.movie-card');

if (cards.length > 0) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible'); // adds CSS class to an element
                observer.unobserve(entry.target); // once a card is in, stops tracking
            }
        });
    }, {threshold: 0.1 }); // triggers once 10% of the card is visible
    cards.forEach(card => observer.observe(card));
}