
├── index.html
├── style.css
└── script.js
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Flashcard Quiz App</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="container">
    <h1>Flashcard Quiz</h1>
    <div class="card" id="flashcard">
      <div class="front" id="question">Question goes here</div>
      <div class="back" id="answer">Answer goes here</div>
    </div>
    <div class="controls">
      <button onclick="prevCard()">Previous</button>
      <button onclick="flipCard()">Flip</button>
      <button onclick="nextCard()">Next</button>
    </div>
  </div>
  <script src="script.js"></script>
</body>
</html>
body {
  font-family: Arial, sans-serif;
  text-align: center;
  background: #f0f4f8;
  margin: 0;
  padding: 20px;
}

.container {
  max-width: 400px;
  margin: auto;
}

.card {
  background: #fff;
  border-radius: 10px;
  padding: 40px 20px;
  margin: 20px 0;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  cursor: pointer;
  perspective: 1000px;
}

.front, .back {
  font-size: 1.2em;
  transition: 0.5s;
}

.controls button {
  padding: 10px 20px;
  margin: 10px;
  font-size: 1em;
  cursor: pointer;
}