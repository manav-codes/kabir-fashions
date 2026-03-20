/* ================================
   Scroll Reveal Animation
   Lightweight IntersectionObserver-based
   fade-in for elements with .reveal class
   ================================ */

(function () {
  'use strict';

  // Bail out if IntersectionObserver is not supported
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal').forEach(function (el) {
      el.classList.add('is-visible');
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target); // animate once
        }
      });
    },
    {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    }
  );

  // Observe all .reveal elements once DOM is ready
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.reveal').forEach(function (el) {
      observer.observe(el);
    });
  });
})();
