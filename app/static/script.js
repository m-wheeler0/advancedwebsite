$(document).ready(function(){

    $("#edit-description").click(function(){
        var desc = $("#display-description");
        var user_input = $("#change-description");

        desc.css('display', 'none');
        user_input.css('display', 'flex');
    });

    $("#save-description").click(function(){
        var user_input = $("#description_user_input").val();

        $.ajax({
            url: '/update_description',
            type: 'POST',
            data: JSON.stringify({new_desc: user_input}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                $("#change-description").hide();
                $("#display-description").show();
                if (user_input){
                    $(".profile-description").text(user_input);
                }
                else{
                    $(".profile-description").text("You currently do not have a description for your profile.");
                }
            }
        });
    });

    $("#order-button").click(function(){
        var game_id = $("#game-id").text();

        $.ajax({
            url: '/order_game',
            type: 'POST',
            data: JSON.stringify({ordered_game_id: game_id}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                alert("Successfully ordered!");
            },
            error:function(){
                alert("Failed.")
            }
        });
    });

    $("#favourite-button").click(function(){
        var game_id = $("#game-id").text();
        var favourite_count_str = ($("#favourites-count-display").text()).replace(/\D/g, '');
        var favourite_count_int = parseInt(favourite_count_str, 10);

        $.ajax({
            url: '/favourite_game',
            type: 'POST',
            data: JSON.stringify({favourite_game_id: game_id}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                alert("Added to favourites!");
                favourite_count_int ++;
                $("#favourites-count-display").text("Favourite Count: " + favourite_count_int);
                $("#favourite-button").css('display', 'none');
                $("#unfavourite-button").css('display', 'inline');
            },
            error:function(){
                alert("Failed.")
            }
        });
    });

    $("#unfavourite-button").click(function(){
        var game_id = $("#game-id").text();
        var favourite_count_str = ($("#favourites-count-display").text()).replace(/\D/g, '');
        var favourite_count_int = parseInt(favourite_count_str, 10);

        $.ajax({
            url: '/unfavourite_game',
            type: 'POST',
            data: JSON.stringify({unfavourite_game_id: game_id}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response){
                alert("Removed from favourites!");
                favourite_count_int --;
                $("#favourites-count-display").text("Favourite Count: " + favourite_count_int);
                $("#favourite-button").css('display', 'inline');
                $("#unfavourite-button").css('display', 'none');
            },
            error:function(){
                alert("Failed.")
            }
        });
    });
});