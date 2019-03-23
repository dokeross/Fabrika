$(document).ready(function(){

  
  
  $(".scrollButton").click(function(){
    $("html, body").animate({scrollTop: $("header").height()+ 480 },"slow");
    
    return false;
  });

  // slick slider

  $('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav'
  });

  $('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    dots: false,
    centerMode: true,
    focusOnSelect: true
  });

  $('.single-item').slick();


  $('.responsive').slick({
    infinite: false,
    speed: 300,
    slidesToShow: 2,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

  // // orderInput
  // $('.contactDetails__input').click(function () {
  //   if (this.checked) {
  //       $('.contactDetails__input').attr('checked',false);
  //       this.checked=true;
  //   };
  // });
  
  // // input in order
  // $("input#Rp").change(function(){
  //   if ($(this).prop('checked')) {
  //     $('#hideRp').fadeIn().show();
  //     $('#hideDc').fadeOut(300);
  //     $('#hidePi').fadeOut(300); 
  //   } else {
  //     $('#hideRp').fadeOut(300); 
  //   }
  // });

  // $("input#Dc").change(function(){
  //   if ($(this).prop('checked')) {
  //     $('#hideDc').fadeIn().show();
  //     $('#hideRp').fadeOut(300);
  //     $('#hidePi').fadeOut(300);
  //   } else {
  //     $('#hideDc').fadeOut(300); 
  //   }
  // });

  // $("input#Pi").change(function(){
  //   if ($(this).prop('checked')) {
  //     $('#hidePi').fadeIn().show();
  //     $('#hideRp').fadeOut(300);
  //     $('#hideDc').fadeOut(300); 
  //   } else {
  //     $('#hidePi').fadeOut(300); 
  //   }
  // });

  // $("input#Ps").change(function(){
  //   if ($(this).prop('checked')) {
  //     $('.paymentSystem').fadeIn().show();
  //   } else {
  //     $('.paymentSystem').fadeOut(300); 
  //   }
  // });


  var choiceDelivery = document.querySelectorAll('.contactDetails__label');
  
  for (var i = 0; i < choiceDelivery.length; i++) {
      choiceControl(choiceDelivery[i]);
  }
  
  function toggleFilter(choice) {
      for (var i = 0; i < choiceDelivery.length; i++) {
        choiceDelivery[i].nextElementSibling.classList.add('hid');
        choiceDelivery[i].firstElementChild.checked=false;
      }
      
      choice.nextElementSibling.classList.remove('hid');
      choice.firstElementChild.checked=true;
      $('#pF').fadeIn().show();
      $('.paymentFact__label').removeClass('paymentFact__error');
  }
  
  function choiceControl(choice) {
      choice.addEventListener('click', function() {
          toggleFilter(choice);
      });
  }
  
  $("input#Rp").change(function(){
      if ($(this).prop('checked')) {
        $('.paymentFact__label').addClass('paymentFact__error');
        $('#pF').fadeOut(300);
      } 
  });

  $('.payment__input').click(function () {
      if (this.checked) {
          $('.payment__input').attr('checked',false);
          this.checked=true;
      };
    });

  // endorderInput

  // yakor
  $(function(){
    $('a[href*=#]').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
        && location.hostname == this.hostname) {
            var $target = $(this.hash);
            $target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
            if ($target.length) {
                var targetOffset = $target.offset().top;
                $('html,body').animate({scrollTop: targetOffset}, 500);//скорость прокрутки
                return false;
            }
        }
    });
  });
  // endyakor


  // panel
  function showingBasket(){
    $('.panelBasket').toggleClass('hidden');
    $('.filter').toggleClass('filterBlur');
  };

  $('.basket').click(function(){
    showingBasket();     
  });
  
  var form = $('.form_buying_product');
  console.log(form);

  function basketUpdating(product_id, nmb, image, is_delete){
    var data = {};
    data.product_id = product_id;
    data.nmb = nmb;
    data.image = image;
    var csrf_token = $('.form_buying_product [name="csrfmiddlewaretoken"]').val();
    data["csrfmiddlewaretoken"] = csrf_token;

    if (is_delete){
      data["is_delete"] = true;
    }

    var url = form.attr("action");

    console.log(data)
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
          console.log("OK");
          console.log(data.products_total_nmb);
          if (data.products_total_nmb || data.products_total_nmb == 0) {
            $('#basket_total_nmb').text(data.products_total_nmb);
            console.log(data.products);
            $('.panelBasket ul').html("");
            $.each(data.products, function(k, v){
              $('.panelBasket ul').append('<li class="basketItem row">' + '<div class="col-4 orderPosition">'
              + '<span class="orderCharacteristic__title">' + v.name + '</span>'
              + '<img src=' + '"' + '/media/' + v.image + '"' + 'class="orderPosition__img' + '"' + '>'
              + '</div>'
              +'<div class="col-2 orderCharacteristic">'
              + '<span class="orderCharacteristic__p">' + v.category + '</span>'
              + '<span class="orderCharacteristic__p">' + v.article + '</span>'
              + '</div>'
              + '<div class="col orderPrice orderPriceJs">'
              // + '<p data-product_id="'+v.id+'" class="basketMin">x</p>'
              + '<img src=' + '"' + '/static/img/basketMin.png' + '"' + 'data-product_id=' + '"' + v.id + '"' + 'class="basketMin' + '"' + '>'
              
              // + '<img src=' + '"' + '{% static' + '"' + 'img/basketMin.png' + '"' + '%}' + "' + data-product_id=' + '"' + v.id + '"' + 'class="basketMin">'
              // <img src="{% static 'img/basketMin.png' %}"  class="basketMin" data-product_id="{{product_in_basket.id}}">
              + '<p class="orderPrice__p">' + v.price_per_item + ' р</p>'
              + '<p class=' + '"' + 'orderPrice__p_min' + '"' + '>за 1' + v.measurement + '</p>'
              + '</div>'
              + '</li>'
              );                
            });
            // $('#orderAmountVal').val(v.nmb);
            
          }
          
        },
        error: function(){
            console.log("error")
        }
    })
  }

  $(document).on('click', '.submit_btn', function(e){
    e.preventDefault();
    product_id = $(this).data("product_id")
    image = $(this).data("image")
    console.log(product_id);
    console.log(image);
    nmb = 0;
    basketUpdating(product_id, nmb, image, is_delete=false)
  });

  // var controls = document.querySelectorAll('.submit_btn');
  // console.log(controls);

  // for (var i = 0; i < controls.length; i++) {
  //   stes(controls[i]);
  // }
  
  // function stes(control){
  //   $(control).click(function(){
  //     form.on('submit',function(e){
  //       e.preventDefault();
  //       console.log(control);
  //       var nmb = $('#number').val();
  //       var submit_btn =$(control).closest('.submit_btn');
  //       var product_id = submit_btn.data("product_id");
  //       var image = submit_btn.data("image");
  //       var product_name = submit_btn.data("product_name")
  //       var product_price = submit_btn.data("product_price")
  //       console.log(submit_btn);
  //       console.log(product_id);
  //       console.log(product_name);
  //       console.log(image);
    
  //       basketUpdating(product_id, nmb, image, is_delete=false);
        
  //     });
      
  //   });
        
  // }


    // $('.panelBasket ul').append('<li class="row">' + '<div class="col-3 orderPosition">'
    // +'<img src="" class="orderPosition__img">'
    // + '</div>'
    // +'<div class="col-5 orderCharacteristic">'
    // + '<span class="orderCharacteristic__title">Темно-розовое</span>'
    // + '<span class="orderCharacteristic__p">Кужево эластичное</span>'
    // + '<span class="orderCharacteristic__p">К001</span>'
    // + '<div class="orderAmount">'
    // + '<input type="number" value="2" autofocus class="orderAmount__input"/>'
    // + '</div>'
    // + '</div>'
    // + '<div class="col orderPrice">'
    // + '<img src="" class="basketMin">'
    // + '<p class="orderPrice__p">250 р</p>'
    // + '</div>'
    // + '</li>');

    // $('.basket-items ul').append('<li>'+name+', ' + nmb + 'шт. ' + 'по ' + price + 'грн  ' +
    // '<a class="delete-item" href="">x</a>'+
    // '</li>');
  

  $(document).on('click', '.basketMin', function(e){
    e.preventDefault();
    product_id = $(this).data("product_id")
    image = $(this).data("image")
    console.log(product_id);
    console.log(image);
    nmb = 0;
    basketUpdating(product_id, nmb, image, is_delete=true)
  });



  function calculatingBasketAmount(){
      var total_order_amount = 0;
      $('.total_product_in_basket_amount').each(function() {
          total_order_amount = total_order_amount + parseFloat($(this).text());
      });
      console.log(total_order_amount);
      $('#total_order_amount').text(total_order_amount.toFixed(2));
  };

  $(document).on('change', ".product_in_basket_nmb", function(){
      var current_nmb = $(this).val();
      console.log('1234');
      console.log(current_nmb);

      var current_oi = $(this).closest('.orderItem');
      var current_price = parseFloat(current_oi.find('.product_price').text()).toFixed(2);
      console.log(current_price);
      var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
      console.log(total_amount);
      current_oi.find('.total_product_in_basket_amount').text(total_amount);

      calculatingBasketAmount();
  });


  calculatingBasketAmount();





