$(document).ready(function () {
    var form = $('#form-buying_book');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log(123);
        var num = $('#number').val();
        console.log(num);
        var submit_btn = $('#submit_btn');
        var book_id = submit_btn.data("book_id");
        var book_title = submit_btn.data("title");
        var book_cost = submit_btn.data("book_cost");
        console.log(book_id);
        console.log(book_title);
        console.log(book_cost);
        
        var data ={};
        data.num = num;
        data.book_id = book_id;
        var csrf_token = $('#form-buying_book [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        console.log(data);

        $.ajax({
            url: url,
            type: 'Post',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
            },
            error: function () {
                console.log("error");
            }
        })

        $('.basket-items ul').append("<li>" + book_title
            + ', ' + num + ', ' + 'books, each costs is ' +  book_cost + ' грн. ' + " <span class='delete-item' href=''>x</span>"+ "</li>")
    });
    $('.basket_container').click( function (e) {
        e.preventDefault();
        $('.basket-items').css('display', "block");
    });
    $('.basket_container').mouseover( function (e) {
        e.preventDefault();
        $('.basket-items').css('display', "block");
    });
    $('.basket_container').mouseleave( function (e) {
        e.preventDefault();
        $('.basket-items').css('display', "none");
    })
    $(document).on('click', '.delete-item', function () {
        $(this).closest('li').remove();
    })
});