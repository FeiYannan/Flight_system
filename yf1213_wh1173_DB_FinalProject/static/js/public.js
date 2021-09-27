// var username = document.getElementById('username');
// username.innerHTML = "Molly"

var search_state = document.getElementById('search_state');
var flight_state = document.getElementById('flight_state')
var search_flight = document.getElementById('search_flight');
var flight_status = document.getElementById('flight_status')

search_state.addEventListener("input",()=>{
  if (search_state.checked) {
    flight_status.style.visibility="hidden";
    search_flight.style.visibility="visible";
    city.style.visibility="visible";
  }
})
flight_state.addEventListener("input",()=>{
  if(flight_state.checked){
    search_flight.style.visibility="hidden";
    flight_status.style.visibility="visible";
    airport.style.visibility="hidden";
    city.style.visibility="hidden";

  }
})

var city_radio = document.getElementById('city_radio');
var airport_radio = document.getElementById('airport_radio')
var city = document.getElementById('city');
var airport = document.getElementById('airport')

city_radio.addEventListener("input",()=>{
  if (city_radio.checked) {
    airport.style.visibility="hidden";
    city.style.visibility="visible";
  }
})
airport_radio.addEventListener("input",()=>{
  if(airport_radio.checked){
    city.style.visibility="hidden";
    airport.style.visibility="visible";
  }
})
