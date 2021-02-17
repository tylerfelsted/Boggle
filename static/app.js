const BASE_URL = 'http://localhost:5000'

const $guessForm = $("#guess-form");

$guessForm.on("submit", async function(evt) {
    evt.preventDefault();

    guess = $('#form-input').val()
    console.log(guess)

    const response = await axios.get(`${BASE_URL}/guess`, {
        params: {
            guess: guess
        }
    });

    console.log(response);
})