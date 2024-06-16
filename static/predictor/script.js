document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("eligibility-form");
    const modal = document.getElementById("result-modal");
    const closeModal = document.getElementById("close-modal");
    const resultMessage = document.getElementById("result-message");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken")
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.eligible) {
                resultMessage.textContent = " HOLA!! Our model predicted that you are eligible to donate blood.";
                resultMessage.style.color = "green";
            } else {
                resultMessage.textContent = "Oops!!For now you are not eligible to donate blood.";
                resultMessage.style.color = "red";
            }
            modal.style.display = "block";
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });

    closeModal.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
});
