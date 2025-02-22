function wait_for(selector) {
  return new Promise(resolve => {
      if (document.querySelector(selector)) {
          return resolve(document.querySelector(selector));
      }

      const observer = new MutationObserver(mutations => {
          if (document.querySelector(selector)) {
              resolve(document.querySelector(selector));
              observer.disconnect();
          }
      });

      observer.observe(document.body, {
          childList: true,
          subtree: true,
      });
  });
}

function gradual_brighten(popup_container) {
  opacity = parseFloat(popup_container.style.opacity) + 0.01
  console.log(opacity);
  if (opacity >= 1.0) {
    gradual_brighten.opacity = 1.0;
    return;
  }
  popup_container.style.opacity = opacity
  setTimeout(() => {
    gradual_brighten(popup_container);
  }, 30);
}

let question = [
  {
    num: 1,
    title: "What is 5+5 ?",
    option: ["0", "10", "1", "25"],
    ans: "b"
  },
  {
    num: 2,
    title: "What is 5-5 ?",
    option: ["10", "1", "25", "0"],
    ans: "d"
  },
  {
    num: 3,
    title: "What is 5*5 ?",
    option: ["25", "0", "10", "1"],
    ans: "a"
  },
  {
    num: 4,
    title: "What is 5/5 ?",
    option: ["1", "0", "10", "25"],
    ans: "a"
  },
  {
    num: 5,
    title: "What is 6+6 ?",
    option: ["1", "12", "10", "25"],
    ans: "b"
  },
  {
    num: 6,
    title: "What is 6-6 ?",
    option: ["0", "1", "3", "2"],
    ans: "a"
  }
];

(async function(){
await wait_for('.question-box');

let abc = ["a", "b", "c", "d"];
let sum = 0;
let interval;
let opt;
let startBox = document.querySelector(".starter");
let container = document.querySelector(".container");
let queBox =  document.querySelector(".question-box");
let nextBtn = document.getElementById("next-btn");
let finishBtn = document.getElementById("finish-btn");
let timerDiv = document.querySelector(".timer");
let resultBox = document.querySelector(".result-box");
let index = 0;
const eachTime = 15;
let timeLimit = question.length * eachTime;
const fixedTime = timeLimit;
// start quiz
function startQuiz(starter) {
  startBox.classList.add("hide");
  container.classList.remove("hide");
  interval = setInterval(timer, 1000);
}
})();

