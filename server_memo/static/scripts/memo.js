const cards = document.querySelectorAll('.memory-card');
var batton = $('#refresh')

 let hasFlippedCard = false;
 let lockBoard = false;
 let firstCard, secondCard, firstCardSource, secondCardSource;

 function flipCard(){
   if (lockBoard) return;
   if (this === firstCard) return;
   this.classList.add('flip');

   if (!hasFlippedCard) {
     hasFlippedCard = true;
     firstCard = this;
     firstCardSource = firstCard.firstChild.nextSibling.getAttribute('src');
   } else {
     hasFlippedCard = false;
     secondCard = this;
     secondCardSource = secondCard.firstChild.nextSibling.getAttribute('src');

     if (secondCardSource === firstCardSource) {
       firstCard.removeEventListener('click', flipCard);
       secondCard.removeEventListener('click', flipCard);
       console.log("It's a match!");
     } else {
       lockBoard = true;
       setTimeout(() => {
         firstCard.classList.remove('flip');
         secondCard.classList.remove('flip');
         lockBoard = false;
       }, 1500);

     }
   }
 }

 function reloadPage() {
   document.location.reload(true)
 }

batton.on('click', reloadPage)
cards.forEach(card => card.addEventListener('click', flipCard));
