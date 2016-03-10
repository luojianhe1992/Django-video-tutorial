/**
 * Created by jianheluo on 3/9/16.
 */


$(function(){
    $('#search_articles').keyup(function(){
        $.ajax({
            type: 'POST',
            url: '/search_articles/',
            data: {
                'search_text': $('#search_articles').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR){
    $('#search_articles_results').html(data)
}