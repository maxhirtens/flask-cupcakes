const api = "http://127.0.0.1:5000/api";

function makeCupcakeHTML(cupcake) {
  return `<div>
  <img class='cupcake-img' src=${cupcake.image}>
  <li>${cupcake.flavor} - ${cupcake.size} - ${cupcake.rating}</li>
  </div>
  `;
}

async function showCupcakes() {
  const response = await axios.get(`${api}/cupcakes`);
  for (let cupcake of response.data.cupcakes) {
    let newCupcake = makeCupcakeHTML(cupcake);
    $(".cupcake-list").append(newCupcake);
  }
}

$(".get-cupcake-btn").on("click", function () {
  showCupcakes();
  $(".cupcake-list").empty();
});

$(".add-cupcake-btn").on("click", async function (evt) {
  evt.preventDefault();
  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image = $("#image").val();
  const newCupcakeResponse = await axios.post(`${api}/cupcakes`, {
    flavor,
    size,
    rating,
    image,
  });
  newCupcake = makeCupcakeHTML(newCupcakeResponse.data.cupcake);
  $(".cupcake-list").append(newCupcake);
  document.querySelector(".add-cupcake-form").reset();
});
