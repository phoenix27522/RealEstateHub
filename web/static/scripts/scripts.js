const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};

document.addEventListener('DOMContentLoaded', function () {
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
  document.getElementById('search-button').addEventListener('click', function () {
    const amenityId = document.getElementById('amenity').value; // Assuming you're getting the amenity ID
    const stateId = document.getElementById('state').value;

    // Perform search based on selected amenity and state
    fetch('/API/v1/propertys_search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ amenities: [amenityId], states: [stateId] }) // Construct an object with an array of amenity IDs
    })
      .then(response => response.json())
      .then(data => {
        // Clear existing swiper slides
        swiper.removeAllSlides();

        // Loop through search results and create swiper slides
        data.forEach(property => {
          const swiperSlide = document.createElement('div');
          swiperSlide.classList.add('swiper-slide');
          swiperSlide.innerHTML = `
              <div class="property__card">
                  <img src="${property.image_path}" alt="Property Image">
                  <div class="property__content">
                      <h4>${property.name}</h4>
                      <p>
                          Price: ${property.price},<br>
                          Description: ${property.description},<br>
                          Number of Rooms: ${property.number_rooms},<br>
                          Number of Bathrooms: ${property.number_bathrooms}
                      </p>
                      <button class="book-now-btn" data-property-id="${property.id}">Book Now</button>
                  </div>
              </div>
          `;
          swiper.appendSlide(swiperSlide);
        });

        // Add event listener to the dynamically created "Book Now" buttons
        document.querySelectorAll('.book-now-btn').forEach(button => {
          button.addEventListener('click', function () {
            const propertyId = button.getAttribute('data-property-id');
            const descriptionTextArea = document.getElementById('description');
            // Populate description box with property ID
            descriptionTextArea.value = `Property ID: ${propertyId}\n\n`;
            // Scroll to the contact section
            document.getElementById('contact').scrollIntoView({ behavior: 'smooth' });
          });
        });

      })
      .catch(error => {
        console.error('Error performing property search:', error);
      });
  });

  document.getElementById('contact-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior
    
    // Get form data
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const email = document.getElementById('email').value;
    const phoneNumber = document.getElementById('phone_number').value;
    const description = document.getElementById('description').value;

    // Send email
    fetch('/API/v1/send-email', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        firstName,
        lastName,
        email,
        phoneNumber,
        description
      })
    })
    .then(response => {
      if (response.ok) {
        console.log('Email sent successfully');
        alert('Your message has been sent successfully!');
      } else {
        console.error('Error sending email:', response.statusText);
        alert('Sorry, there was an error sending your message. Please try again later.');
      }
    })
    .catch(error => {
      console.error('Error sending email:', error);
      alert('Sorry, there was an error sending your message. Please try again later.');
    });
  });
});

// header container
ScrollReveal().reveal(".header__container img", {
  duration: 1000,
});

ScrollReveal().reveal(".header__container h1", {
  ...scrollRevealOption,
  delay: 500,
});

ScrollReveal().reveal(".header__container p", {
  ...scrollRevealOption,
  delay: 1000,
});

ScrollReveal().reveal(".header__btns", {
  ...scrollRevealOption,
  delay: 1500,
});

// about container
ScrollReveal().reveal(".about__image img", {
  ...scrollRevealOption,
  origin: "left",
});

ScrollReveal().reveal(".about__content h3", {
  ...scrollRevealOption,
  delay: 500,
});

ScrollReveal().reveal(".about__content .section__header", {
  ...scrollRevealOption,
  delay: 1000,
});

ScrollReveal().reveal(".about__content .section__subheader", {
  ...scrollRevealOption,
  delay: 1500,
});

ScrollReveal().reveal(".about__content .about__grid", {
  ...scrollRevealOption,
  delay: 2000,
});

// contact container
ScrollReveal().reveal(".contact__image img", {
  ...scrollRevealOption,
  origin: "left",
});

const swiper = new Swiper(".swiper", {
  loop: true,
  slidesPerView: "auto",
  centeredSlides: true,
  spaceBetween: 30,
});