async function video_ended() {
  const popup_container = document.createElement('div');
  popup_container.setAttribute('id', 'popup_container');
  popup_container.style.opacity = 0.0;
  popup_container.innerHTML = `
  <div class="wrapper">
    <header>
      <i class="bx bx-cookie"></i>
      <h2>Test Your Understanding!</h2>
    </header>

    <div class="data">
      <p>Play a small game to test your understanding of the video!</p>
    </div>

    <div class="buttons">
      <button class="button" id="acceptBtn">Play!</button>
      <button class="button" id="declineBtn">No Thanks</button>
    </div>
  </div>
  `;
  setTimeout( () => {
    gradual_brighten(popup_container);
  }, 30);
  
  document.body.appendChild(popup_container);
  (await wait_for('#declineBtn')).addEventListener('click', () => {
    popup_container.remove();
  });
  document.getElementById('acceptBtn').addEventListener('click', async () => {
  //   window.location.replace('http://127.0.0.1:8250/play_game?' + new URLSearchParams({ url: window.location.href }).toString());
  // 
    document.getElementById("popup_container").innerHTML = `<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400&family=Ubuntu:wght@300&display=swap");
            * {
              margin: 0;
              padding: 0;
              box-sizing: border-box;
              font-family: "Poppins", sans-serif;
              user-select: none;
            }
            ::-webkit-scrollbar {
              width: 0;
              height: 0;
            }
            body {
              position: relative;
              height: 99vh;
              display: flex;
              justify-content: center;
              align-items: center;
              /* background: linear-gradient(45deg, crimson, #0390c8); */
              background: #0083bb;
            }
            .starter {
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
              min-width: 400px;
              height: 200px;
              background-color: #eee;
              border-radius: 5px;
              box-shadow: 0 0 10px 5px #c1c1c120;
              padding: 0 10px;
              filter: drop-shadow(0px 0px 10px #e2f9ff8d);
            }
            .starter button {
              padding: 10px 20px;
              font-size: 1.7rem;
              border: none;
              border-radius: 3px;
              outline: none;
              background-color: #0091ff;
              cursor: pointer;
              box-shadow: 0 0 10px 5px #00000020;
            }
            .container {
              position: relative;
              display: flex;
              flex-direction: column;
              width: 450px;
              height: auto;
              background: #fff;
              border-radius: 5px;
              overflow: hidden;
              transition: 0.3s ease;
            }
            .container header {
              display: flex;
              justify-content: space-between;
              align-items: center;
              width: 100%;
              height: 65px;
              padding: 0 10px;
              box-shadow: 0 0 10px 2px #00000030;
              pointer-events: none;
            }
            .container header p {
              font-size: 1.7rem;
              font-weight: 600;
              letter-spacing: 4px;
            }
            .container header .timer {
              font-size: 1.2rem;
              font-weight: 600;
              background: #dc143ca1;
              padding: 5px 10px;
              color: #222;
              border-radius: 3px;
            }
            .container .question-box {
              display: flex;
              align-self: flex-start;
              padding: 15px 0;
              padding-bottom: 0;
              transition: transform 0.2s ease;
            }
            .question-box .section {
              width: 450px;
              padding: 0 1rem;
            }
            .question-box .section .title {
              font-family: "Ubuntu", sans-serif;
              font-weight: 600;
              font-size: 1.5rem;
              letter-spacing: 3px;
              margin-bottom: 1rem;
            }
            .question-box .section div {
              position: relative;
              display: flex;
              align-items: center;
              width: 100%;
              background: #5dbffc2a;
              border: 2px solid #005eff19;
              margin: 7px 0;
              padding: 10px;
              font-family: "Poppins", sans-serif;
              border-radius: 5px;
              cursor: pointer;
              transition: 0.3s ease;
            }
            .question-box .section div span {
              display: none;
              opacity: 0;
              pointer-events: none;
            }
            .question-box .section div i {
              position: absolute;
              right: 15px;
              height: 26px;
              width: 26px;
              border: 2px solid transparent;
              border-radius: 50%;
              text-align: center;
              font-size: 0.8rem;
              line-height: 1.4rem;
              pointer-events: none;
            }
            .question-box .section div i.fa-check {
              color: #23903c;
              border-color: #23903c;
              background: #d4edda;
            }
            .question-box .section div i.fa-times {
              color: #a42834;
              background: #f8d7da;
              border-color: #a42834;
            }
            .question-box .section div:hover {
              background: #cce5ff;
              color: #004085;
              border: 2px solid #b8daff;
            }
            .question-box .section div.selected {
              background: #009dff50;
              border: 2px solid #009dff50;
            }
            .question-box .section div.correct {
              background: #00ff0050;
              border: 2px solid #00ff0050;
            }
            .question-box .section div.wrong {
              background-color: #ff000030;
              border: 2px solid #ff000030;
            }
            .container footer {
              margin: 5px;
              margin-bottom: 10px;
              text-align: right;
            }
            .container footer button {
              padding: 7px 15px;
              background-color: #0091ff;
              color: #000;
              border: none;
              outline: none;
              border-radius: 3px;
              font-size: 1.1rem;
              font-weight: 600;
              margin: 0 10px;
              cursor: pointer;
            }
            .result-box {
              position: relative;
              display: flex;
              flex-direction: column;
              justify-content: center;
              align-items: center;
              width: 500px;
              background: #fff;
              border-radius: 5px;
              padding: 1rem 0;
              transition: 0.3s ease;
            }
            .result-box .num-div {
              display: flex;
              flex-wrap: wrap;
              font-size: 1.5rem;
              font-weight: 600;
              margin: 1rem;
            }
            .num-div p {
              color: blue;
              margin: 0 10px;
              font-weight: 1000;
            }
            
            .result-box button {
              background-color: #0091ff;
              color: #222;
              border: none;
              outline: none;
              border-radius: 3px;
              font-size: 1rem;
              font-weight: 1000;
              margin: 1rem 0.3rem;
              padding: 8px;
              cursor: pointer;
            }
            button {
              transition: 0.2s ease-out;
              letter-spacing: 1px;
            }
            button:hover {
              transform: scale(1.03);
              filter: brightness(1.2);
            }
            /* hide class */
            .hide {
              position: absolute;
              opacity: 0;
              pointer-events: none;
              transform: scale(0.9);
              transition: 0s;
              z-index: -999;
            }
            
            @media screen and (max-width: 430px) {
              body {
                padding: 0 10px;
              }
              .starter {
                min-width: auto;
                width: 100vw;
              }
              .container {
                width: 100vw;
              }
              .question-box .section {
                width: calc(100vw - 1.25rem);
              }
              .result-box {
                width: 100vw;
              }
            }
            </style>
        <title>Document</title>
    </head>
    <body>
        
            <div class="starter">
                <button onclick="startQuiz(this)">Start</button>
              </div>
              <div class="container hide">
                <header>
                  <p>Quiz</p>
                  <div class="timer"></div>
                </header>
                <div class="question-box"></div>
                <footer>
                  <button id="next-btn">Next</button>
                  <button id="finish-btn" class="hide">Finish</button>
                </footer>
              </div>
              <div class="result-box hide">
                <div class="num-div">
                  You have got
                  <p id="got-num"></p>
                  out of
                  <p id="total-num"></p>
                </div>
                <div class="button-box">
                  <button id="replay" onclick="resultShow()">See Reullt</button>
                  <button id="replay" onclick="replay()">Replay Quiz</button>
                </div>
              </div>
    </body>
    </html>`;
})
}
function replay() {
  sum = 0;
  index = 0;
  timeLimit = fixedTime;
  clearInterval(interval);
  interval = setInterval(timer, 1000);

  container.classList.remove("hide");
  resultBox.classList.add("hide");
  nextBtn.classList.remove("hide");
  finishBtn.classList.add("hide");
  queBox.style.transform = `translateX(0px)`;
  queBox.style.pointerEvents = "initial";
  queBox.querySelectorAll("div").forEach((opt2) => {
    opt2.classList.remove("selected", "correct", "wrong");
  });
  queBox.querySelectorAll(".ricon").forEach((ricon) => {
    ricon.remove();
  });
  queBox.querySelectorAll("input").forEach((input) => {
    input.value = "";
  });
}
function resultShow() {
  index = 0;
  sum = 0;
  container.classList.remove("hide");
  resultBox.classList.add("hide");
  nextBtn.classList.remove("hide");
  finishBtn.classList.remove("hide");
  queBox.style.transform = `translateX(0px)`;
  for (m = 0; m < question.length; m++) {
    section[m].querySelector(`#\${question[m].ans}`).classList.add("correct");
  }
  queBox.style.pointerEvents = "none";
}

