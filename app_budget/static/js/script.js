// froms------------------------------------------------------------->
function showForm_transactions(e) {
    document.getElementById("formTransactions").style.display = "grid";
    document.getElementById("homeForm").style.display = "grid";

};

function hideForm_transactions(e) {
    document.getElementById("formTransactions").style.display = "none";

};

function showForm_budget(e) {
    document.getElementById("formBudget").style.display = "grid";
};

function hideForm_buget(e) {
    document.getElementById("formBudget").style.display = "none";

};



// main navigatoin------------------------------------------------------->
function showBudget(e) {
    document.getElementById("overview").style.display = "none";
    document.getElementById("budget").style.display = "block";

}


function showIncome(e) {
    document.getElementById("overview").style.display = "grid";
    document.getElementById("budget").style.display = "none";

}

function showTransactions(e) {
    document.getElementById("overview").style.display = "grid";
    document.getElementById("budget").style.display = "none";

}



// forms------------------------------------------------

function showBills(e) {
    document.getElementById("billsForm").style.display = "grid";
    document.getElementById("homeForm").style.display = "none";
    document.getElementById("personalForm").style.display = "none";
    document.getElementById("eatingForm").style.display = "none";
    document.getElementById("carForm").style.display = "none";
    document.getElementById("givingForm").style.display = "none";
}

function showHome(e) {
    document.getElementById("homeForm").style.display = "grid";
    document.getElementById("billsForm").style.display = "none";
    document.getElementById("personalForm").style.display = "none";
    document.getElementById("eatingForm").style.display = "none";
    document.getElementById("carForm").style.display = "none";
    document.getElementById("givingForm").style.display = "none";
}

function showPersonal(e) {
    document.getElementById("homeForm").style.display = "none";
    document.getElementById("billsForm").style.display = "none";
    document.getElementById("personalForm").style.display = "grid";
    document.getElementById("eatingForm").style.display = "none";
    document.getElementById("carForm").style.display = "none";
    document.getElementById("givingForm").style.display = "none";
}

function showEating(e) {
    document.getElementById("homeForm").style.display = "none";
    document.getElementById("billsForm").style.display = "none";
    document.getElementById("personalForm").style.display = "none";
    document.getElementById("eatingForm").style.display = "grid";
    document.getElementById("carForm").style.display = "none";
    document.getElementById("givingForm").style.display = "none";
}



function showCar(e) {
    document.getElementById("homeForm").style.display = "none";
    document.getElementById("billsForm").style.display = "none";
    document.getElementById("personalForm").style.display = "none";
    document.getElementById("eatingForm").style.display = "none";
    document.getElementById("carForm").style.display = "grid";
    document.getElementById("givingForm").style.display = "none";
}


function showGiving(e) {
    document.getElementById("homeForm").style.display = "none";
    document.getElementById("billsForm").style.display = "none";
    document.getElementById("personalForm").style.display = "none";
    document.getElementById("eatingForm").style.display = "none";
    document.getElementById("carForm").style.display = "none";
    document.getElementById("givingForm").style.display = "grid";
}