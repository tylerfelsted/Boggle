const BASE_URL = 'http://localhost:5000'

const $guessForm = $("#guess-form");
const $wordList = $("#word-list");
const $score = $("#score");

let score = 0;
$score.html(score);

$guessForm.on("submit", async function(evt) {
    evt.preventDefault();

    const word = $('#form-input').val()
    console.log(word)

    const response = await axios.get(`${BASE_URL}/guess`, {
        params: {
            guess: word
        }
    });

    if(response.data === 'ok') {
        $("<li>").html(word).appendTo($wordList);
        score += word.length;
    }

    $("#message").html(response.data);
    $score.html(score)
})