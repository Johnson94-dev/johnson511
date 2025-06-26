const flashcards = [
  { question: "What is the capital of France?", answer: "Paris" },
  { question: "2 + 2?", answer: "4" },
  { question: "Who wrote 'Hamlet'?", answer: "William Shakespeare" },
];

let currentCard = 0;
let flipped = false;

const questionEl = document.getElementById("question");
const answerEl = document.getElementById("answer");
const flashcard = document.getElementById("flashcard");

function showCard(index) {
  const card = flashcards[index];
  questionEl.textContent = card.question;
  answerEl.textContent = card.answer;
  answerEl.style.display = "none";
  questionEl.style.display = "block";
  flipped = false;
}

function flipCard() {
  if (!flipped) {
    questionEl.style.display = "none";
    answerEl.style.display = "block";
  } else {
    questionEl.style.display = "block";
    answerEl.style.display = "none";
  }
  flipped = !flipped;
}

function nextCard() {
  currentCard = (currentCard + 1) % flashcards.length;
  showCard(currentCard);
}

function prevCard() {
  currentCard = (currentCard - 1 + flashcards.length) % flashcards.length;
  showCard(currentCard);
}

// Initialize
showCard(currentCard);