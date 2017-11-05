/*================================================================================
	Item Name: Materialize - Material Design Admin Template
	Version: 4.0
	Author: PIXINVENT
	Author URL: https://themeforest.net/user/pixinvent/portfolio
================================================================================

NOTE:
------
PLACE HERE YOUR OWN JS CODES AND IF NEEDED.
WE WILL RELEASE FUTURE UPDATES SO IN ORDER TO NOT OVERWRITE YOUR CUSTOM SCRIPT IT'S BETTER LIKE THIS. */
function fetchSummary(account_id, customer_id) {
	axios.post('http://127.0.0.1:5100/candy/budget', {
	  "account-id": account_id,
	  "customer-id": customer_id,
	})
	.then(function (resp) {
	  console.log(resp.data.content.budgets);
	  return resp.data.content.budgets
	})
	.catch(function (error) {
	  console.log(error);
	})
}

function fetchSpending(customer_id, current_date) {
	axios.post('http://127.0.0.1:5100/candy/spending', {
	  "customer-id": customer_id,
	  "current-date": current_date,
	})
	.then(function (resp) {
	  console.log(resp.data.content);
	  var balance = document.getElementsByClassName("balance")[0];
	  var rewards = document.getElementById("rew");
	  var savings = document.getElementById("sav");
	  var available = document.getElementById("ava");

	  console.log(balance);

	  var payload = resp.data.content;
	  balance.innerHTML = payload.balance.toFixed(2);
	  rewards.innerHTML = payload.rewards.toFixed(2);
	  savings.innerHTML = payload.savings.toFixed(2);
	  available.innerHTML = (payload.savings+payload.balance).toFixed(2);
	  return resp.data.content;
	})
	.catch(function (error) {
	  console.log(error);
	})
}