document.addEventListener("DOMContentLoaded", function () {
    // Example animation: Fade in the form container
    const formContainer = document.querySelector('.form-container');
    formContainer.style.opacity = 0;
    formContainer.style.transition = 'opacity 1s ease-in-out';

    setTimeout(() => {
        formContainer.style.opacity = 1;
    }, 100);

    // Additional animations or interactivity can be added here
});
