
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


////////////////////// CAROUSEL //////////////////////////////////////

let currentSlide = 0;
const itemsPerPage = 1 // Number of images to show per view

function moveCarousel(direction) {
    const items = document.querySelectorAll('.grid-item');
    const totalSlides = Math.ceil(items.length / itemsPerPage); // Total number of slides based on items per page

    // Update the current slide index
    currentSlide += direction;

    // Loop the carousel
    if (currentSlide < 0) {
        currentSlide = totalSlides -1; // Prevent going to negative slide index
    } else if (currentSlide >=totalSlides) {
        currentSlide = 0; // Prevent going beyond the last slide
    }

    // Move the carousel
    const carouselInner = document.querySelector('.carousel-inner');
    const offset = -currentSlide * (itemsPerPage * (100 / itemsPerPage)); // Calculate offset based on itemsPerPage
    carouselInner.style.transform = `translateX(${offset}%)`;
}


let currentCarouselSlide = currentSlide;
const carouselItemsPerPage = 5// Number of images to show per view

function moveCarouselSlider(direction) {
    const items = document.querySelectorAll('.grid-item-scroll');
    const totalSlides = Math.ceil(items.length / carouselItemsPerPage); // Total number of slides based on items per page

    // Update the current slide index
    currentCarouselSlide += direction;

    // Loop the carousel
    if (currentCarouselSlide < 0) {
        currentCarouselSlide = totalSlides -1; // Prevent going to negative slide index
    } else if (currentCarouselSlide >= totalSlides) {
        currentCarouselSlide = 0; // Prevent going beyond the last slide
    }

    // Move the carousel
    const carouselInner = document.querySelector('.carousel-inner-scroll');
    const offset = -currentCarouselSlide * (carouselItemsPerPage * (100 / carouselItemsPerPage)); // Calculate offset based on itemsPerPage
    carouselInner.style.transform = `translateX(${offset}%)`;
}

function changeMainImage(imageUrl) {
    document.getElementById("mainImage").src = imageUrl;
  }


////////////////////// MORTGAGE CALCULATOR ///////////////////////////////
function calculateMortgage(loanAmount, interestRate, loanTerm) {
    const monthlyRate = interestRate / 100 / 12; // Monthly interest rate
    const totalMonths = loanTerm * 12; // Total loan term in months

    const monthlyPayment = (loanAmount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -totalMonths));

    return monthlyPayment;
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('mortgage-form');

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const loanAmount = parseFloat(document.getElementById('loanAmount').value);
            const downPaymentPercentage = parseFloat(document.getElementById('downPaymentPercentage').value);
            const interestRate = parseFloat(document.getElementById('interestRate').value);
            const loanTerm = parseInt(document.getElementById('loanTerm').value);

            // Calculate the actual loan amount after the down payment
            const downPaymentAmount = loanAmount * (downPaymentPercentage / 100);
            const effectiveLoanAmount = loanAmount - downPaymentAmount;

            const monthlyPayment = calculateMortgage(effectiveLoanAmount, interestRate, loanTerm);
            
            if (!isNaN(monthlyPayment) && (monthlyPayment !== Infinity) && (monthlyPayment > 0)) {
                document.getElementById('monthlyPayment').innerText = `Monthly Payment: $${monthlyPayment.toFixed(2)}`;
            } else {
                document.getElementById('monthlyPayment').innerText = 'Please enter valid values';
            }
        });
    }
});



// ////////////////////////////// GOOGLE MAPS JAVA SCRIPT FOR FILTERING //////////////////////////////////

