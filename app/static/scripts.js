
//// MOBILE NAVBAR ///////

function toggleNavbar() {
    var navbarItems = document.getElementById('navbar_items');
    if (navbarItems.classList.contains('show')) {
        navbarItems.classList.remove('show');
        navbarItems.classList.add('hide');
    } else {
        navbarItems.classList.remove('hide');
        navbarItems.classList.add('show');
    }
}

document.addEventListener('click', function(event) {
    var navbarItems = document.getElementById('navbar_items');
    var hamburgerMenu = document.getElementById('hamburger_menu');

    if (!navbarItems.contains(event.target) && !hamburgerMenu.contains(event.target)) {
        navbarItems.classList.remove('show');
        navbarItems.classList.add('hide');
    }
});


///////////////////////////////



document.addEventListener("DOMContentLoaded", function () {
    
    // const video = document.querySelector('video').playbackRate = 0.5;
    const sections = document.querySelectorAll("section");

    const options = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("in-view");
                observer.unobserve(entry.target);
            }
        });
    }, options);

    sections.forEach(section => {
        observer.observe(section);
    });
});


// HOME PAGE FADE IN BANNER TEXT
document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll('#home_page_banner_text .content');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target); // Stop observing once the animation is triggered
            }
        });
    }, {
        threshold: 0.1 // Trigger when 10% of the element is visible
    });

    sections.forEach(section => {
        observer.observe(section);
    });
});



// // CAROUSEL
// const carouselSlide = document.getElementById('carouselSlide');
// const images = carouselSlide.getElementsByTagName('img');
// const totalImages = images.length;
// let counter = 0;

// document.getElementById('nextBtn').addEventListener('click', () => {
//     if (counter >= totalImages - 1) {
//         counter = 0;
//     } else {
//         counter++;
//     }
//     updateCarousel();
//     updateMainImage(images[counter].src);
// });

// document.getElementById('prevBtn').addEventListener('click', () => {
//     if (counter <= 0) {
//         counter = totalImages - 1;
//     } else {
//         counter--;
//     }
//     updateCarousel();
//     updateMainImage(images[counter].src);
// });

// function updateCarousel() {
//     const size = images[0].clientWidth;
//     carouselSlide.style.transform = `translateX(${-size * counter}px)`;
// }

// function updateMainImage(src) {
//     document.getElementById('mainImage').src = src;
// }


let currentIndex = 0;
const itemsToShow = 5;

function scrollCarousel(direction) {
    const container = document.querySelector('.carousel-container');
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;

    currentIndex += direction * itemsToShow;

    if (currentIndex < 0) {
        currentIndex = 0;
    } else if (currentIndex >= totalItems) {
        currentIndex = totalItems - itemsToShow;
    }

    const translateX = -currentIndex * 20; // Move by 20% for each image
    container.style.transform = `translateX(${translateX}%)`;
}

function changeMainImage(newSrc) {
    const mainImage = document.getElementById('mainImage');
    mainImage.src = newSrc;
}


// function changeMainImage(newSrc) {
//     const mainImage = document.getElementById('mainImage');
    
//     // Log the newSrc to ensure it’s correct
//     console.log('Changing main image to:', newSrc);
    
//     if (mainImage) {
//         mainImage.src = newSrc;
//     } else {
//         console.error('Main image element not found');
//     }
// }


// ////////////////////////////// GOOGLE MAPS JAVA SCRIPT FOR FILTERING //////////////////////////////////


document.addEventListener('DOMContentLoaded', function () {
    // Toggle filter visibility
    document.getElementById('filter-button').addEventListener('click', function() {
        const filters = document.getElementById('filters');
        if (filters.classList.contains('filters-visible')) {
            filters.classList.remove('filters-visible');
            this.textContent = 'Show Filters';
        } else {
            filters.classList.add('filters-visible');
            this.textContent = 'Hide Filters';
        }
    });

    // Apply filters and hide filter options
    window.applyFilters = function() {
        const minPrice = parseFloat(document.getElementById('min-price').value) || 0;
        const maxPrice = parseFloat(document.getElementById('max-price').value) || Infinity;
        const minBeds = parseInt(document.getElementById('min-beds').value) || 0;
        const minBaths = parseFloat(document.getElementById('min-baths').value) || 0;

        const propertyItems = document.querySelectorAll('.property-item');

        propertyItems.forEach(item => {
            const price = parseFloat(item.getAttribute('data-price'));
            const beds = parseInt(item.getAttribute('data-beds'));
            const fullBaths = parseFloat(item.getAttribute('data-full-baths'));
            const halfBaths = parseFloat(item.getAttribute('data-half-baths'));

            let baths = 0;
            if (halfBaths > 1) {
                baths = fullBaths + (halfBaths / 2);
            } else if (halfBaths > 0) {
                baths = fullBaths + (halfBaths / 2);
            } else {
                baths = fullBaths;
            }

            if (price >= minPrice && price <= maxPrice &&
                beds >= minBeds &&
                baths >= minBaths) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });

        // Hide filters after applying
        document.getElementById('filters').classList.remove('filters-visible');
        document.getElementById('filter-button').textContent = 'Show Filters';
    };
});












