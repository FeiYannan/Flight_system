var customer = document.getElementById('customer');
var booking_agent = document.getElementById('booking_agent')
var airline_staff = document.getElementById('airline_staff')
var customer_wrapper = document.getElementById('customer_wrapper');
var BA_wrapper = document.getElementById('BA_wrapper')
var AS_wrapper = document.getElementById('AS_wrapper');

customer.addEventListener("input",()=>{
  if (customer.checked) {
    BA_wrapper.style.visibility="hidden";
    AS_wrapper.style.visibility="hidden";
    customer_wrapper.style.visibility="visible";

  }
})
booking_agent.addEventListener("input",()=>{
  if(booking_agent.checked){
    customer_wrapper.style.visibility="hidden";
    AS_wrapper.style.visibility="hidden";
    BA_wrapper.style.visibility="visible";
  }
})
airline_staff.addEventListener("input",()=>{
  if(airline_staff.checked){
    customer_wrapper.style.visibility="hidden";
    BA_wrapper.style.visibility="hidden";
    AS_wrapper.style.visibility="visible";
  }
})
