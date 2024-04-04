const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};
document.addEventListener('DOMContentLoaded', function() {
  const scrollRevealOption = {
      distance: "50px",
      origin: "bottom",
      duration: 1000,
  };

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
          // Clear existing swiper slides
          swiper.removeAllSlides();

          // Loop through search results and create swiper slides
          data.forEach(property => {
              const swiperSlide = document.createElement('div');
              swiperSlide.classList.add('swiper-slide');
              swiperSlide.innerHTML = `
              <div class="property__card">
                <h4>${property.name}</h4>
                <p>
                  Amenity: ${property.amenity},
                  State: ${property.state}
                </p>
                <img src="${property.image_path}" alt="Property Image">
              </div>
              `;
              swiper.appendSlide(swiperSlide);
          });
      })
      .catch(error => {
          console.error('Error performing property search:', error);
      });
  });

  // Additional code for ScrollReveal initialization and configuration
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
})