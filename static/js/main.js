/// <reference path="jquery.d.ts" />



$(document).ready(function(){
    $('#btn_dobiZapiske').click();
});
$(document).on('submit', '#nov_zapisek_form', function (e) {

    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/ustvari/',
        data: {
            naslov: $('#input_naslov').val(),
            besedilo: $('#input_besedilo').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

        },
        success: function () {
            $('#btn_dobiZapiske').click();
        }
    });
});
$('#btn_dobiZapiske').click(function dobiZapiske(e) {
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: '/api/zapiski/',
        dataType: 'json',
        success: function (data) {
            $('#zapiskiDiv').html("")

            $.each(data, function (i, item) {
                $('#zapiskiDiv').append('<div class="zapisek" indeks='+data[i].id+'> <h3>' + data[i].naslov + '</h3>' + data[i].besedilo + '</div>')
            })



        }
    });
});

$('#iskanje').keyup(dobiZadetke);

var ujemajociZadetki = "";
function dobiZadetke() {
    $.ajax({
        type: 'GET',
        url: '/api/iskanje/',
        data: {
            query: $('#iskanje').val()
        },
        dataType: 'json',
        success: function (data) {
            ujemajociZadetki = "";

            $.each(data, function (i, item) {
                ujemajociZadetki += "<li class='searchResult' indeks='" + item.id + "'>" + item.naslov + " " + item.besedilo + "</li>";
            })
            $('#zadetki').html(ujemajociZadetki);


        }
    });
}
$('body').on('click', '#zadetki li', function () {
    $.ajax({
        type: 'GET',
        url: '/api/zapisek/',
        data: {
            id: $(this).attr('indeks')
        },
        dataType: 'json',
        success: function (data) {
            $('#podrobnosti').html("Naslov: " + data.naslov + " Besedilo: " + data.besedilo);


        }
    });
});

// Trigger action when the contexmenu is about to be shown
var idClickedZapisek=0;
$(document).bind("contextmenu", function (event) {

    // Avoid the real one
    

    if(event.target.matches('.zapisek')||event.target.matches('.zapisek h3')){
        event.preventDefault();
        // Show contextmenu
        $(".custom-menu").finish().toggle(100).css({
            top: event.pageY + "px",
            left: event.pageX + "px"
        });
        if(event.target.nodeName=="H3"){
            idClickedZapisek = event.target.closest('.zapisek').getAttribute('indeks');
        }
        else{
            idClickedZapisek = event.target.getAttribute('indeks');
        }
        
    }
    
});


// If the document is clicked somewhere
$(document).bind("mousedown", function (e) {

    // If the clicked element is not the menu
    if (!$(e.target).parents(".custom-menu").length > 0) {

        // Hide it
        $(".custom-menu").hide(100);
    }
});


// If the menu element is clicked
$(".custom-menu li").click(function () {

    // This is the triggered action name
    switch ($(this).attr("data-action")) {

        // A case for each action. Your actions here
        case "delete": izbrisiZapisek(idClickedZapisek); break;
        
    }
    idClickedZapisek=0;
    // Hide it AFTER the action was triggered
    $(".custom-menu").hide(100);
});

function izbrisiZapisek(indeks){
    $.ajax({
        type: 'GET',
        url: '/api/zapisek/izbris/',
        data: {
            id: indeks
        },
        dataType: 'json',
    });
    $('div[indeks="'+indeks+'"]').remove();
}