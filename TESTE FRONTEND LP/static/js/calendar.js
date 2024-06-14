document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        dateClick: function(info) {
            var dateStr = info.dateStr;
            var modalHtml = `
                <div id="modal" class="modal">
                    <div class="modal-content">
                        <span class="close">&times;</span>
                        <h2>Escolha uma ação para ${dateStr}</h2>
                        <button id="agendarAula">Agendar Aula</button>
                        <button id="visualizarAula">Visualizar Aula</button>
                    </div>
                </div>`;
            document.body.insertAdjacentHTML('beforeend', modalHtml);
            
            var modal = document.getElementById('modal');
            var span = document.getElementsByClassName('close')[0];
            var agendarBtn = document.getElementById('agendarAula');
            var visualizarBtn = document.getElementById('visualizarAula');
            
            modal.style.display = "block";

            span.onclick = function() {
                modal.remove();
            }

            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.remove();
                }
            }

            agendarBtn.onclick = function() {
                alert('Aula agendada');
                calendar.addEvent({
                    title: 'Aula Agendada',
                    start: dateStr,
                    allDay: true
                });
                modal.remove();
            }

            visualizarBtn.onclick = function() {
                alert('Visualizando aula para ' + dateStr);
                modal.remove();
            }
        }
    });
    calendar.render();
});
