const navbar = document.getElementById('navbar');
if (navbar) {
  const anchorLinks = navbar.querySelectorAll('a');

  // Function to show the navbar
  function showNavbar() {
    clearTimeout(hideTimeout); // Clear any pending hide action
    navbar.classList.remove('translate-y-0', 'opacity-10');
    navbar.classList.add('-translate-y-14', 'opacity-100');
  }

  // Function to hide the navbar with a delay
  function hideNavbarWithDelay() {
    hideTimeout = setTimeout(() => {
      navbar.classList.remove('-translate-y-14', 'opacity-100');
      navbar.classList.add('translate-y-0', 'opacity-10');
    }, 5000); // 2000ms = 2 seconds
  }

  // Add event listeners to show and hide the navbar
  navbar.addEventListener('mouseenter', showNavbar);
  navbar.addEventListener('mouseleave', hideNavbarWithDelay);

  // Also apply to the <a> elements within the navbar
  anchorLinks.forEach(anchor => {
    anchor.addEventListener('mouseenter', showNavbar);
    anchor.addEventListener('mouseleave', hideNavbarWithDelay);
  });
}