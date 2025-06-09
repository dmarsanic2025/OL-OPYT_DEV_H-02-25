// Dohvaćanje HTML elemenata pomoću njihovih ID-jeva
const taskInput = document.getElementById('task-input'); // polje za unos zadatka
const addTaskBtn = document.getElementById('add-task-btn'); // gumb "Dodaj zadatak"
const taskList = document.getElementById('task-list'); // <ul> element koji prikazuje sve zadatke
const remainingTasks = document.getElementById('remaining-tasks'); // prikaz broja nedovršenih zadataka

// Funkcija koja ažurira prikaz broja nedovršenih zadataka
function updateRemainingCount() {
  // Odabire sve <li> elemente koji NEMAJU klasu "completed"
  const total = document.querySelectorAll('#task-list li:not(.completed)').length;
  remainingTasks.textContent = `Preostalo zadataka: ${total}`;
}

// Funkcija za kreiranje jednog zadatka kao <li> element
function createTaskElement(taskText) {
  const li = document.createElement('li'); // novi <li> element
  li.textContent = taskText; // postavi tekst zadatka

  // Klikom na zadatak, mijenja se njegov status: dovršen ↔︎ nedovršen
  li.addEventListener('click', () => {
    li.classList.toggle('completed'); // dodaje/uklanja klasu "completed"
    updateRemainingCount(); // osvježava brojač
  });

  // Gumb za uklanjanje zadatka
  const removeBtn = document.createElement('button');
  removeBtn.textContent = 'Ukloni';
  removeBtn.className = 'remove-btn';

  // Klikom na gumb "Ukloni" briše se zadatak
  removeBtn.addEventListener('click', (e) => {
    e.stopPropagation(); // spriječi da klik označi zadatak kao dovršen
    li.remove(); // uklanja zadatak iz DOM-a
    updateRemainingCount(); // ažurira broj zadataka
  });

  li.appendChild(removeBtn); // dodaj gumb u <li>
  return li; // vrati cijeli <li> element
}

// Kad korisnik klikne na "Dodaj zadatak"
addTaskBtn.addEventListener('click', () => {
  const taskText = taskInput.value.trim(); // uzima i čisti unos

  // Provjera je li polje prazno
  if (taskText === '') {
    alert('Unesi neki zadatak!');
    return;
  }

  const taskElement = createTaskElement(taskText); // kreira novi zadatak
  taskList.appendChild(taskElement); // dodaje ga u listu
  taskInput.value = ''; // briše unos
  updateRemainingCount(); // ažurira broj preostalih zadataka
});

// Omogućuje dodavanje zadatka pritiskom na Enter tipku
taskInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    addTaskBtn.click(); // simulira klik na gumb
  }
});
