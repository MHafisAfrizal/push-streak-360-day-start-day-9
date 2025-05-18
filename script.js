document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/api/testimonials")
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("testimonial-container");
      data.testimonials.forEach(testi => {
        const card = document.createElement("div");
        card.className = "testimonial-card";
        card.innerHTML = `
          <img src="${testi.avatar}" alt="${testi.name}" />
          <h4>${testi.name}</h4>
          <p>"${testi.message}"</p>
        `;
        container.appendChild(card);
      });
    })
    .catch(err => console.error("Gagal load testimoni:", err));
});
