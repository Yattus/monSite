// var cadre = document.getElementById('cadre');
// var cadreL = parseFloat(getComputedStyle(cadre).width);
var jobElt = document.getElementById('job');
var maxJob = parseFloat(getComputedStyle(jobElt).width);
var d = 1;
var v = 10;
var jobLActuel = 0;
var cpt = 0;
var t = false;

function funtionAnimation(){
    jobLActuel = parseFloat(getComputedStyle(jobElt).width);

    if(jobLActuel + v > maxJob)
    {
        d *= -1;
        // t = true;
        jobElt.textContent = 'fini fini fini';
    }

    if(jobLActuel <= 0)
    {
        d *= -1;
        // t = true;
        jobElt.textContent = 'debut debut debut';
    }
    changeLargeur();

}

function changeLargeur(){
    jobElt.style.width = (jobLActuel + v*d) + 'px';
    console.log('oui');
    // if(t){
    //     clearInterval(intervalId);
    //     setTimeout(function() {}, 10000);
    //     t = false;
    //     intervalId = setInterval(funtionAnimation, 1000);
    // }
}

// var l = ['j','k','o'];

// funtionAnimation();
intervalId = setInterval(funtionAnimation, 200);