function timer() {
  timeLimit--;
  min = (timeLimit / 60).toString().split(".")[0];
  sec = timeLimit % 60;
  if (min < 10) min = "0" + min;
  if (sec < 10) sec = "0" + sec;
  if (timeLimit == 0) {
    clearInterval(interval);
    nextBtn.classList.add("hide");
    finishBtn.classList.remove("hide");
    queBox.style.pointerEvents = "none";
  }
  timerDiv.innerHTML = min + " : " + sec;
}
async function main() {

for (i = 0; i < question.length; i++) {
  queBox.innerHTML += 
    `<div class='section' id='${question[i].num}'>` +
    `<p class='title'>${question[i].title}</p>` +
    `</div>`;
  let section = queBox.querySelectorAll(".section");
  for (k = 0; k < 4; k++) {
    section[
      i
    ].innerHTML += `<div id='\${abc[k]}'>(\${abc[k]}) \${question[i].option[k]}</div>`;
  }
}
section = queBox.querySelectorAll(".section");
section.forEach((section1) => {
  opt = section1.querySelectorAll("div");
  let input = document.createElement("input");
  input.hidden = true;
  input.readOnly = true;
  section1.appendChild(input);
  opt.forEach((opt1) => {
    opt1.onclick = (e) => {
      section1.querySelectorAll("div").forEach((optR) => {
        optR.classList.remove("selected");
      });
      opt1.classList.add("selected");
      input.value = e.target.id;
    };
  });
});

function increament() {
  index++;
  if (index < question.length) {
    queBox.style.transform = `translateX(\${-section[0].offsetWidth * index}px)`;
  }
  if (index == question.length - 1) {
    nextBtn.classList.add("hide");
    finishBtn.classList.remove("hide");
  }
}
nextBtn.onclick = () => {
  increament();
};

finishBtn.onclick = () => {
  clearInterval(interval);
  index = 0;
  container.classList.add("hide");
  resultBox.classList.remove("hide");
  for (j = 0; j < section.length; j++) {
    if (section[j].querySelector("input").value == question[j].ans) {
      sum++;
      section[j].querySelector(".selected").innerHTML +=
        "<i class='fa fa-check ricon'></i>";
    } else if (section[j].querySelector(".selected")) {
      section[j].querySelector(".selected").classList.add("wrong");
      section[j].querySelector(".selected").innerHTML +=
        "<i class='fa fa-times ricon'></i>";
    }
  }
  resultBox.querySelector("#got-num").innerHTML = sum;
  resultBox.querySelector("#total-num").innerHTML = question.length;
};

// timer start
let min = (timeLimit / 60).toString().split(".")[0];
let sec = timeLimit % 60;
if (min < 10) min = "0" + min;
if (sec < 10) sec = "0" + sec;
timerDiv.innerHTML = min + " : " + sec;

//timer end
document.onkeydown = (e) => {
  e.preventDefault();
  if (e.keyCode == 13 && index + 1 < question.length) {
    increament();
  }
};
window.onresize = () => {
  queBox.style.transform = `translateX(\${-section[0].offsetWidth * index}px)`;
};
window.oncontextmenu = (e) => {
  e.preventDefault();
};



}

main();