document.addEventListener('DOMContentLoaded', function () {
    // Toggle filter visibility
    document.getElementById('filter-button').addEventListener('click', function () {
        const filters = document.getElementById('filters');
        filters.classList.toggle('filters-visible');
        this.textContent = filters.classList.contains('filters-visible') ? 'Hide Filters' : 'Show Filters';
    });

    window.applyFilters = function () {
        const mlsId = document.getElementById('mls-listing-id').value.trim();
        const location = document.getElementById('location').value.trim();
        const minPrice = document.getElementById('min-price').value.trim();
        const maxPrice = document.getElementById('max-price').value.trim();
        const minBeds = document.getElementById('min-beds').value.trim();
        const minBaths = document.getElementById('min-baths').value.trim();

        // Send AJAX request
        const url = `/filter-properties?mls_listing_id=${mlsId}&location=${location}&min_price=${minPrice}&max_price=${maxPrice}&min_beds=${minBeds}&min_baths=${minBaths}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const propertyList = document.getElementById('property-list');
                propertyList.innerHTML = '';  // Clear current list

                // Update property list
                data.properties.forEach(property => {
                    const formattedPrice = parseFloat(property.list_price).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
                    const beds = property.bedrooms || 'N/A';
                    const baths = property.baths_total || 'N/A';
                    const sqFt = property.building_area_total ? `${property.building_area_total.toLocaleString()} Sq. Ft.` : 'N/A';

                    const propertyItem = `
                        <a href="/property/${property.id}" class="property-link">
                            <div class="property-item">
                                <div class="property-image">
                                    <img src="${property.image_url}" alt="Property Image">
                                </div>
                                <h2>${property.house_number || ''} ${property.street_name}, ${property.city}, ${property.state} ${property.postal_code}</h2>
                                <div class="property-details">
                                    <h3>${formattedPrice}</h3>
                                    <p>${beds} Beds &nbsp; | &nbsp; ${baths} Baths &nbsp; | &nbsp; ${sqFt}</p>
                                    <p>${property.property_type || 'N/A'}</p>
                                    <p class="agent-info">${property.agent_name || 'N/A'}</p>
                                    <a href="#" onclick="moveToProperty(${property.latitude}, ${property.longitude})">View on Map</a>
                                </div>
                            </div>
                        </a>
                    `;
                    propertyList.insertAdjacentHTML('beforeend', propertyItem);
                });

                // Update the map with new markers
                updateMap(data.properties);

                // Close the filters form after applying filters
                const filters = document.getElementById('filters'); // Adjust this ID if needed
                if (filters.classList.contains('filters-visible')) {
                    filters.classList.remove('filters-visible'); // Hide the filter form
                    document.getElementById('filter-button').textContent = 'Show Filters'; // Reset button text
                }
            })
            .catch(error => {
                console.error('Error filtering properties:', error);
            });
    };

    function updateMap(properties) {
        // Clear existing markers
        windowsOpen.forEach(window => window.close());
        windowsOpen = [];
        map.markers.forEach(marker => marker.setMap(null));  // Remove existing markers
        map.markers = [];

        // Add new markers to the map
        properties.forEach(property => {
            if (!isNaN(property.latitude) && !isNaN(property.longitude)) {
                const priceMarkerDiv = document.createElement('div');
                priceMarkerDiv.className = 'price-marker';
                priceMarkerDiv.innerHTML = `$${property.list_price}`;

                const marker = new google.maps.Marker({
                    position: new google.maps.LatLng(property.latitude, property.longitude),
                    map: map,
                    title: property.house_number + ' ' + property.street_name
                });

                map.markers.push(marker);

                const infoWindowContent = `
                    <div class="map-popup">
                        <h3 class="popup-title"><a href="/property/${property.id}">${property.house_number} ${property.street_name}, ${property.city}, ${property.state}</a></h3>
                        <p class="popup-price">Price: $${property.list_price}</p>
                    </div>
                `;

                const infoWindow = new google.maps.InfoWindow({
                    content: infoWindowContent
                });

                marker.addListener('click', () => {
                    windowsOpen.forEach(win => win.close());
                    infoWindow.open(map, marker);
                    windowsOpen.push(infoWindow);
                });
            }
        });
    }

    window.moveToProperty = function (lat, lng) {
        map.setCenter({ lat: lat, lng: lng });
        map.setZoom(15);
    };
});



// Get commas in infowindow on maps for price, REGEX is dumb
function formatPriceWithCommas(price) {
    return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }

  function toggleDescription(id) {
    var desc = document.getElementById(id);
    var allDescriptions = document.querySelectorAll('.team-description');

    allDescriptions.forEach(function(description) {
        description.style.display = 'none';
    });

    if (desc.style.display === 'none' || desc.style.display === '') {
        desc.style.display = 'block';
    } else {
        desc.style.display = 'none';
    }
}

function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to add the 'visible' class to portraits when they are in the viewport
function handleScroll() {
    const portraits = document.querySelectorAll('.portrait');
    portraits.forEach(function(portrait) {
        if (isElementInViewport(portrait)) {
            portrait.classList.add('visible');
        }
    });
}

// Listen for scroll events
window.addEventListener('scroll', handleScroll);

// Initial check when the page loads
window.addEventListener('load', handleScroll);




let currentPage = 0;
const propertiesPerPage = 3;

document.addEventListener('DOMContentLoaded', () => {
  showProperties(currentPage);

  document.getElementById('next-button').addEventListener('click', nextPage);
  document.getElementById('prev-button').addEventListener('click', prevPage);
});

function showProperties(page) {
  const allProperties = document.querySelectorAll('.property-item');
  const totalPages = Math.ceil(allProperties.length / propertiesPerPage);
  
  allProperties.forEach((property, index) => {
    if (index >= page * propertiesPerPage && index < (page + 1) * propertiesPerPage) {
      property.style.display = 'block'; // Show the properties for the current page
    } else {
      property.style.display = 'none'; // Hide the rest
    }
  });

  // Disable buttons at the edges
  document.getElementById('prev-button').disabled = page === 0;
  document.getElementById('next-button').disabled = page >= totalPages - 1;
}

function nextPage() {
  const allProperties = document.querySelectorAll('.property-item');
  const totalPages = Math.ceil(allProperties.length / propertiesPerPage);
  
  if (currentPage < totalPages - 1) {
    currentPage++;
    showProperties(currentPage);
  }
}

function prevPage() {
  if (currentPage > 0) {
    currentPage--;
    showProperties(currentPage);
  }
}



// Property detail collapsible functions

function toggleCollapse(element) {
    const content = element.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  }
  
  // Optional: Hide collapsible content by default
  document.querySelectorAll('.content').forEach(content => {
    content.style.display = "none";
  });


  