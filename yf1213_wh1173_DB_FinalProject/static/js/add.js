var flight = document.getElementById('flight');
var state = document.getElementById('state');
var airplane = document.getElementById('airplane');
var airport = document.getElementById('airport');
var flight_wrapper = document.getElementById('flight_wrapper');
var status_wrapper = document.getElementById('status_wrapper');
var airplane_wrapper = document.getElementById('airplane_wrapper');
var airport_wrapper = document.getElementById('airport_wrapper');

flight.addEventListener("input",()=>{
  if (flight.checked) {
    status_wrapper.style.visibility="hidden";
    airplane_wrapper.style.visibility="hidden";
    airport_wrapper.style.visibility="hidden";
    flight_wrapper.style.visibility="visible";
  }
})
state.addEventListener("input",()=>{
  if(state.checked){
    flight_wrapper.style.visibility="hidden";
    status_wrapper.style.visibility="visible";
    airport_wrapper.style.visibility="hidden";
    airplane_wrapper.style.visibility="hidden";
  }
})
airplane.addEventListener("input",()=>{
  if(airplane.checked){
    flight_wrapper.style.visibility="hidden";
    status_wrapper.style.visibility="hidden";
    airport_wrapper.style.visibility="hidden";
    airplane_wrapper.style.visibility="visible";
  }
})
airport.addEventListener("input",()=>{
  if(airport.checked){
    flight_wrapper.style.visibility="hidden";
    status_wrapper.style.visibility="hidden";
    airplane_wrapper.style.visibility="hidden";
    airport_wrapper.style.visibility="visible";
  }
})
