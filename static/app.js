const BASE_URL = 'http://localhost:5000'

const $guessForm = $("#guess-form");
const $wordList = $("#word-list");
const $score = $("#score");
const $timer = $("#timer");

let score = 0;
let timeRunOut = false;
let timeLeft = 60;
let wordList = new Set();
$score.html(score);
$timer.html(timeLeft);

$guessForm.on("submit", async function(evt) {
    evt.preventDefault();

    if(timeRunOut){

    } else {
        const word = $('#form-input').val()

        const response = await axios.get(`${BASE_URL}/guess`, {
            params: {
                guess: word
            }
        });

        if(response.data === 'ok' && !wordList.has(word)) {
            $("<li>").html(word).appendTo($wordList);
            score += word.length;
            wordList.add(word);
        }

        $("#message").html(response.data);
        $score.html(score)
    }

    
})

const gameTimer = setInterval(async function() {   
    timeLeft--;    
    $timer.html(timeLeft);

    if(timeLeft === 0){
        clearInterval(gameTimer)
        console.log("Time's Up!")
        timeRunOut = true;
        const data = {score: score}
        let res = await axios.post(`${BASE_URL}/game-over`, data)
        console.log(res)
    }
}, 1000);