// $('#panelBasket').click(function(){
//   if( $('#panel1').attr('class') == 'close' ){
//       $('content').css('display','block');
//       $('#panel1').attr('class','open');
//   }else{
//       $('content').css('display','none');
//       $(this).attr('class','close');
//   }        
// });


  $('.productItem__infoItem').one('click', '.hiddenDescriptionItem__imgLike', function(e){
    e.preventDefault();
    var like = $(this).nextAll('.hiddenDescriptionItem__countLike').text();
    var like = parseInt(like) + parseInt(1);
    var liketrue = $(this).nextAll('.hiddenDescriptionItem__likeTrue').text();
    var product_id = $(this).nextAll('.hiddenDescriptionItem__id').text();
    // $(this).nextAll('.hiddenDescriptionItem__countLike').text(likeAmount);
    console.log(like);
    console.log(liketrue);
    console.log(product_id);
    $(this).addClass('hiddenDescriptionItem__imgLike_active');
    $(this).addClass('hiddenDescriptionItem__imgLike_click');
    
    $(this).nextAll('.hiddenDescriptionItem__countLike').text(like);
    likeAdding(like, liketrue, product_id);
  });
  
  
  function likeAdding(like, liketrue, product_id){
    var data = {};
    data.like = like;
    data.product_id = product_id;
    var csrf_token = $('.hiddenDescriptionItem [name="csrfmiddlewaretoken"]').val();
    data["csrfmiddlewaretoken"] = csrf_token;
    // var urlProducts = $('.hiddenDescriptionItem__countLike');
    // var urlProduct = urlProducts.data("urlproducts");
    // var url = urlProduct + 'like_adding';
    $.ajax({
      url: '/like_adding/',
      type: 'POST',
      data: data,
      cache: true,
      success: function (data) {     
      },
      error: function(){
          console.log("error")
      }
    });
  };




  // $(window).scroll(function() {   
  //   if($(window).scrollTop() + $(window).height() == $(document).height()) {
  //     $.ajax({
  //         url: url,
  //         type: 'POST',
  //         data: data,
  //         cache: true,
  //         success: function (data) {
  //           console.log("OK");
  //           console.log(data.products_total_nmb);
            
  //         },
  //         error: function(){
  //             console.log("error")
  //         }
  //     });
  //   }
  // });


  // about_page

  $(window).bind('scroll',function(e){
    parallaxScroll();
    if ($(this).scrollTop()>=699) {
      $('.mapAbout__p').addClass('show');
    }
    if ($(this).scrollTop()>=917) {
      $('.mapDescription__img').addClass('show');
    }
    if ($(this).scrollTop()>=1297) {
      $('.mapDescription__p').addClass('show');
    }
  });
  
  function parallaxScroll(){
      var scrolled = $(window).scrollTop();
      $('.logoAbout').css('top',(0+(scrolled*.495))+'px');
      // $('.mapAbout').css('top',(0-(scrolled*.895))+'px');
      // $('.logoAbout').css('top',(0-(scrolled*.95))+'px');
  }


  


  // about_page


  // headerBg

  $(window).bind('scroll',function(e){
    if ($(this).scrollTop()>=300) {
      $('.header').addClass('header__bgJs');
    }
    else {
      $('.header').removeClass('header__bgJs');
    }
  });


});  


// aside

$('.filterCatalog').click(function() {
  $('.filterCatalog__fa').toggleClass('filterCatalog__fa_open');
  $('.filterCatalog__hide').toggleClass('show');
  $('.filterCatalog__show').toggleClass('hide');
  $('.smHide').toggleClass('showBlock');


  
})



// endaside

// $(window).scroll(function() {
  //   if ($(this).scrollTop()>=697) {
  //     // длительность анимации - 'slow'
  //     // тип анимации -  'linear'
  //     $('.mapAbout__p').addClass('show');
  //     // var duration = 850; //'slow'
  //     // $(".utp").each(function(index) {
  //     //     $(this).delay(duration * index).fadeIn(duration);
  //     // });

      
  //   }
  // });